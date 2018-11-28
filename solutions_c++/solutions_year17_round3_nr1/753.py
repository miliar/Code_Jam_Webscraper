#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define M_PI 3.14159265358979323846
struct pancake
{
	ll r, h, ar;
};
vector<pancake> cakes;
bool sortByRadius(const pancake &a, const pancake &b) {
	return a.r > b.r;
}
int main() {
	int n,k,t;
	ll r, h;
	pancake cake;
    //freopen("./in.txt", "r", stdin);
    //freopen("./out.txt", "w", stdout);
	scanf("%d", &t);
	for(int l=1;l<=t;l++)
	{
		scanf("%d %d", &n, &k);
		for (int i=0;i<n;i++)
		{
			scanf("%lld %lld", &r, &h);
			ll ar = 2*r*h;
			cake.r = r;
			cake.h = h;
			cake.ar = ar;
			cakes.push_back(cake);
		}
		sort(cakes.begin(), cakes.end(), sortByRadius);
		ll ans1=0;
		for(int i=0;i<n;i++)
		{
			ll ans = (cakes[i].r*cakes[i].r)+cakes[i].ar;
			vector<ll> foo;
			int ctr = 1;
			for (int j=i+1; j<n;j++)
			{
			  foo.push_back(cakes[j].r*cakes[j].h*2);
			}
			sort(foo.begin(), foo.end());
			if (foo.size()>=k-1)
			{
			  int len = foo.size();
			  while(ctr<k)
			  {
			    ans += foo[len-ctr];
			    ctr++;
			  }
			}
			if (ctr == k)
			{
			  ans1 = max(ans, ans1);
		    }
		}
		double finalans = (double) ans1 * M_PI;
		cakes.clear();
		printf("Case #%d: %.9lf\n",l, finalans);
	}
	return 0;
}
