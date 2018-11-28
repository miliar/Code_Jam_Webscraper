#define _USE_MATH_DEFINES

#include <cstdlib>
#include <climits>
#include <cmath>

#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

#include <algorithm>
#include <utility>

#include <vector>
#include <map>
#include <list>
#include <set>

using namespace std;

double solve(int D, vector<int>& K, vector<int>& S) {
	vector<double> distance;
	vector<double> time;
	vector<int> speed;
	int N = K.size();
	for (int i = N - 1; i >= 0; i--) {
		vector<double> d;
		vector<double> t;
		vector<int> s;

		double d_travelled = K[i], t_travelled = 0;
		int c_speed = S[i];

		d.push_back(d_travelled);
		t.push_back(t_travelled);
		s.push_back(c_speed);

		if (i < N - 1) {
			int n = distance.size();
			bool caught_up = false;
			for (int k = 1; k < n; k++) {
				double their_time = time[k];
				double their_distance = distance[k];
				double travelled = (their_time - t_travelled) * c_speed;
				if (d_travelled + travelled <= their_distance) {
					// not yet caught up
					d_travelled += travelled;
					t_travelled = their_time;
				}
				else {
					// will catch up...

					// calculate intersect
					double their_speed = speed[k - 1];

					double r_speed = c_speed - their_speed;
					double sep = their_distance - d_travelled;
					double catchup_time = sep / r_speed;

					t_travelled += catchup_time;
					d_travelled += c_speed * catchup_time;
					c_speed = their_speed;

					d.push_back(d_travelled);
					t.push_back(t_travelled);
					s.push_back(c_speed);

					// add the rest of their data;
					for (int kk = k + 1; kk < n; kk++) {
						d.push_back(distance[kk]);
						t.push_back(time[kk]);
						s.push_back(speed[kk]);
					}
					caught_up = true;
					// done
					break;
				}
			}

			double their_end_speed = speed[n - 1];
			// catch up after last change?
			if (!caught_up && c_speed > their_end_speed) {
				double their_distance = distance[n - 1];
				double their_speed = their_end_speed;

				double r_speed = c_speed - their_speed;
				double sep = their_distance - d_travelled;
				double catchup_time = sep / r_speed;

				t_travelled += catchup_time;
				d_travelled += c_speed * catchup_time;
				c_speed = their_speed;

				d.push_back(d_travelled);
				t.push_back(t_travelled);
				s.push_back(c_speed);
			}
		}

		distance = move(d);
		time = move(t);
		speed = move(s);
	}

	// when does the first horse pass the goal?
	double time_taken = -1;

	int n = distance.size();
	for (int i = 1; i < n; i++) {
		if (distance[i] >= D) {
			time_taken = time[i] - (distance[i] - D) / speed[i - 1];
			break;
		}
	}
	if (time_taken == -1) {
		time_taken = time[n - 1] + (D - distance[n - 1]) / speed[n - 1];
	}

	double avg_speed = D / time_taken;
	return avg_speed;
}

class Comp {
	const vector<int>& K;

public:
	Comp(const vector<int>& K)
		: K(K)
	{}

	bool operator() (int i, int j) {
		return K[i] < K[j];
	}
};

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		// read input
		int D, N;
		cin >> D >> N;
		vector<int> k, s, indices;
		k.reserve(N);
		s.reserve(N);
		for (int n = 0; n < N; n++) {
			int ki, si;
			cin >> ki >> si;
			k.push_back(ki);
			s.push_back(si);
			indices.push_back(n);
		}

		sort(indices.begin(), indices.end(), Comp(k));

		vector<int> K, S;
		for (int n = 0; n < N; n++) {
			K.push_back(k[indices[n]]);
			S.push_back(s[indices[n]]);
		}

		// calculate solution

		cout << "Case #" << (t + 1) << ": ";

		// output solution
		double sol = solve(D, K, S);
		cout.setf(ios::scientific);
		cout.precision(10);
		cout << sol;

		cout << endl;
	}
}