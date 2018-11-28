#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#define min(a,b) a>b ? b:a
#define INF 987654321
int dp[1001];
int k, n;

int solve(int idx, char *S){
	if (idx + k > n){
		for (int i = 0; i < n; ++i)
			if (S[i] == '-')
				return INF;
		return 0;
	}
	int ret;
	/*int &ret = dp[idx];
	if (ret <= INF){
		printf("%d %d\n", idx, ret);
		return ret;
	}*/
	//안뒤집기
	ret = solve(idx + 1, S);
	//뒤집기
	if (idx + k <= n){
		for (int i = 0; i < k; ++i)
			if (S[idx + i] == '+')
				S[idx + i] = '-';
			else
				S[idx + i] = '+';
		ret = min(ret, solve(idx + 1, S) + 1);
		for (int i = 0; i < k; ++i)
			if (S[idx + i] == '+')
				S[idx + i] = '-';
			else
				S[idx + i] = '+';
	}
	return ret;
}
void main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		char S[1001];
		scanf("%s%d", &S, &k);
		n = strlen(S);
		

		memset(dp, 0x3f3f3f3f, sizeof(dp));
		
		int res = solve(0, S);

		cout << "Case #" << i << ": ";
		if (res < INF)
			cout << res << " " << endl;
		else
			cout << "IMPOSSIBLE" << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}