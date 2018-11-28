#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	int iter = 1;
	while (iter <= t) {
		string s;
		cin >> s;
		int k;
		cin >> k;

		int count = 0;
		for (int i = 0; i < s.size()-k+1; i++) {
			if (s[i] == '+')
				continue;
			count++;
			for (int j = i; j < i+k; j++) 
				if (s[j] == '+')	s[j] = '-';
				else				s[j] = '+';
		}

		bool all_happy = true;
		for (int i = s.size()-k+1; i < s.size(); i++)
			all_happy = all_happy && (s[i] == '+');

		if (all_happy)
			cout << "Case #" << iter << ": " << count << "\n";
		else
			cout << "Case #" << iter << ": " << "IMPOSSIBLE\n";
		iter++;
	}
}