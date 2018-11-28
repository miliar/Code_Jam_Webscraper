
#include<bits/stdc++.h>
using namespace std;
#define D(x)	cout << #x " = " << (x) << endl
#define xx		first
#define yy		second
typedef long long int LL;
typedef pair<LL, LL> pll;

pll solve(LL n, LL k)
{
	LL mid = ( n + 1 ) / 2;
	if(k == 1) return pll(n - mid, mid - 1);
	
	k = k - 1;
	if(k & 1) return solve(n - mid, (k + 1) / 2);
	return solve(mid - 1, k / 2);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int t, cs;
	LL n, k;
	
	scanf("%d", &t);
	for(cs = 1; cs <= t; cs++)
	{
		cin >> n >> k;
		pll result = solve(n, k);
		
		printf("Case #%d: %I64d %I64d\n", cs, result.xx, result.yy);
	}
	return 0;
}
