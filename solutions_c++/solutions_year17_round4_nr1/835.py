
/* 
Take yourself as work in progress.
-Bhai
*/

#include<bits/stdc++.h>
using namespace std;

#define M 1000000007
#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define VI vector<int>
#define SZ(a) int(a.size())
#define TR(c, it) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
#define SET(a, b) memset(a, b, sizeof(a))

int N, P;
int arr[105];

int solve4()
{
	int a[4] = {0,0,0,0};
	for(int i=0; i<N; i++)
		a[arr[i]%4]++;
	int ans=  0;

	ans = a[0];
	ans += (a[2])/2;
	a[2] = a[2]%2;

	int lo = min(a[1], a[3]);
	int hi = max(a[1], a[3]);

	ans += lo;
	hi -= lo;

	if(a[2])
	{
		ans += 1;
		hi -= 2;
		ans += (max(0, hi)+3)/4;
	}
	else
	{
		ans += (hi+3)/4;		
	}

	return ans;		
}

int solve3()
{
	int a[3] = {0,0,0};
	for(int i=0; i<N; i++)
		a[arr[i]%3]++;
	int ans;
	ans = a[0];
	int lo = min(a[1], a[2]);
	int hi = max(a[1], a[2]);

	ans += lo;
	hi -= lo;
	ans += (hi+2)/3;
	return ans;
}

int solve2()
{
	int a[2]= {0,0};
	for(int i=0; i<N; i++)
		a[arr[i]%2]++;
	int ans;
	ans = a[0] + (a[1]+1)/2;
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	int nahoy = 1;
	while(t--)
	{
		cin >> N >> P;
		for(int i=0; i<N; i++)
			cin >> arr[i];
		int ans;
		if(P==2) ans = solve2();
		else if(P==3) ans = solve3();
		else ans = solve4();
		printf("Case #%d: %d\n", nahoy, ans);
		nahoy++;
	}
	return 0;
}
