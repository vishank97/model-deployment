# Replace `YOUR_WORKSPACE_FQN`
# with the actual value.
import logging

from servicefoundry import Build, PythonBuild, Service, Resources

logging.basicConfig(level=logging.INFO)
service = Service(
    name="flask",
    image=Build(
        build_spec=PythonBuild(
            command="gunicorn -b 0.0.0.0:8000 main:app",
        ),
    ),
    ports=[{"port": 8000}],
    resources=Resources(memory_limit=1500, memory_request=1000),
)
service.deploy(workspace_fqn="v1:tfy-dev-cluster:vishank-betatest-ws")