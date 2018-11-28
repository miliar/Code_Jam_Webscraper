#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair < double, double > ii;
typedef pair < ll, ii > iii;

const int INF = 0x3f3f3f3f;
const ll LINF = 1LL<<58;

int main(){

	
	int T; cin >> T;
	
	rep(z, 1, T+1){
	
		int D, N; cin >> D >> N; ii aux;
		double ans=0.0;
		
		rep(i, 0, N){
			scanf("%lf %lf", &aux.F, &aux.S);
			double cmp=(D-aux.F)/aux.S;
			ans=max(ans, cmp);
		}
		printf("Case #%d: %.6lf\n", z, D/ans);
		
	}

	return 0;
	
}
