
class BIOSwimmer:
    def __init__(self):
        self.x_acceleration = 0.0
        self.y_acceleration = 0.0
        self.z_acceleration = 0.0
        self.roll_rate = 0.0
        self.pitch_rate = 0.0
        self.yaw_rate = 0.0
        self.dvl_valid = False
        self.v_north = 0.0
        self.v_east = 0.0
        self.v_surface = 0.0
        self.compass_pitch = 0.0
        self.compass_direction = 0.0
        self.compass_roll = 0.0
        self.gps_sat_status = False
        self.gps_latitude = 0.0 
        self.gps_longitude = 0.0
        self.gps_speed_east = 0.0
        self.gps_speed_north = 0.0
        self.gps_altitude = 0.0 
        self.gps_num_satellites = 0.0
        self.gps_hdop = 0.0
        self.gps_bearing = 0.0 
        self.depth = 0.0
        self.tick_count = 0.0
        self.motor1_position = 0.0
        self.motor2_position = 0.0
        self.motor3_position = 0.0
        self.motion_state = 0.0
        self.time_stamp = 0

    