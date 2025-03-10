from __future__ import annotations

from typing import Final

DOMAIN: Final = "promql-fork"

CONF_QUERY = "query"

DEFAULT_NAME = "Prometheus"
DEFAULT_HOST = "http://192.168.120.9:9090"
DEFAULT_VERIFY_SSL = False

PROMETHEUS_API_PATH = "/api/v1/query"

PROMETHEUS_METRIC_KEY = "metric"
PROMETHEUS_VALUE_KEY = "value"
PROMETHEUS_JOB_KEY = "job"
PROMETHEUS_INSTANCE_KEY = "instance"
