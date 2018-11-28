#include <bits/stdc++.h>
#define _USE_MATH_DEFINES
#include <cmath> 
using namespace std;

typedef long long LL;
const long double PI =  3.14159265358979323846L;
// const double PI = acos(-1);

int n,k;

struct Cake{
	LL r, h;
	bool operator <(const Cake &that)const{
		return r<that.r;
	}
	LL edge(){
		return LL(r)*2*LL(h);
	}
	LL top(){
		return LL(r)*LL(r);
	}
};

vector<Cake> cakes;

void input(){
	scanf("%d%d",&n,&k);
	cakes.resize(n);
	for(int i=0; i<n; i++)
		scanf("%lld%lld",&cakes[i].r,&cakes[i].h);
}

void solve(int kase){
	printf("Case #%d: ",kase+1);

	sort(cakes.begin(),cakes.end());

	static LL dp[1111][1111];
	memset(dp,0,sizeof dp);
	for(int i=0; i<=n; i++) dp[0][i]=0;

	for(int i=0; i<n; i++){
		Cake &cake=cakes[i];
		LL *dppre=dp[i];
		LL *dpnow=dp[i+1];

		dpnow[0]=0;
		for(int j=1; j<=k; j++){
			dpnow[j]=max(dppre[j-1]+cake.edge(), dppre[j]);
		}
	}

	LL ans=0;
	for(int i=k-1; i<n; i++){
		Cake &cake=cakes[i];
		LL *dpnow=dp[i];
		ans=max(ans, dpnow[k-1]+cake.edge()+cake.top());
		// printf("%lld + %lld = %d\n",dpnow[k],cake.top(), dpnow[k]+cake.top());
	}
	// printf("%.8f\n",ans*PI);
	printf("%.9Lf\n",((long double)ans)*PI);
	// printf("ans %lld\n",ans);
	// for(int i=0; i<n; i++)
	// 	printf("Cake %d: %f %f\n", i+1, cakes[i].edge(), cakes[i].top());
}

int main(){
	fprintf(stderr, "PI=%.9Lf\n",PI);
	// fprintf(stderr, "M_PI=%.9f\n",M_PI);
	int zz;
	scanf("%d",&zz);
	for(int i=0; i<zz; i++){
		input();
		solve(i);
	}
}
