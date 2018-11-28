#include <iostream>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<int> vi;
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end();i++)
#define present(c,x) ((c).find(x)!=(c).end())
#define pb push_back
#define ll long long
#define index(i,j) ((i)*12+(j))

ll k[1005];
ll s[1005];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	ll D;
	int N;
	scanf("%d",&T);
	double ans;
	for(int t = 1 ;t <= T;t++)
	{
		scanf("%lld%d",&D,&N);
		for(int i = 1; i<= N;i++)
			scanf("%lld%lld",&k[i],&s[i]);
		double tt = 0;
		double tmp;
		for(int i = 1; i<= N;i++)
		{
			tmp = (D-k[i])*1.0 / s[i];
			if(tt < tmp)
			{
				tt = tmp;
			}
		}
		ans = D*1.0/tt;
		printf("Case #%d: %.6lf\n",t,ans);

	}
	
return 0;
}