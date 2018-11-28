#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll solve(string s) {
	int j = 0;
	for (unsigned i = 0; i < s.size() - 1; i++)
	{			
		if (s[i] > s[i+1]) {
			s[j]--;				
			
			for (unsigned k = j + 1; k < s.size(); k++)
				s[k] = '9';				
				
			break;
		}
		else if (s[i] != s[i + 1])
			j = i + 1;
	}

	return stoll(s);
}

int main() {
	freopen("in-large", "r", stdin);
	freopen("out-large", "w", stdout);
	int T;
	string n;

	cin >> T;
	for(int it = 1; it <= T; ++it) {
		cin >> n;
		printf("Case #%d: %lld\n", it, solve(n));
	}
	
	fclose(stdout);
	return 0;
}
