#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int tc=1;tc<=T;++tc) {
		long long n, k;
		cin >> n >> k;
		
		long long linterval=1, sinterval=0, lintl=n, sintl=n-1;

		cout << "Case #" << tc << ": ";
		while (true) {
//cerr << "there are now " << linterval << " long intervals of length " << lintl << " and " << sinterval << " short intervals of length " << sintl << endl;
//			cerr << k << " people remaining\n";
			if (k<=linterval) {
				cout << (lintl)/2 << " " << (lintl-1)/2 << endl;
//				cerr << "last person got a long interval\n";
				break;
			}
			if (k<=linterval+sinterval) {
				cout << (sintl)/2 << " " << (sintl-1)/2 << endl;
//				cerr << "last person got a short interval\n";
				break;
			}
//			cerr << linterval + sinterval << " people take a seat\n";
			k-=linterval+sinterval;

			if (lintl&1) {
				linterval=2*linterval+sinterval;
			} else {
				sinterval=2*sinterval+linterval;
			}
			lintl/=2;
			sintl=lintl-1;
		}
//cerr << endl << endl;
	}
	return 0;
}