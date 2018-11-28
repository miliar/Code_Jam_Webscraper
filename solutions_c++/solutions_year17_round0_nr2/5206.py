#include <iostream>
#include <cmath>
using namespace std;

int GetNumberOfDigits (long long i)
{
    return i > 0 ? (long long) log10 ((double) i) + 1 : 1;
}
long long res = 0;
long long n;
bool solution;
void cRes (int k, int b, long long sol) {
	//cout << k << " " << b <<  endl;
	if (k == -1) {
		//cout << sol << endl;
		res = max(sol, res);
		solution = true;
		return;
	}

	for (int i = 9; i >= b && !solution; i--) {
		if (i*pow(10, k) <= n - sol) {
			//cout << i << endl;
			//cout << sol + i*pow(10, k) << endl;
			cRes(k - 1, i, sol + i*pow(10, k));
		}
	}
}

int main() {
	int tc; cin >> tc;
	int cont =0 ;
	while (tc--) {
		cont++;
		cin >> n;
		res = 0;
		solution = false;
		int k = GetNumberOfDigits(n);
		cRes(k - 1, 0, 0);
		cout << "Case #" << cont << ": " << res << endl;

	}


}	