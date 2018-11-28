#include<bits/stdc++.h>
using namespace std;
const int N = 1005;
const double PI = 3.14159265358;
long long	 r[N],h[N];
priority_queue<double> q;
int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int _t = 1;_t <= T;_t++) {
		int n,k;
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;i++) {
			scanf("%lld%lld",r+i,h+i);
		}
		double ans = 0;
		for (int i=0;i<n;i++) {
			double tmp = r[i] * r[i] * PI + 2 * PI * r[i] * h[i];
			for (int j=0;j<n;j++) {
				if (j == i) continue;
				if (r[j] <= r[i]) q.push(2 * PI * r[j] * h[j]);
				//cout<<-2 * PI * r[j] * h[j]<<endl;
			}	
			int tot = 1;
			while (!q.empty()) {
				if (tot < k) {
					tmp += q.top();
					tot++;
				}
				q.pop();
			}
			if (tmp > ans) ans = tmp;
		}
		printf("Case #%d: %.7lf\n",_t,ans);
	}
}
