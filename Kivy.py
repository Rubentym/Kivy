# Implementation of a mobile app expense tracker using Kivy
# Users can add expenses, categorize spending, and view summaries

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ExpenseTrackerApp(App):
    def __init__(self):
        super().__init__()
        self.expenses = {}

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.category_input = TextInput(hint_text="Category")
        self.amount_input = TextInput(hint_text="Amount")
        add_button = Button(text="Add Expense")
        add_button.bind(on_press=self.add_expense)
        self.summary_label = Label(text="")
        layout.add_widget(self.category_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(add_button)
        layout.add_widget(self.summary_label)
        return layout

    def add_expense(self, instance):
        category = self.category_input.text
        amount = float(self.amount_input.text)
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)
        self.category_input.text = ""
        self.amount_input.text = ""

    def view_summary(self):
        summary = ""
        for category, expenses in self.expenses.items():
            total = sum(expenses)
            summary += f"{category}: ${total}\n"
        self.summary_label.text = summary

if __name__ == '__main__':
    ExpenseTrackerApp().run()
