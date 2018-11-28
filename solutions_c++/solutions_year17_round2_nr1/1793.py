#include<iostream>
#include<math.h>
#include<vector>
#include<iomanip>

using namespace std;

int main(){
	int T;
	cin >> T;
	int D;
	int N;
	for(int i = 0; i<T; i++){
		cin >> D;
		cin >> N;
		double start;
		double speed;
		double time;
		double maxtime = 0;
		double anniespeed;
		for (int j = 0; j<N; j++){
			cin >> start;
			cin >> speed;
			time = (D-start)/speed;
			maxtime = time > maxtime ? time :  maxtime;
		}
		anniespeed = D/maxtime;
		cout << "Case #" << i+1 << ": " << setprecision(10) << anniespeed << endl;
	}
	return 0;
}