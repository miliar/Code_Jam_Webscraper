// nerdyninja
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VII;

int solve(char x[], int l, int k)
{
	int i, j;
	int ans = 0;
	for(i = l-1; i >= k-1; i--){
		if(x[i] == '-'){
			ans++;
			for(j = i; j > i-k; j--){
				if(x[j] == '+')x[j] = '-';
				else if(x[j] == '-')x[j] = '+';
			}
		}
	}
	for(i = l-1; i >= 0; i--){
		if(x[i] != '+')return -1;
	}
	return ans;
}

int main()
{
	freopen("A-l.in", "r", stdin);
	freopen("A-l.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int qq = 1; qq <= t; qq++)
	{
		char x[1001];
		scanf("%s", x);
		int k;
		scanf("%d", &k);
		int l = strlen(x);
		int ans = solve(x, l, k);
		if(ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", qq);
		else printf("Case #%d: %d\n", qq, ans);
	}
	return 0;
}