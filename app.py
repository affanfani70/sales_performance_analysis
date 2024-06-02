from flask import Flask, request, jsonify
from llm_integration import analyze_sales_data
from data_ingestion import load_sales_data

app = Flask(__name__)

# Load the sales data
sales_data = load_sales_data("sales_performance_data.csv")


@app.route("/api/rep_performance", methods=["GET"])
def rep_performance():
    rep_id = request.args.get("employee_id")
    rep_data = sales_data[sales_data["employee_id"] == int(rep_id)]

    prompt = f"Analyze the performance of sales representative with ID {rep_id} based on the following data: {rep_data.to_dict()}."
    insights = analyze_sales_data(prompt)

    return jsonify({"rep_id": rep_id, "insights": insights})


@app.route("/api/team_performance", methods=["GET"])
def team_performance():
    prompt = f"Analyze the overall sales team performance based on the following data: {sales_data.to_dict()}."
    insights = analyze_sales_data(prompt)

    return jsonify({"team_insights": insights})


@app.route("/api/performance_trends", methods=["GET"])
def performance_trends():
    time_period = request.args.get("time_period")
    prompt = f"Analyze sales performance trends and provide forecasting for the {time_period} period based on the following data: {sales_data.to_dict()}."
    insights = analyze_sales_data(prompt)

    return jsonify({"time_period": time_period, "trends_and_forecasting": insights})


if __name__ == "__main__":
    app.run(debug=True)
