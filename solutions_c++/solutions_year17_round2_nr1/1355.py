#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

int k[1005];
int s[1005];
bool checkCross(int n, int d, double speed){
	//double eps = 1e-16;
	for(int i=0;i<n;i++){
		double t1 = (d-k[i])*1.0/s[i];
		double t2 = (d)/speed;
		if(t1>=t2)
			return true;
	}
	return false;
}
double solve(int tcase){
	int d,n;
	s(d);s(n);
	REP(i,n){
		s(k[i]);
		s(s[i]);
	}
	double upper = 2e13, lower = 0.5;
	while(((upper-lower)/lower)>=1e-8){
		//printf("%.7lf %.7lf\n", lower, upper);
		double mid = (upper+lower)/2;
		if(checkCross(n,d,mid))
			upper = mid;
		else lower = mid;
	}
	return lower;
}
int main()
{
	int t;
	s(t);
	REP(tt,t){
		printf("Case #%d: %.7lf\n",tt+1,solve(tt+1));
	}
    return 0;
}
