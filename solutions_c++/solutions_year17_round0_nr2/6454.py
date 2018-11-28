#include <bits/stdc++.h>

using namespace std;

#define INF 2000000000
#define MOD 1000000007
typedef long long ll;
typedef pair<int, int> P;


int main()
{
	int t;
	cin >> t;

	for (int ii = 1; ii <= t; ii++) {
		string s;
		cin >> s;

		for (int i = s.size()-1; i > 0; i--) {
			if (s[i-1]-'0'> s[i]-'0') {
				s[i] = '9';
				if (s[i-1]=='1') {
					s[i-1] = '0';
					for (int j = i; j > 0; j--) {
						s[j] = '9';
					}
					s.erase(0,1);
					break;
				} else {
					int tmp = (s[i-1]-'0')-1;
					s[i-1] = tmp + '0';
					for (int j = i; j < s.size(); j++) {
						s[j] = '9';
					}

				}
			} else if (s[i]=='0') {
				s[i] = '9';
			}
		}
		cout << "Case #" << ii << ": " << s << "\n";
	}
}
