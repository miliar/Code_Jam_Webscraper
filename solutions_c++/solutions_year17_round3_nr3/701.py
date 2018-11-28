#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double eps=1e-10;
int T, n, k;
double p, a[100];
bool check(double x){
	double t=p;
	for(int i=0; i<n; i++){
		if(a[i]>x)continue;
		t-=x-a[i];
	}
	if(t>=0)
		return 1;
	return 0;
}
int main() {
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for(int cas=0; cas<T; cas++){
		scanf("%d%d%lf", &n, &k, &p);
		for(int i=0; i<n; i++)
			scanf("%lf", a+i);
		double lo=0, hi=1, ans=0;
		for(int i=0; i<1000; i++){
			double mid=(lo+hi)/2;
			if(check(mid)){
				double t=1;
				lo=mid;
				for(int i=0; i<n; i++){
					if(a[i]<mid)
						t*=mid;
					else t*=a[i];
				}
				ans=max(ans, t);
			}
			else
				hi=mid;
		}
		printf("Case #%d: %.7f\n", cas+1, ans);
	}
	return 0;
}
