//In the name of Allah
#include <bits/stdc++.h>
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
const int N=2e5+7;

int main()
{
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
	freopen ("Out.txt","w",stdout);
	freopen ("in.in","r",stdin);

	int t, n, p, ans, num, sum=0, x[4];

	cin >> t;

	for(int tt=1 ; tt<=t ; tt++)
	{
		cin >> n >> p;

		x[0]=x[1]=x[2]=x[3]=sum=0;

		for(int i=0 ; i<n ; i++)
		{
			cin >> num;
			x[num%p]++;
		}

		ans = x[0];

		if(p==2)
			ans += x[1]/2 + (x[1]%2);

		else if(p==3)
		{
			if(x[1]<x[2])
				ans += x[1] + (x[2]-x[1])/3 + ((x[2]-x[1])%3!=0);

			else
				ans += x[2] + (x[1]-x[2])/3 + ((x[1]-x[2])%3!=0);
		}

		else if(p==4)
		{
			ans += x[2]/2;

			if(x[1]<x[3])
				ans += x[1] + (x[3]-x[1])/4 + (x[2]%2 && (x[3]-x[1])%4>=2)
					+ ( (x[2]%2 && (x[3]-x[1])%4<2) || (x[2]%2==0 && (x[3]-x[1])%4)
							|| ((x[3]-x[1])%4==3) );

			else
				ans += x[3] + (x[1]-x[3])/4 + (x[2]%2 && (x[1]-x[3])%4>=2)
					+ ( (x[2]%2 && (x[1]-x[3])%4<2) || (x[2]%2==0 && (x[1]-x[3])%4)
							|| ((x[1]-x[3])%4==3) );
		}

		cout << "Case #" << tt << ": " << ans << '\n';
	}

	return 0;
}
