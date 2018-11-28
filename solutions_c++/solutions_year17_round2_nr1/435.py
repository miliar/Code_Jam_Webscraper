
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 1005
#define ones(x) __builtin_popcount(x)

using namespace std;

long long k[N], s[N];
int n;
long long d;

bool puedo(long double v){
	
	bool ok = true;
	long double difD, difV, temp;
	
	for(int i = 0; i < n; i++){
		
		if(v <= s[i])continue;
		difV = abs(v - s[i]);
		
		difD = k[i];
		temp = (difD*1.0)/difV;
		if(v * temp < d)ok = false;
	}
	
	return ok;
}

int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
		
	while(tc--){
		
		scanf("%lld%d", &d, &n);
		
		for(int i = 0; i < n; i++){
			
			scanf("%d%d", &k[i], &s[i]);	
		}
		
		long double lo = 0, hi = 10000000000000000, me;
		//cout2("puedo: ", puedo(50.0));
		
		for(int i = 0; i < 100; i++){
			
			me = (lo + hi)/2.0;
			if(puedo(me))lo = me;
			else hi = me;
		}
		
		printf("Case #%d: %.6Lf\n", caso++, lo);
	}


}

