#include "bits/stdc++.h"
#define MAXN 100009
#define INF 1000000007
#define mp(x,y) make_pair(x,y)
#define all(v) v.begin(),v.end()
#define pb(x) push_back(x)
#define wr cout<<"----------------"<<endl;
#define ppb() pop_back()
#define tr(ii,c) for(typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define ff first
#define ss second
#define my_little_dodge 46
#define eps (1e-9)
using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
template<class T>bool umin(T& a,T b){if(a>b){a=b;return 1;}return 0;}
template<class T>bool umax(T& a,T b){if(a<b){a=b;return 1;}return 0;}
int n,k;
double arr[MAXN];
double ok(double x){
	double res=0;
	for(int i=1;i<=n;i++)
		res+=max(0.0,x-arr[i]);
	return res;	
}
void solve(int tt,double x){
	double ans=1;
	for(int i=1;i<=n;i++){
		if(arr[i]<x)
			arr[i]=x;
		ans*=arr[i];	
	}
	printf("Case #%d: %.10lf\n",tt,ans);
}
int main(){
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
		scanf("%d%d",&n,&k);
		double u;
		scanf("%lf",&u);
		for(int i=1;i<=n;i++)
			scanf("%lf",&arr[i]);
		double st=0,en=1.0;
		while(st+eps<en){
			double mid=(st+en)/2.0;
			if(ok(mid)<=u)
				st=mid;
			else
				en=mid;
		}
		if(ok(en)<=u)
			solve(test,en);
		else
			solve(test,st);
	}
	return 0;
}
