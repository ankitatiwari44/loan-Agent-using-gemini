from gemini.gemini_client import evaluate_eligibility
from data.input_data import pl_applicant, sme_applicant


def run():

    print(" Personal Loan Eligibility ")
    result1 = evaluate_eligibility(pl_applicant)
    print(result1)

    print("\n SME Loan Eligibility ")
    result2 = evaluate_eligibility(sme_applicant)
    print(result2)


if __name__ == "__main__":
    run()