#include <iostream>
#include <iomanip>

#include <limits.h>
using namespace std;

int main() {
    int ncase = 0;
    cin >> ncase;
    for (int round = 1; round <= ncase; ++round) {
		long long dis, n;
		cin >> dis >> n;
		long long gp_start = dis;
		long long gp_speed = INT_MAX;
		double time_off = 0.0;
		for(long i = 0; i < n; ++i) {
			long long start, speed;;
			cin >> start >> speed;
//			cout << "-" << gp_start << "," << gp_speed << endl;
//			cout << start << "," << speed << endl;
			if (start <= gp_start && speed <= gp_speed) {
				gp_start = start;
				gp_speed = speed;
				time_off = 0.0;
				continue;
			}

			if (start >= gp_start && speed >= gp_speed) {
				continue;
			}

			if (speed <= gp_speed) {
				double time = (double)(start - gp_start) / (gp_speed - speed);
				if ((double)start + speed * time > dis) continue;
				gp_speed = speed;
				gp_start = start + time * speed;
				time_off += time;
				continue;
			}

			if (speed >= gp_speed) {
				double time = (double)(gp_start - start) / (speed - gp_speed);
				if ((double)start + speed * time < dis) continue;
				gp_speed = speed;
				gp_start = start;
				time_off = 0;
				continue;
			}
		}

		double total_time = time_off + (double)(dis - gp_start) / gp_speed;
		double speed = dis / total_time;
		    std::cout << std::fixed;
			    std::cout << std::setprecision(10);

        cout << "Case #" << round << ": ";
        cout << speed << endl;
    }
    return 0;
}
