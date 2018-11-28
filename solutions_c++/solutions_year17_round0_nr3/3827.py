#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;
set<pair<pair<ll,pair<ll,ll> >,ll> > s;
map<ll,ll > m;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int qq=1;qq<=t;qq++){
		m.clear();
		ll n,k;
		cin>>n>>k;
		printf("Case #%d: ",qq);
		s.insert(make_pair(make_pair(n,make_pair(1,n)),1));
		m[n]++;
		ll mn=0,mx=0;
		pair<pair<ll,pair<ll,ll> >,ll> p,q;
		while(k>0){
			mn=(m.rbegin()->first-1);
			
			mn/=2;
			pll p1= *m.rbegin();
			//cout<<"~ "<<p1.first<<" "<<p1.second<<endl;
			m[p1.first]-=p1.second;
			m.erase(p1.first);
			ll d1=(p1.first-1)/2;
			m[d1]+=p1.second;
			d1=(p1.first)/2;
			mx=d1;
			m[d1]+=p1.second;
			k-=p1.second;
			/*
			p=*s.begin();
			q=*s.rbegin();
			mn=(p.first.first-1)/2;
			s.erase(q);
			mx=(q.first.first)/2;
			ll l=q.first.second.first;
			ll r=q.first.second.second;
			ll m=l+mx+1;
			ll d1=m-l;
			ll no=q.second;
			k-=no;
			if(mx-l==r-mx)
				s.insert(make_pair(make_pair(d1,make_pair(l,m-1)),(2*no)));
			else{
				s.insert(make_pair(make_pair(d1,make_pair(l,m-1)),(no)));
				s.insert(make_pair(make_pair((r-m),make_pair(m+1,r)),(no)));
			}*/
		}
		cout<<mx<<" "<<mn<<endl;
	}
	return 0;
}
