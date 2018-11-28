//Aleksander Łukasiewicz
#include<bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define ALL(G) (G).begin(),(G).end()

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int INF = 1000000009;
const int MAXN = 1000000;

int D, n;
PII horses[MAXN + 3];

bool Check(double v){
	for(int i=0; i<n; i++){
		if(v*(D - horses[i].x) > (double)D*horses[i].y)
			return false;
	}
	
	return true;
}

int main(){
    int t;
	scanf("%d", &t);
	for(int pp=1; pp<=t; pp++){
		scanf("%d %d", &D, &n);
		for(int i=0; i<n; i++)
			scanf("%d %d", &horses[i].x, &horses[i].y);
		double a = 0.0, b = 1e19;
		for(int i=0; i<150; i++){
			double mid = (a+b)/2.0;
			if(Check(mid))
				a = mid;
			else
				b = mid;
		}
		
		printf("Case #%d: %.10lf\n", pp, a);
	}
    
return 0;
}