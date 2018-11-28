#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long ll;

const ll inf = 1e18;

ll t,n,d;
double ans=(double)inf;
ll P[10000], S[10000];


int main(){
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> d >> n;
		for(int j = 1; j <= n; j++){
			cin >> P[j] >> S[j];
			double tmp = (double)(d*S[j])/(d-P[j]);
			if(tmp < ans) ans = tmp;
		}
		printf("Case #%d: %.6f\n",i,ans);
		ans = inf;
	}
	return 0;
}
