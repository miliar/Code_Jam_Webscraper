#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
int t;
long long n,m,a,b;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	for(int _=1;_<=t;++_){
		scanf("%lld%lld",&n,&m);
		map<long long,long long> M;
		M.insert({-n,1});
		while(m>M.begin()->y){
			pair<long long,long long> now=*M.begin();
			M.erase(now.x);
			++now.x;
			a=-now.x/2;
			b=-now.x-a;
			M[-a]+=now.y;
			M[-b]+=now.y;
			m-=now.y;
		}
		n=-M.begin()->x-1;
		a=n/2;
		b=n-a;
		if(a<b)swap(a,b);
		printf("Case #%d: %lld %lld\n",_,a,b);
	}
	return 0;
}

