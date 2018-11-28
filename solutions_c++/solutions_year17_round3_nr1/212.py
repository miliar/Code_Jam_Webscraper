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

int r[1005];
int h[1005];
pair<double,int> prod[1005];
const double PI = 3.14159265358979323846;
double solve(){
	int n,k;
	s(n);s(k);
	REP(i,n){
		s(r[i]);
		s(h[i]);
		prod[i] = make_pair(r[i]*1.0*h[i],i);
	}
	sort(prod, prod+n);
	double maxi = 0;
	for(int i=n-1;i>=0;i--){
		int cind = prod[i].second;
		double csum = PI*r[cind]*1.0*r[cind];
		for(int j=n-1;j>=(n-k+1);j--)
			csum += 2*PI*prod[j].first;
		if(i>=(n-k+1))
			csum += 2*PI*prod[n-k].first;
		else 
			csum += 2*PI*prod[i].first;
		//cout<<"With base of "<<cind<<" ans = "<<csum<<endl;
		maxi = max(maxi, csum);
	}
	return maxi;
}

int main()
{
	int t;
	s(t);
	REP(tt,t){
		printf("Case #%d: ",tt+1);
		printf("%.15lf",solve());
		printf("\n");
	}
    return 0;
}
