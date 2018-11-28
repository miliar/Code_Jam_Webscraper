#include <iostream>
#include <sstream>
#define ull unsigned long long int
using namespace std;

string N;

ull process() {
	int i, sz;
	int back = 0;
	string res;
	ull ret;
	N = "0" + N;
	sz = N.length();
	//cout << "Doing " << N << endl;
	//cout << "Going forward..." << endl;
	for(i=1;i<sz;++i) {
		//cout << N[i];
		if (N[i]<N[i-1]) {
			--N[i-1];
			//cout << "... Oops, problemo!" << endl;
			back = i-1;
			//cout << "Now I am " << N << endl;
			break;
		}
	}
	
	if (back) {
		for(i=back;i>0;--i) {
			if (N[i]>=N[i-1]) {
				res = N.substr(1,i) + string(sz-(i+1),'9');	
				//cout << "All good to go as " << res << endl;
				break;
			} else {
				--N[i-1];
				//cout << "Now I am " << N << endl;
			}
		}
	} else {
		res = N.substr(1);
		//cout << "No problem! " << res << endl;
	}
	
	stringstream ss; ss.clear(); ss.str(res);
	ss >> ret;
	return ret;
}

int main() {
	int tc, t;
	cin >> t;
	for(tc=1; tc <= t; ++tc) {
		cin >> N;
		
		cout << "Case #" << tc << ": " << process() << endl;
	}
	return 0;
}