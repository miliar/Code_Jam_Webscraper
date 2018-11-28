#include <bits/stdc++.h>
using namespace std;
#define R(i,x,y) for(long long (i)=(x);(i)<(y);(i)++)
long long ar[100005];
long long  p(long long a, long long  n){
	if(n==0) return 1;
	if(n%2==1) return a*p(a,n-1);
	if(n%2==0) {
		long long  x=p(a,n/2);
		return x*x;
	}
}

inline void make(long long  ta, long long  ar[]){
	long long  pos=ta;
	R(i,0,ta-1){
		if(ar[ta-1-i]>ar[ta-i-2]){
			ar[ta-1-i]--; pos=i+1;
			break;
		}
	}
	for(int i=pos;i<ta;i++){
		ar[ta-1-i]=9;
	}
}
long long  ok(long long  ta, long long  ar[]){
	R(i,0,ta){
		if(ar[ta-1-i]>ar[ta-i-2]) return 1;
	}
	return 2;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("l.out","w",stdout);
   ios_base::sync_with_stdio(0);cin.tie(0);
	long long  t; cin>>t;
	R(asd,0,t){
		long long  x; cin>>x; long long  val=x,ta;
		R(i,0,20){
			ar[i]=val%10;
			val=(val-ar[i])/10;
			if(val==0) { ta=i;break;}
		} ta++;
		for(int i=0;i<20;i++){
			make(ta,ar);

			if(ok(ta,ar)==2) break;
		}
		long long  ans=0;
			R(i,0,ta) ans+=ar[i]*p(10,i);
			cout<<"Case #"<<asd+1<<":"<<" "<<ans<<endl;
	memset(ar,0,sizeof(ar));

	}
	return 0;
}
