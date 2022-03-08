import intake  # Import this first to avoid circular imports during discovery.
from .xarray_container import RemoteXarray

import intake.container

intake.container.register_container('databroker-xarray', RemoteXarray)
