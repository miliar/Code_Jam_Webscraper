#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <queue>
#include <list>
#include <utility>
#include <functional>
#include <numeric>
#include <algorithm>

using std::cin; using std::cout; using std::endl; using std::string; using std::vector;

int solve(int testcase);

int main(int argc, char *argv[]){

#ifndef ONLINE_JUDGE
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif 

	::std::ios::sync_with_stdio(false); ::std::cin.tie(0); ::std::cout.tie(0);

	int testcase;
	cin >> testcase;
	for(int t = 1; t <= testcase ; ++ t)
		solve(t);

	return 0;
}

char inverse(char c){
	return c == '-' ? '+' : '-';
}
int solve(int testcase)
{

	string s;
	int k;
	cin >> s;
	cin >> k;

	int const n = s.length();
	vector<int> v( 2 + n );
	// 1 <= k <= n;
	int ans = 0;
	for(int i = 0; i + k <=n ; ++i)
	{
		if (s[i] == '-')
		{
			for(int j = 0; j < k; ++j)
			{
				s[i + j] = inverse( s[ i + j ] );
			}
			++ans;
		}
	}

	bool yes = true;
	for(int i = 0; i !=n ; ++i){
		yes = yes && s[i] == '+';

	}
	cout << "Case #"<< testcase << ": ";
	if (yes)cout << ans << '\n'; else cout << "IMPOSSIBLE\n";

	return 0;
}
