#include <iostream>
#include <limits>

using namespace std;

int main() {
    int nb_test;
    cin >> nb_test;

    for (int t = 1; t <= nb_test; ++t) {
        int dest, nb_horses, pos, speed;
        cin >> dest >> nb_horses;
        double total = numeric_limits<double>::max();

        for (int i = 0; i < nb_horses; ++i) {
            cin >> pos >> speed;

            double dist_from_arr = dest - pos;
            double time_to_arr = dist_from_arr / speed;
            double total_speed = dest / time_to_arr;

            if (total_speed < total)
                total = total_speed;
        }

        cout.precision(15);
        cout << fixed << "Case #" << t << ": " << total << endl;
    }

    return 0;
}


