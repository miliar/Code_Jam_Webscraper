#include<bits/stdc++.h>
using namespace std;

void change(string& test, int pos, int k)
{
	for(int i=0; i<k; ++i)
		test[pos+i] = (test[pos+i]=='-')? '+':'-';
}

int solve(string& test, int k)
{
	int ans = 0;
	for(int i=0; i+k-1<test.length(); ++i) {
		if(test[i]=='-') {
			++ans;
			change(test, i, k);
		}
	}

	return ans;
}

bool check(string& test)
{
	for(auto& c: test)
		if(c == '-')
			return false;
	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	cin >> t;

	for(int i=1; i<=t; ++i) {
		string test;
		int k;
		cin >> test >> k;

		int ans = solve(test, k);

		cout << "Case #" << i << ": ";
		if(check(test))
			cout << ans;
		else
			cout << "IMPOSSIBLE";
		cout << "\n";
	}

	return 0;
}
