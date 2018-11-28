#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

struct node{
	ll l,r;
	bool operator <(const node &rhs)const{
		ll m1=(l+r)>>1;ll L1=m1-l,R1=r-m1;
		ll m2=(rhs.l+rhs.r)>>1;
		ll L2=m2-rhs.l,R2=rhs.r-m2;
		if(L1>R1)swap(L1,R1);if(L2>R2)swap(L2,R2);
		if(L1!=L2)return L1<L2;
		if(R1!=R2)return R1<R2;
		return l<rhs.l;
	}
	node(){}
	node(ll a,ll b){l=a;r=b;}
};
priority_queue<node> q;

int main(){
	freopen("C-small-2-attempt1.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int t,cas=1;ll n,k;
	cin>>t;
	while(t--){
		cin>>n>>k;
		while(!q.empty())q.pop();
		q.push(node(1,n));
		ll L,R,m;
		while(k--){
			node tt=q.top();q.pop();
			m=(tt.l+tt.r)>>1;
			L=tt.l;R=tt.r;
			if(tt.l<m)q.push(node(tt.l,m-1));
			if(tt.r>m)q.push(node(m+1,tt.r));
		}
		//cout<<L<<" "<<R<<endl;
		ll LL=max(0LL,m-L);
		ll RR=max(0LL,R-m);
		if(LL>RR)swap(LL,RR);
		printf("Case #%d: %lld %lld\n",cas++,RR,LL);
	}
	return 0;
}