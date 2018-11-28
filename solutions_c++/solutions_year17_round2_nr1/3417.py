// Example program
#include <iostream>
#include <string>
#include <vector>
#include <limits>

using namespace std;

struct Horse {
public:
	double location;
	double speed;

	Horse(double l, double s) : location(l), speed(s) {
		//empty

	}
};



int main() {


	double D, N;
	double numTests;
	int ind = 0;
	cin >> numTests;
	while (numTests > 0) {
		vector<Horse> horses;
		double total_time = 0;
		cin >> D;
		cin >> N;
		for (int i = 0; i < N; i++) {
			double init_loc, max_speed;
			cin >> init_loc;
			cin >> max_speed;
			horses.push_back(Horse(init_loc, max_speed));
		}
		for (int i = horses.size() - 1; i >= 0; i--) {
			double newTime = (D - horses[i].location) / horses[i].speed;
			if (newTime > total_time) {
				total_time = newTime;
			}

		}
		ind++;
		numTests--;
		cout << "Case #" << ind << ": " << fixed << D / total_time << endl;
	}


}

