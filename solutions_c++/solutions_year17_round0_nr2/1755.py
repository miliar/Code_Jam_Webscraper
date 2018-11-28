#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long int ll;

const int MAXSIZE = 100;
const int INF = 2000*1000*1000;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie();

	int T;
	cin >> T;
	for(int t=1; t<=T; ++t) {
		string s;
		cin >> s;

		size_t conflict_pos = -1;
		for(size_t i=0; i<s.length()-1; ++i)
			if (s[i+1] < s[i]) {
				int j = i;
				while (j-1 >= 0 && s[j] == s[j-1]) j--;
				conflict_pos = j;
				break;
			}
		string ans = s;
		if (conflict_pos != -1) {
			ans[conflict_pos] = char(int(ans[conflict_pos]) - 1);
			for(size_t i=conflict_pos+1; i<ans.length(); ++i)
				ans[i] = '9';
		}
		size_t first_non_zero = 0;
		while (first_non_zero < ans.length() && ans[first_non_zero] == '0') first_non_zero++;
		ans = ans.substr(first_non_zero, ans.length() - first_non_zero);

		cout << "Case #" << t << ": " << ans;
		if (t != T) cout << endl;
	}

	return 0;
}