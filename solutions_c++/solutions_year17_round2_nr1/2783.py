#include <iostream>
#include <string>
#include <list>
#include <set>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
	int T, D, N;
	double K, S, distLeft, Max = 0, time, MaxSpeed;
	freopen("A-large", "r", stdin);
	freopen("file.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> D;
		cin >> N;
		Max = 0;
		for(int k = 0; k < N; k++) {
			cin >> K;
			cin >> S;
			distLeft = D - K;
			time = distLeft/S;
			if(time > Max) {
				Max = time;
			}
		}
		MaxSpeed = D/Max;
		cout << "Case #" << i+1 << ": " << fixed << setprecision(10) << MaxSpeed << endl;
	}
	return 0;
}