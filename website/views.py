from django.shortcuts import render
from django.contrib import messages
from .models import Enquiry


def generate_solution(question):
    question = question.lower()

    if any(word in question for word in ["profit", "sales", "revenue"]):
        return {
            "solution": "Focus on increasing profitable sales while controlling operating costs.",
            "tips": [
                "Identify your highest-profit products or services.",
                "Track monthly revenue and expenses.",
                "Improve customer retention.",
                "Review unnecessary business expenses.",
                "Use targeted digital marketing."
            ]
        }

    elif any(word in question for word in ["customer", "customers"]):
        return {
            "solution": "Improve customer acquisition and retention through better service and engagement.",
            "tips": [
                "Collect customer feedback.",
                "Create loyalty programs.",
                "Respond quickly to customer enquiries.",
                "Personalize marketing campaigns.",
                "Track customer satisfaction."
            ]
        }

    elif any(word in question for word in ["marketing", "advertising"]):
        return {
            "solution": "Build a measurable digital marketing strategy.",
            "tips": [
                "Define your target customers.",
                "Use social media consistently.",
                "Create useful content.",
                "Measure campaign performance.",
                "Focus spending on successful channels."
            ]
        }

    elif any(word in question for word in ["cost", "expense", "expenses"]):
        return {
            "solution": "Analyze your expenses and reduce costs that do not contribute to business growth.",
            "tips": [
                "Categorize all monthly expenses.",
                "Automate repetitive operations.",
                "Negotiate supplier costs.",
                "Track your profit margin.",
                "Create a monthly budget."
            ]
        }

    else:
        return {
            "solution": "Analyze the business problem using customer, financial, operational and market data before making a decision.",
            "tips": [
                "Clearly define the business problem.",
                "Collect relevant business data.",
                "Identify possible causes.",
                "Compare multiple solutions.",
                "Measure results after implementation."
            ]
        }


def home(request):
    context = {}

    if request.method == "POST":

        form_type = request.POST.get("form_type")

        if form_type == "solver":
            question = request.POST.get("question", "")
            result = generate_solution(question)

            context["question"] = question
            context["solution"] = result["solution"]
            context["tips"] = result["tips"]

        elif form_type == "calculator":
            try:
                revenue = float(request.POST.get("revenue", 0))
                expenses = float(request.POST.get("expenses", 0))

                profit = revenue - expenses

                margin = (
                    (profit / revenue) * 100
                    if revenue > 0 else 0
                )

                context["revenue"] = revenue
                context["expenses"] = expenses
                context["profit"] = profit
                context["margin"] = round(margin, 2)

            except ValueError:
                messages.error(
                    request,
                    "Please enter valid numbers."
                )

        elif form_type == "enquiry":
            Enquiry.objects.create(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                service=request.POST.get("service"),
                message=request.POST.get("message")
            )

            messages.success(
                request,
                "Your enquiry has been submitted successfully!"
            )

    return render(
        request,
        "website/index.html",
        context
    )
