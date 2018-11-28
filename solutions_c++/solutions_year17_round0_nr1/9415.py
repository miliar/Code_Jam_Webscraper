#include <iostream>
#include <string>
using namespace std;

int main () {
	int N, k;
	string s;

	cin >> N;
	for(int l=0; l<N; l++) {
		cin >> s >> k;
		int len = s.length();
		int tot = 0;
		for(int i=0; i<len-k+1; i++) {
			if (s[i] == '-') {
				tot++;
				for(int j=i; j<i+k; j++) {
					if (s[j] == '-') s[j] = '+';
					else			 s[j] = '-';
				}
			}
		}

		bool success = true;
		for(int i=0; i<len; i++) {
			if (s[i] == '-')
				success = false;
		}

		cout << "Case #" << l+1 << ": ";
		if (success)
			cout << tot << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}