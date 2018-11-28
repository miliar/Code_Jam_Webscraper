
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <map>
#include <iomanip>


using namespace std;


// void printVec(vector<pair<double, double>> v) {
// 	for (int i = 0; i < v.size(); ++i) {
// 		cout << v[i].first << " " << v[i].second << endl;
// 	}
// 	cout << endl;
// }



double getMaxSpeed(double dist, vector<pair<double, double>> horses) {

	// printVec(horses);
	sort(horses.rbegin(), horses.rend());
	// printVec(horses);

	double mx_t = (dist - horses[0].first) / horses[0].second;
	for (auto horse : horses) {
		double t = (dist - horse.first) / horse.second;
		if (mx_t < t) {
			mx_t = t;
		}
	}

	double res = (double)dist / (double)mx_t;
	return res;
}



int main() {
	
	
	// ifstream in("in.in");
	// ofstream out("out.out");

	// ifstream in("A-small-attempt1.in");
	// ofstream out("A-small-attempt1.out");


	ifstream in("A-large.in");
	ofstream out("A-large.out");


	out.setf(ios::showpoint);
	out.precision(6);
	out.setf(ios::fixed);



	
	int n;
	double D, N, start, speed;
	in >> n;
	
	
	for (int i = 1; i <= n; ++i) {
		in >> D >> N;
		vector<pair<double, double>> horses;
		for (int j = 0; j < N; ++j) {
			in >> start >> speed;
			horses.push_back({start, speed});
		}
		double res = getMaxSpeed(D, horses);
		out << "Case #" << i << ": " << res << endl;
	}
	
	

	// cout.setf(ios::showpoint);
	// cout.precision(6);
	// cout.setf(ios::fixed);

	// vector<pair<double, double>> horses1{{2400,5}};
	// cout << getMaxSpeed(2525, horses1) << endl;

	// vector<pair<double, double>> horses2{{120,60},{60,90}};
	// cout << getMaxSpeed(300, horses2) << endl;

	// vector<pair<double, double>> horses3{{80,100},{70,10}};
	// cout << getMaxSpeed(100, horses3) << endl;


}


