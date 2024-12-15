import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class GuessingGame:
    def __init__(self, lower_bound=1, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.secret_number = random.randint(lower_bound, upper_bound)
        self.attempts = 0
        self.max_attempts = 10

    def reset_game(self):
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0

    def make_guess(self, guess):
        self.attempts += 1
        if guess < self.lower_bound or guess > self.upper_bound:
            return "Ваше число вне диапазона!"
        if guess < self.secret_number:
            return "Слишком низко!"
        elif guess > self.secret_number:
            return "Слишком высоко!"
        else:
            return "Поздравляем! Вы угадали число!"

    def is_game_over(self):
        return self.attempts >= self.max_attempts

    def remaining_attempts(self):
        return self.max_attempts - self.attempts

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.game = GuessingGame()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Игра "Угадай число"')
        self.layout = QVBoxLayout()

        self.label = QLabel(f"Я загадал число от {self.game.lower_bound} до {self.game.upper_bound}.")
        self.layout.addWidget(self.label)

        self.attempts_label = QLabel(f"Осталось попыток: {self.game.remaining_attempts()}")
        self.layout.addWidget(self.attempts_label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите ваше число")
        self.layout.addWidget(self.input_field)

        self.submit_button = QPushButton('Угадать')
        self.submit_button.clicked.connect(self.make_guess)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def make_guess(self):
        try:
            guess = int(self.input_field.text())
            result = self.game.make_guess(guess)
            QMessageBox.information(self, 'Результат', result)

            self.attempts_label.setText(f"Осталось попыток: {self.game.remaining_attempts()}")

            if result == "Поздравляем! Вы угадали число!":
                self.ask_to_continue()
            elif self.game.is_game_over():
                QMessageBox.information(self, 'Игра окончена', f"Игра окончена! Я загадал число {self.game.secret_number}.")
                self.game.reset_game()
                self.update_label()
                self.attempts_label.setText(f"Осталось попыток: {self.game.remaining_attempts()}")
        except ValueError:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите целое число.')

        self.input_field.clear()

    def ask_to_continue(self):
        reply = QMessageBox.question(self, 'Поздравляем!', 'Хотите сыграть еще раз?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.game.reset_game()
            self.update_label()
            self.attempts_label.setText(f"Осталось попыток: {self.game.remaining_attempts()}")
        else:
            QApplication.quit()

    def update_label(self):
        self.label.setText(f"Я загадал число от {self.game.lower_bound} до {self.game.upper_bound}. У вас есть {self.game.max_attempts} попыток.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec_())