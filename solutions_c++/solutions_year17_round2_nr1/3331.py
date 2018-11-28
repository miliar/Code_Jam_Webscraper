#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<map>
#include<cstring>
#include<set>
#include<limits.h>
#include<iomanip>
using namespace std;
#define uii long long int
#define M(a,b) (a>b ? a : b)
#define m(a,b) (a>b ? b : a)
#define it(a)  ::iterator a
#define slld(a) uii a;scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define plld(a) printf("%lld",a)
#define MAX 10000
#define INF LLONG_MAX
#define MOD 1000000007
#define powOf2(a) !(a&a-1)
#define mod(a) (a>0 ? a : (-1*a))
#define tc(a) uii a; for(scanf("%lld",&a);a--;)
#define swap(a,b) a = a^b; b = a^b;a = a^b;
int main(){
	uii T,X=0;
	cin>>T;
	while(X!=T){
	X++;
	double D;cin>>D;slld(N);
	double m = 0;
	for(uii i = 0;i<N;i++){
		double d,s;
		cin>>d>>s;
		double temp = (D-d)/s;
		m = max(m,temp);		
	}
	cout<<"Case #"<<X<<": ";
	double ans;
	if(m!=0) ans = (D)/m;
	else ans = D;
	printf("%lf\n",ans);
	
		
		
		
		
	}     
   




	return 0;
}


