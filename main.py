import sys
import requests
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QStackedWidget,
    QPushButton, QHBoxLayout, QSizePolicy, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import (
    QUrl, QTimer, Qt, QPropertyAnimation, QEasingCurve, pyqtSignal, QThread, QObject
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QColor, QMouseEvent, QFont
from web3 import Web3
from eth_account import Account

class EthDataFetcher(QObject):
    """
    Fetches Ethereum data such as current price and gas fees periodically.
    Emits signals with the fetched data.
    """
    data_fetched = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_data)
        self.timer.start(60000)  # Fetch every 60 seconds
        self.fetch_data()  # Initial fetch

    def fetch_data(self):
        try:
            # Fetch ETH price from CoinGecko
            price_response = requests.get(
                'https://api.coingecko.com/api/v3/simple/price',
                params={
                    'ids': 'ethereum',
                    'vs_currencies': 'usd'
                }
            )
            price_data = price_response.json()
            eth_price = price_data.get('ethereum', {}).get('usd', 'N/A')

            # Fetch gas prices from Etherscan
            gas_response = requests.get(
                'https://api.etherscan.io/api',
                params={
                    'module': 'gastracker',
                    'action': 'gasoracle',
                    'apikey': '3M7EZ6RV3HH5T5BP8AQ1MV2XTRPS5YMF48'
                }
            )
            gas_data = gas_response.json()
            
            if gas_data.get('status') == "1":
                gas_prices = gas_data['result']
                safe_gas_price = gas_prices.get('SafeGasPrice', 'N/A')
                propose_gas_price = gas_prices.get('ProposeGasPrice', 'N/A')
                fast_gas_price = gas_prices.get('FastGasPrice', 'N/A')
            else:
                raise Exception("Error fetching gas data from Etherscan")

            # Prepare data
            data = {
                'eth_price': eth_price,
                'safe_gas_price': safe_gas_price,
                'propose_gas_price': propose_gas_price,
                'fast_gas_price': fast_gas_price
            }

            # Emit signal with data
            self.data_fetched.emit(data)

            # Print to CLI
            print(f"ETH Price: ${eth_price} | Safe Gas Price: {safe_gas_price} Gwei | "
                  f"Propose Gas Price: {propose_gas_price} Gwei | Fast Gas Price: {fast_gas_price} Gwei")
            print('Join us at discord.gg/solana-scripts')

        except Exception as e:
            print(f"Error fetching ETH data: {e}")




def create_buy_transaction(account, private_key, recipient, value, gas_price, gas_limit):
    # Connect to Ethereum node (e.g., Infura)
    infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
    w3 = Web3(Web3.HTTPProvider(infura_url))


    private_key_1 = '0xYOUR_PRIVATE_KEY_1'
    private_key_2 = '0xYOUR_PRIVATE_KEY_2'

    account_1 = '0xADDRESS_1'
    account_2 = '0xADDRESS_2'

    nonce = w3.eth.get_transaction_count(account)
    
    # Build the transaction
    tx = {
        'nonce': nonce,
        'to': recipient,  # Address where the buy transaction is directed
        'value': w3.toWei(value, 'ether'),  # Amount of Ether to send
        'gas': gas_limit,
        'gasPrice': w3.toWei(gas_price, 'gwei'),  # Gas price
        'chainId': 1  # Ethereum mainnet
    }
    
    # Sign the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    
    return signed_tx


def flash_bundle(recipient_1, recipient_2, value_1, value_2, gas_price, gas_limit):
    # Create two buy transactions
    #signed_tx1 = create_buy_transaction(account_1, private_key_1, recipient_1, value_1, gas_price, gas_limit)
    #signed_tx2 = create_buy_transaction(account_2, private_key_2, recipient_2, value_2, gas_price, gas_limit)

    #tx_bundle = [signed_tx1, signed_tx2]

    #print("Transaction 1 Hash:", signed_tx1.hash.hex())
    #print("Transaction 2 Hash:", signed_tx2.hash.hex())
    
    #print("Flash Bundle created with two transactions:")
    #print(f" - Transaction 1: {value_1} ETH to {recipient_1}")
    #print(f" - Transaction 2: {value_2} ETH to {recipient_2}")
    
    # Example: return bundle data for further processing or submission
    return True

# Example usage
recipient_1 = '0xRECIPIENT_ADDRESS_1'
recipient_2 = '0xRECIPIENT_ADDRESS_2'
value_1 = 0.1  # Amount of ETH for the first transaction
value_2 = 0.2  # Amount of ETH for the second transaction
gas_price = 50  # Gas price in Gwei
gas_limit = 21000  # Basic gas limit for a simple ETH transfer

# Create a flash bundle with two transactions
flash_bundle(recipient_1, recipient_2, value_1, value_2, gas_price, gas_limit)


# -------------------- Modern Loading Screen --------------------

class ModernLoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: #1e1e1e;
            color: white;
            border-radius: 20px;
        """)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        # Drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(shadow)

        # Loading label
        self.label = QLabel("Loading eth-bundler.com...")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
        """)
        layout.addWidget(self.label)

        # Spinner
        self.spinner = QLabel("🔄")
        self.spinner.setAlignment(Qt.AlignCenter)
        self.spinner.setStyleSheet("""
            font-size: 60px;
            margin-top: 10px;
        """)
        layout.addWidget(self.spinner)

        # Start spinner animation
        self.start_spinner()

    def start_spinner(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_spinner)
        self.timer.start(150)

    def update_spinner(self):
        spinner_symbols = ['🔄', '🔃', '🔁', '🔂']
        current_text = self.spinner.text()
        next_index = (spinner_symbols.index(current_text) + 1) % len(spinner_symbols)
        self.spinner.setText(spinner_symbols[next_index])

# -------------------- Web Engine with Error Handling --------------------

class WebEngineWithErrorHandling(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setUrl(QUrl("https://eth-bundler.com/app"))
        self.setZoomFactor(1.5)  # Scale to 150%
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if not success:
            self.setHtml("""
                <h1 style='color:white; text-align:center; margin-top:20%;'>
                    Failed to load eth-bundler.com.<br>Please check your connection.
                </h1>
            """, QUrl())
            print("Error: Failed to load website")
        else:
            print("Web page loaded successfully")

# -------------------- Modern Control Bar --------------------

class ModernControlBar(QWidget):
    minimize_requested = pyqtSignal()
    close_requested = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(50)
        self.setStyleSheet("""
            background-color: #282828;
            color: white;
        """)
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 0, 20, 0)
        self.setLayout(layout)

        # Title label
        self.title_label = QLabel("eth-bundler.com - Launch effortlessly on Ethereum")
        self.title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
        """)
        layout.addWidget(self.title_label)

        layout.addStretch()

        # Minimize button
        self.minimize_button = QPushButton("_")
        self.minimize_button.setFixedSize(40, 30)
        self.minimize_button.setStyleSheet(self.button_style())
        self.minimize_button.clicked.connect(self.minimize_requested.emit)
        layout.addWidget(self.minimize_button)

        # Close button
        self.close_button = QPushButton("X")
        self.close_button.setFixedSize(40, 30)
        self.close_button.setStyleSheet(self.button_style())
        self.close_button.clicked.connect(self.close_requested.emit)
        layout.addWidget(self.close_button)

    def button_style(self):
        return """
            QPushButton {
                background-color: #3c3c3c;
                color: white;
                border: none;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #ff6666;
            }
            QPushButton:pressed {
                background-color: #ff4d4d;
            }
        """

# -------------------- Main Window --------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()

        # Central widget and layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Control bar
        self.control_bar = ModernControlBar(self)
        self.control_bar.minimize_requested.connect(self.minimize_window)
        self.control_bar.close_requested.connect(self.close_window)
        main_layout.addWidget(self.control_bar)

        # Stacked widget for loading screen and web view
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # Loading screen
        self.loading_screen = ModernLoadingScreen()
        self.stacked_widget.addWidget(self.loading_screen)

        # Web view
        self.web_view = WebEngineWithErrorHandling()
        self.stacked_widget.addWidget(self.web_view)

        # Show loading screen first
        self.stacked_widget.setCurrentWidget(self.loading_screen)

        # Animation for fading out the loader
        self.animation_opacity = QPropertyAnimation(self.loading_screen, b"windowOpacity")
        self.animation_opacity.setDuration(1000)
        self.animation_opacity.setStartValue(1.0)
        self.animation_opacity.setEndValue(0.0)
        self.animation_opacity.setEasingCurve(QEasingCurve.OutCubic)
        self.animation_opacity.finished.connect(self.hide_loading_screen)

        # Timer to switch to web view after 1 second
        self.loader_timer = QTimer()
        self.loader_timer.timeout.connect(self.show_web_view)
        self.loader_timer.start(1000)  # 1 second

        # Solid background
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c2c2c;
            }
            QWidget {
                background-color: #2c2c2c;
            }
        """)

        # Start Ethereum data fetcher in a separate thread
        self.eth_thread = QThread()
        self.eth_fetcher = EthDataFetcher()
        self.eth_fetcher.moveToThread(self.eth_thread)
        self.eth_fetcher.data_fetched.connect(self.handle_eth_data)
        self.eth_thread.started.connect(self.eth_fetcher.fetch_data)
        self.eth_thread.start()

        # Dragging variables
        self.is_dragging = False

    def show_web_view(self):
        self.animation_opacity.start()

    def hide_loading_screen(self):
        self.stacked_widget.setCurrentWidget(self.web_view)
        self.loading_screen.hide()

    def minimize_window(self):
        self.showMinimized()

    def close_window(self):
        self.eth_thread.quit()
        self.eth_thread.wait()
        self.close()

    def handle_eth_data(self, data):
        eth_price = data.get('eth_price', 'N/A')
        gas_price = data.get('gas_price', 'N/A')
        # You can also update the GUI with this data if needed

    # Drag and move functionality
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.is_dragging and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.is_dragging = False
        event.accept()

# -------------------- Entry Point --------------------

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Set custom application font
    font = QFont("Arial", 10)
    app.setFont(font)

    # Launch the main window
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
