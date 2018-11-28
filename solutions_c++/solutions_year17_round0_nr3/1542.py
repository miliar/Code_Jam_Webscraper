#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char** argv) {
	int t;
	cin >> t;
	for(int iter = 0; iter < t; iter++) {
		cout << "Case #" << iter + 1 << ": ";
        long long n, k;
        cin >> n >> k;

        long long v = 0;
        while((v << 1) + 1 < k) {
            v = (v << 1) + 1;
        }

        long long cell = (n - v) / (v + 1);
        long long left = (n - v) % (v + 1);

        if (k - v <= left) cell++;
        cell--;

        if (cell % 2 == 0) {
            cout << cell / 2 << " " << cell / 2 << endl;
        } else {
            cout << cell / 2 + 1 << " " << cell / 2 << endl;
        }
	}
	return 0;
}
