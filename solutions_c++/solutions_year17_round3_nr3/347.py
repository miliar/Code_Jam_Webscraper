#include<bits/stdc++.h>
using namespace std;
int n, k;
double u, a[55];

void solve (int tc) {
	printf("Case #%d: ",tc);
	scanf("%d%d",&n,&k);
	scanf("%lf",&u);
	for(int i=0;i<n;i++) {
		scanf("%lf",&a[i]);
	}
	sort(a, a+n);
	a[n] = 1.0;
	double ans = 1.0;
	for(int i=0;i<n;i++) {
		if(u <= (i+1)*(a[i+1]-a[i])) {
			for(int j=0;j<=i;j++) {
				ans = ans * (a[i] + u/(i+1));
			}
			for(int j=i+1;j<n;j++) {
				ans = ans * a[j];
			}
			break;
		}
		else u -= (i+1)*(a[i+1]-a[i]);
	}
	printf("%.12f\n",ans);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++) solve(i);
}
