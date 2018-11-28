#include <iostream>
#include <iomanip>
#include <limits>
#include <cassert>

using namespace std;

typedef unsigned long long ull;

int main() {
    int num_inputs;
    cin >> num_inputs;

    for (int i = 0; i < num_inputs; i++) {
        ull destination = 0;
        int other_horses = 0;
        double max_speed = numeric_limits<double>::max();

        cin >> destination >> other_horses;

        for (int j = 0; j < other_horses; j++) {
            ull tmp_position = 0;
            int tmp_speed = 0;
            cin >> tmp_position >> tmp_speed;

            double tmp_max_speed =
                (1.0 * destination) / (1.0 * (destination - tmp_position)/ (1.0 * tmp_speed));
            
            if (tmp_max_speed < max_speed) {
                max_speed = tmp_max_speed;
            }
        }

        cout << "Case #" << i+1 << ": " << fixed << setprecision(6) << max_speed << endl;
    }
    return 0;
}

