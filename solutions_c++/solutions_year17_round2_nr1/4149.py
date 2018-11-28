#include <iostream>
#include <algorithm>
#include <fstream>
#include <iomanip>
using namespace std;

double sol[100];

int main() {
	ofstream file;
	file.open("Out.in");
	int T;
	cin >> T;
	for (int i = 0;i < T;i++) {
		double distination;
		int n;
		cin >> distination >> n;
		double maxTime = 0;
		double arr[100][2];
		for (int j = 0;j < n;j++) {
			double pos, speed;
			cin >> pos >> speed;
			arr[j][0] = pos;
			arr[j][1] = speed;
		}
		for (int i = 0;i < n;i++) {
			for (int j = 0;j < n;j++) {
				if (arr[i][0] > arr[j][0]) {
					double temp1 = arr[i][0];
					double temp2 = arr[i][1];
					arr[i][0] = arr[j][0];
					arr[i][1] = arr[j][1];
					arr[j][0] = temp1;
					arr[j][1] = temp2;
				}
			}
		}
		for (int j = n-1;j >=0;j--) {
			double tim;
			tim = (distination - arr[j][0]) / arr[j][1];
			maxTime = max(maxTime, tim);
		}
		sol[i] = distination / maxTime;
	}
	file << fixed << setprecision(10);
	for (int i = 0;i < T;i++) {
		file << "Case #" << i + 1;
		
		file << ": ";
		file << (double)sol[i] << '\n';
	}
	return 0;
}


