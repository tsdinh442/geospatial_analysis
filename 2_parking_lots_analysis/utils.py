
from pyproj import Proj

def read_jgw_file(jgw_file_path):
    with open(jgw_file_path, 'r') as jgw_file:
        lines = jgw_file.readlines()
        transformation_params = {
            'A': float(lines[0].strip()),  # Pixel width
            'D': float(lines[1].strip()),  # Rotation parameter
            'B': float(lines[2].strip()),  # Rotation parameter
            'E': float(lines[3].strip()),  # Pixel height
            'C': float(lines[4].strip()),  # x-coordinate of the upper-left corner of the image
            'F': float(lines[5].strip())   # y-coordinate of the upper-left corner of the image
        }
    return transformation_params


def utm_to_lat_long(easting, norting, zone=14, ellps='WGS84', hemisphere='N'):
    """
    """
    proj = Proj(proj='utm', zone=zone, ellps=ellps, hemisphere=hemisphere)
    lon, lat = proj(easting, norting, inverse=True)

    return lon, lat