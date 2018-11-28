#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
typedef long long ll;
using namespace std;
bool ok(ll n){
	int a[30],p = 0;
	while(n){
		a[p++] = n%10;
		n /= 10;
	//	cout<<n<<endl;
	//	cout<<p<<endl;
	}
	for(int i = 0;i<p-1;i++)
		if(a[i]<a[i+1])
			return 0;
	return 1;
}
int main() {
	//freopen("b.in","r",stdin);
	//freopen("a.out","w",stdout);
	int T;
	long long n;
	scanf("%d",&T);
	for(int cs = 1;cs<=T;cs++){
		scanf("%lld",&n);
		while(!ok(n)){
			n--;
		}
		printf("Case #%d: %lld\n",cs,n);
		//printf("%lld\n",n);
	}
}
