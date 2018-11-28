/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
* File Name : a.cpp
* Purpose : Google Code Jam 2017 (1B)
* Creation Date : 22-04-2017
* Last Modified : Sat 22 Apr 2017 19:47:55 EEST
* Created By : Vasilis Livanos <basilis3761@yahoo.gr>
_._._._._._._._._._._._._._._._._._._._._.*/

#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

vector<long> K(1001);
vector<int> S(1001);

int main() {
	int T, N, imax;
	long D, max;
	double speed;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> D; 
		cin >> N;
		cin >> K[0];
		cin >> S[0];
		max = D - K[0];
		imax = 0;
		for(int i = 1; i < N; i++) {
			cin >> K[i];
			cin >> S[i];
			if(S[imax]*(D - K[i]) > S[i]*max) {
				max = D - K[i];
				imax = i;
			}
		}
		speed = (double) S[imax]*K[imax] / (D - K[imax]) + S[imax];
		
		cout << fixed;
		cout << setprecision(6);
		cout << "Case #" << t << ": " << speed << endl;
	}
	return 0;
}
