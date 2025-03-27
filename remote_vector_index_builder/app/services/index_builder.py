# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import logging
from typing import Optional, Tuple
from app.models.workflow import BuildWorkflow
from core import run_tasks

logger = logging.getLogger(__name__)


class IndexBuilder:
    """
    Handles the building of indexes based on provided workflows.
    """

    def build_index(
        self, workflow: BuildWorkflow
    ) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Builds the index for the given workflow, using the run_tasks function

        Args:
            workflow (BuildWorkflow): Workflow containing index build parameters

        Returns:
            Tuple[bool, Optional[str], Optional[str]]: A tuple containing:
                - Success status (True/False)
                - Index path if successful, None otherwise
                - Error message if failed, None otherwise
        """
        result = run_tasks(workflow.index_build_parameters)
        if not result.remote_path:
            return False, None, result.error
        return True, result.remote_path, None
