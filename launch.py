import requests
import argparse

class AWXClient:
    """A class to interact with the AWX API."""

    def __init__(self, awx_url, token):
        """
        Initializes the AWX client.

        :param awx_url: Base URL of the AWX API (e.g., "http://awx-server/api/v2").
        :param token: API authentication token.
        """
        self.awx_url = awx_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def trigger_job(self, job_template_id, extra_vars=None):
        """
        Triggers a job template execution in AWX.

        :param job_template_id: ID of the job template to launch.
        :param extra_vars: Dictionary of extra variables for the job.
        :return: Job ID if successful, None otherwise.
        """
        url = f"{self.awx_url}/job_templates/{job_template_id}/launch/"
        payload = {"extra_vars": extra_vars} if extra_vars else {}

        response = requests.post(url, json=payload, headers=self.headers)

        if response.status_code == 201:
            job_id = response.json().get("id")
            print(f"✅ Job triggered successfully! Job ID: {job_id}")
            return job_id
        else:
            print(f"❌ Failed to trigger job: {response.status_code}")
            print(response.text)
            return None

# job launch
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AWX URL and Job template ID")
    parser.add_argument("--awx_url", type=str, required=True, help="AWX URL")
    parser.add_argument("--job_template_id", type=int, required=True, help="Your Job Template ID")
    args= parser.parse_args()

    # Configuration
    #AWX_URL = "http://51.254.116.97:8052/api/v2"  # Replace with your AWX server URL
    TOKEN = "3KEEHyNaPY1AM6kth5RNacnSJtuMit"  # Replace with your actual token
    #JOB_TEMPLATE_ID = 16  # Replace with your job template ID

    # Create an instance of AWXClient
    awx_client = AWXClient(args.awx_url, TOKEN)

    # Trigger the job
    awx_client.trigger_job(args.job_template_id, extra_vars={"example_var": "value"})
