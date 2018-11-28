#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define endl "\n"
#define PI acos(-1)
typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,int> ii;
typedef complex<double> base;

int t, n;
double d, k, s;

int main(void){
	scanf("%d", &t);

	for(int caso = 1; caso <= t; caso++){
		scanf("%lf%d", &d, &n);
		double maxtemp = -1;
		For(i,0,n){
			scanf("%lf%lf", &k, &s);
			maxtemp = max(maxtemp, (d-k)/s);
		}

		double speed = d/maxtemp;
		printf("Case #%d: %lf\n", caso, speed);
	}

	return 0;
}