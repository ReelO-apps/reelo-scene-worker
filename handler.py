import runpod

def handler(job):
    job_input = job.get("input", {})
    return {
        "ok": True,
        "echo": job_input,
    }

runpod.serverless.start({"handler": handler})
