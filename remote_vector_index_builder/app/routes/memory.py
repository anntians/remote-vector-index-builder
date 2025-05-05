# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from fastapi import APIRouter, HTTPException, Request

import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/_memory")
def memory(request: Request) -> str:
    job_service = request.app.state.job_service
    return f"_available_gpu_memory: {job_service.resource_manager._available_gpu_memory}, _available_cpu_memory: {job_service.resource_manager._available_cpu_memory}, total_gpu_memory: {job_service.total_gpu_memory}, total_cpu_memory: {job_service.total_cpu_memory}"
