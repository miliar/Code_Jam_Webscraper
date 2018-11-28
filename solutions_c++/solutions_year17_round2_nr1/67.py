#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 2000000000.0
#define M 1000000007ll
#define INFLL 1000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)
int tc;
int n;
double d,k[1005],s[1005];
int main() {
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		scanf("%lf%d",&d,&n);
		double ans=0.0;
		for (int i=0;i<n;i++) {
			scanf("%lf%lf",&k[i],&s[i]);
			if (i) ans=min(ans,d*s[i]/(d-k[i]));
			else ans=d*s[i]/(d-k[i]);
		}
		printf("Case #%d: %.8lf\n",kk,ans);
	}
}