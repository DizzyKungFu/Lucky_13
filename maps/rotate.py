import math


def quaternion_multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return [
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    ]


def quaternion_conjugate(q):
    w, x, y, z = q
    return [w, -x, -y, -z]


def rotate_vector_by_quaternion(v, q):
    # Convert vector to pure quaternion
    v_quat = [0.0] + v
    q_conj = quaternion_conjugate(q)

    # q * v * q^-1
    temp = quaternion_multiply(q, v_quat)
    rotated = quaternion_multiply(temp, q_conj)

    return rotated[1:]  # Return only the vector part


def create_rotation_quaternion(axis, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    half_angle = angle_radians / 2
    sin_half = math.sin(half_angle)
    x, y, z = axis
    return [
        math.cos(half_angle),
        x * sin_half,
        y * sin_half,
        z * sin_half
    ]

