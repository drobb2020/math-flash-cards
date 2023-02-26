import random

from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "core/index.html", context)


def addition(request):
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    if request.method == "POST":
        answer = request.POST["answer"]
        org_num1 = request.POST["org_num1"]
        org_num2 = request.POST["org_num2"]
        if not answer:
            result = "No answer provided!"
            color = "warning"
            context = {
                "answer": answer,
                "num1": num1,
                "num2": num2,
                "result": result,
                "color": color,
            }
            return render(request, "core/addition.html", context)

        answer = int(answer)
        correct_answer = int(org_num1) + int(org_num2)
        if answer == correct_answer:
            result = (
                "Correct 👍: "
                + str(org_num1)
                + " + "
                + str(org_num2)
                + " is equal to "
                + str(answer)
            )
            color = "success"
        else:
            result = (
                "Incorrect 👎: "
                + str(org_num1)
                + " + "
                + str(org_num2)
                + " is not equal to "
                + str(answer)
                + " it is equal to "
                + str(correct_answer)
            )
            color = "danger"

        context = {
            "answer": answer,
            "result": result,
            "num1": num1,
            "num2": num2,
            "color": color,
        }
        return render(request, "core/addition.html", context)

    context = {"num1": num1, "num2": num2}
    return render(request, "core/addition.html", context)


def subtraction(request):
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    if request.method == "POST":
        answer = request.POST["answer"]
        org_num1 = request.POST["org_num1"]
        org_num2 = request.POST["org_num2"]
        if not answer:
            result = "No answer provided!"
            color = "warning"
            context = {
                "answer": answer,
                "num1": num1,
                "num2": num2,
                "result": result,
                "color": color,
            }
            return render(request, "core/subtraction.html", context)

        answer = int(answer)
        correct_answer = int(org_num1) - int(org_num2)
        if answer == correct_answer:
            result = (
                "Correct 👍: "
                + str(org_num1)
                + " - "
                + str(org_num2)
                + " is equal to "
                + str(answer)
            )
            color = "success"
        else:
            result = (
                "Incorrect 👎: "
                + str(org_num1)
                + " - "
                + str(org_num2)
                + " is not equal to "
                + str(answer)
                + " it is equal to "
                + str(correct_answer)
            )
            color = "danger"

        context = {
            "answer": answer,
            "result": result,
            "num1": num1,
            "num2": num2,
            "color": color,
        }
        return render(request, "core/subtraction.html", context)

    context = {"num1": num1, "num2": num2}
    return render(request, "core/subtraction.html", context)


def multiplication(request):
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    if request.method == "POST":
        answer = request.POST["answer"]
        org_num1 = request.POST["org_num1"]
        org_num2 = request.POST["org_num2"]
        if not answer:
            result = "No answer provided!"
            color = "warning"
            context = {
                "answer": answer,
                "num1": num1,
                "num2": num2,
                "result": result,
                "color": color,
            }
            return render(request, "core/multiplication.html", context)

        answer = int(answer)
        correct_answer = int(org_num1) * int(org_num2)
        if answer == correct_answer:
            result = (
                "Correct 👍: "
                + str(org_num1)
                + " x "
                + str(org_num2)
                + " is equal to "
                + str(answer)
            )
            color = "success"
        else:
            result = (
                "Incorrect 👎: "
                + str(org_num1)
                + " x "
                + str(org_num2)
                + " is not equal to "
                + str(answer)
                + " it is equal to "
                + str(correct_answer)
            )
            color = "danger"

        context = {
            "answer": answer,
            "result": result,
            "num1": num1,
            "num2": num2,
            "color": color,
        }
        return render(request, "core/multiplication.html", context)

    context = {"num1": num1, "num2": num2}
    return render(request, "core/multiplication.html", context)


def division(request):
    num1 = random.randint(0, 10)
    num2 = random.randint(1, 10)
    if request.method == "POST":
        answer = request.POST["answer"]
        org_num1 = request.POST["org_num1"]
        org_num2 = request.POST["org_num2"]
        if not answer:
            result = "No answer provided!"
            color = "warning"
            context = {
                "answer": answer,
                "num1": num1,
                "num2": num2,
                "result": result,
                "color": color,
            }
            return render(request, "core/division.html", context)

        answer = float(answer)
        correct_answer = int(org_num1) / int(org_num2)
        if answer == correct_answer:
            result = (
                "Correct 👍: "
                + str(org_num1)
                + " / "
                + str(org_num2)
                + " is equal to "
                + str(answer)
            )
            color = "success"
        else:
            result = (
                "Incorrect 👎: "
                + str(org_num1)
                + " / "
                + str(org_num2)
                + " is not equal to "
                + str(answer)
                + " it is equal to "
                + str(correct_answer)
            )
            color = "danger"

        context = {
            "answer": answer,
            "result": result,
            "num1": num1,
            "num2": num2,
            "color": color,
        }
        return render(request, "core/division.html", context)

    context = {"num1": num1, "num2": num2}
    return render(request, "core/division.html", context)
