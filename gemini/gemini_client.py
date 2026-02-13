from config import client, MODEL_NAME

PROMPT = """
You are a loan eligibility pre-screener agent used by a bank.

Follow STRICT rule-based evaluation.

For PERSONAL LOAN RULES:
Age: 21–60
Income ≥ 25,000
Bureau score ≥ 700
EMI ≤ 50% of income

For SME LOAN RULES:
Age: 25–65
Bureau score ≥ 680
Business vintage ≥ 2 years
Turnover ≥ 10 lakh
GST available
ITR available

Return JSON Response :

{
 "verdict": "Eligible / Not Eligible",
 "reason": "specific reason"
}
"""


def evaluate_eligibility(applicant_data):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""
        {PROMPT}

        Applicant Data:
        {applicant_data}
        """
    )

    return response.text
