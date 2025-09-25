from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            income = float(request.form.get('income', 0))
            rent = float(request.form.get('rent', 0))
            groceries = float(request.form.get('groceries', 0))
            utilities = float(request.form.get('utilities', 0))
            other = float(request.form.get('other', 0))

            total_expenses = rent + groceries + utilities + other
            cash_flow = income - total_expenses

            result = {
                'income': income,
                'total_expenses': total_expenses,
                'cash_flow': cash_flow,
                'status': 'positive' if cash_flow >= 0 else 'negative'
            }
        except ValueError:
            result = {'error': 'Please enter valid numbers.'}

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
