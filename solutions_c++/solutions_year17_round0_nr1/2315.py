#include <bits/stdc++.h>
using namespace std;

#define IOS std::ios_base::sync_with_stdio(false);std:cin.tie(0);std::cout.tie(0);
typedef long long ll;

bool last[1010];

int main() {
	IOS
	int casos;
	cin >> casos;

	string s;
	int k;
	
	for(int caso = 1; caso <= casos; caso++) {
		int ans = 0;
		memset(last, 0, sizeof last);
		cin >> s >> k;
		k--;
		bool volt = false;
		for(int i = 0; i < s.size(); i++) {
			int temp = s[i] == '+';
			temp += volt; temp %= 2;
			if(temp == 0 && i + k < s.size()) {
				volt = !volt;
				last[i+k] = true;
				ans++;
			}
			else if(temp == 0) {
				ans = -1;
				break;
			}
			if(last[i])
				volt = !volt;
		}
		cout << "Case #" << caso << ": ";
		if(ans == -1)
			cout << "IMPOSSIBLE" << "\n";
		else
			cout << ans << "\n";

	}

	return 0;
}
