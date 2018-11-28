#include <bits/stdc++.h>
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define pi pair <int, int>
#define ppi pair <pair <int, int>, int>
#define fi first
#define se second
typedef long long ll;

using namespace std;
int a[1005], b[1005];

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	freopen("cruise_large.in", "r", stdin);
	freopen("cruise_large.out", "w", stdout);

	int t=1, l, i, n, d;
	cin>>t;
	float x, y=0;
	for(l=1; l<=t; l++)
	{
		y=0;
		cin>>d>>n;
		for(i=0; i<n; i++)
		{
			cin>>a[i]>>b[i];
			x=(1.0*(d-a[i]))/(1.0*b[i]);
			if(y<x)
				y=x;
		}
		//cout<<y<<endl;
		y=(1.0*d)/y;
		printf("Case #%d: %0.8f\n", l, y);

	}

	return 0;
}