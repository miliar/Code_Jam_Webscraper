#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

//g++ -std=c++11 cruise_control.cpp -o main && ./main < test.in

int main () {
	int t;
	cin >> t;

	for(int i=1; i<=t; i++) {
		// d - destination, n - num horses, k - start pos, s - speed
		double d, n, k_i, s_i, t_i=0;
		cin >> d >> n;

		cin >> k_i >> s_i;
		t_i = max(t_i,(d-k_i)/s_i);

		for(int j=1; j<n; j++){
			cin >> k_i >> s_i;
			t_i = max(t_i,(d-k_i)/s_i);
		}

		cout << "Case #" << i << ": " << std::setprecision(10) << d/t_i << endl;
	}
	return 0;
}
