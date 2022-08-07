from scipy import signal
import matplotlib.pyplot as p


def main():
    print("BODE PLOT GENERATOR\n")
    print("""Given a continuous LTI transfer function with numerator and denominator in expanded polynomial form,
    enter the coefficients in descending order, starting with the term of highest order.""")
    print("NOTE: If the numerator and denominator are not fully simplified/expanded, this will not work!\n")
    print("Example 1: For numerator s^2 + s + 2, input is '1 1 2'.")
    print("Example 2: For denominator 5s^4 + 2s^3 + s + 1, input is '5 2 0 1 1'.")
    while True:
        while True:
            n, d = get_num_den()
            tf = validate(n, d)
            if tf:
                get_bode(tf)
                again = input("\nPress any key to enter more data, or type '0' to exit. ").strip()
                if again == "0":
                    return False


def get_num_den():
    """Get user num/den input"""
    n = input("\nEnter the numerator coefficients, separated by single spaces: ")
    d = input("Enter the denominator coefficients, separated by single spaces: ")
    return n, d


def validate(n, d):
    """Validate user input and process transfer function args"""
    try:
        tf = process_tf_args(n, d)  # If valid, process tf args
        return tf
    except:
        print("\nERROR: Invalid input.")    # Else, return error message and prompt for new input
        return False


def process_tf_args(n, d):
    """Process vals for num/den, gather into list for transfer function args"""
    num = list(map(float, n.split()))
    den = list(map(float, d.split()))
    tf = signal.TransferFunction(num, den)  # tf(num, den, dt=None)
    return tf


def get_bode(tf):
    """Get Bode mag/phase plots from transfer function data"""
    w, mag, phase = tf.bode()
    p.figure()
    p.semilogx(w, mag) # Bode magnitude plot
    p.grid()
    p.ylabel("Magnitude (dB)")
    p.xlabel("Frequency (rad/s)")
    p.figure()
    p.semilogx(w, phase)  # Bode phase plot
    p.grid()
    p.ylabel("Phase (deg)")
    p.xlabel("Frequency (rad/s)")
    p.show()
    return


if __name__ == "__main__":
    main()
