#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

int t;
string x;
int arr[2010],k;

int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	cin>>t;
	lop(C,t){
		cin>>x>>k;
		int n=x.size();
		memset(arr,0,sizeof arr);
		int xr=0,ok=1,cnt=0;
		lop(i,n){
			xr^=arr[i];
			if( (xr&&x[i]=='+' ) || (!xr&&x[i]=='-')){
				if(n-i<k)ok=0;
				xr^=1;
				arr[i+k]=1;
				cnt++;
			}
		}
		printf("Case #%d: ",C+1);
		if(ok)printf("%d\n",cnt);
		else puts("Impossible");
	}

}
