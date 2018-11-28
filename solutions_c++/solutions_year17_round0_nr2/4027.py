// https://code.google.com/codejam/contest/3264486/dashboard#s=p1
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <iostream>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdint>

using namespace std;

typedef long long ll;

string solve(string S)
{
	string ans;
	int L = S.length();
	for (int i=0; i<L; i++) {
		int j = L - i - 1;
		if (j == 0 && S[j] == '0')
			return string(L - 1, '9');
		if (j > 0 && S[j - 1] > S[j]) {
			S[j - 1] = S[j - 1] - 1;
			ans = string(ans.length()+1, '9');
		} else {
			ans = S[j] + ans;
		}
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string N;
		cin >> N;
		auto ans = solve(N);
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
