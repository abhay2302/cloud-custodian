# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0

import pytest
from c7n.config import Config
from c7n.ctx import ExecutionContext
from c7n_tencentcloud.client import Session


@pytest.fixture(scope="package")
def vcr_config():
    return {"filter_headers": ["authorization"]}


@pytest.fixture
def session():
    return Session()


@pytest.fixture
def client_cvm(session):
    return session.client("cvm.tencentcloudapi.com", "cvm", "2017-03-12", "ap-singapore")


@pytest.fixture
def client_tag(session):
    return session.client("tag.tencentcloudapi.com", "tag", "2018-08-13", "ap-singapore")


@pytest.fixture
def options():
    return Config.empty(**{
        "region": "ap-singapore"  # just for init, ignore the value
    })


@pytest.fixture
def ctx(session, options):
    return ExecutionContext(session, {}, options)
