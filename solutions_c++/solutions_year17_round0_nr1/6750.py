#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int N; cin>>N;
	for(int n = 1 ; n <= N ; n++) {
		string s;
		int k;
		cin >> s >> k;

		int ret = 0;
		for (int i = 0 ; i <= s.size() - k ; i++) {
			if (s[i] == '-') {
				ret ++ ; 
				for(int j = i ; j < i + k ; j++) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}

		cout<<"Case #" << n <<": ";
		if (s.find('-') != string::npos)
			cout << "IMPOSSIBLE" << endl;
		else 
			cout<< ret <<endl;
	}
	return 0;
}