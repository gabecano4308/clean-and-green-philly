from typing import Tuple

import geopandas as gpd

from src.validation.base import ValidationResult, validate_output
from src.validation.li_complaints import LIComplaintsOutputValidator

from ..constants.services import COMPLAINTS_SQL_QUERY
from ..data_utils.kde import apply_kde_to_input


@validate_output(LIComplaintsOutputValidator)
def li_complaints(
    input_gdf: gpd.GeoDataFrame,
) -> Tuple[gpd.GeoDataFrame, ValidationResult]:
    """
    Applies kernel density estimation (KDE) analysis for L&I complaints to the primary feature layer.

    Args:
        primary_featurelayer (FeatureLayer): The feature layer containing property data.

    Returns:
        FeatureLayer: The input feature layer with KDE analysis results for L&I complaints,
        including density and derived metrics.

    Tagline:
        Analyzes L&I complaint density

    Columns added:
        l_and_i_complaints_density (float): KDE density of complaints.
        l_and_i_complaints_density_zscore (float): Z-score of complaint density.
        l_and_i_complaints_density_label (str): Categorized density level.
        l_and_i_complaints_density_percentile (float): Percentile rank of density.

    Primary Feature Layer Columns Referenced:
        geometry

    Source:
        https://phl.carto.com/api/v2/sql

    """
    return apply_kde_to_input(
        input_gdf, "L and I Complaints", COMPLAINTS_SQL_QUERY, batch_size=20000
    )
