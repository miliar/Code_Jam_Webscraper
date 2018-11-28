#include <bits/stdc++.h>
#define SZ(v) ((int)(v).size())
#define PI 3.141592653589793238

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, ll> pil;

int a[55], b;

int main(){
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++){
		int n, k;
		scanf("%d%d", &n, &k);
		int u, v;
		int sum = 0;
		double ans = 1;
		double div;
		scanf("%d.%d", &u, &v);
		b = 10000*u + v;
		for (int i=0; i<n; i++){
			scanf("%d.%d", &u, &v);
			a[i] = 10000*u+v;
			sum += a[i];
		}
		if (sum + b >= n*10000){
			goto done;
		}
		sort(a,a+n);
		for (int i=0; i<n-1; i++){
			if (b < (i+1)*(a[i+1]-a[i])){
				div = (double) b / (i+1);
				for (int j=0; j<=i; j++){
					ans *= (div + a[j]) / 10000.0;
				}
				for (int j=i+1; j<n; j++){
					ans *= (double) a[j] / 10000.0;
				}
				goto done;
			}
			else {
				b -= (i+1)*(a[i+1] - a[i]);
				for (int j=0; j<=i; j++){
					a[j] = a[i+1];
				}
			}
		}
		div = (double) b / n;
		for (int i=0; i<n; i++){
			ans *= (div + a[i]) / 10000.0;
		}
		done:
		printf("Case #%d: %.9lf\n", t, ans);
	}
	return 0;
}