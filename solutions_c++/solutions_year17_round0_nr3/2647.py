#include<iostream>
#include <queue>
#include<map>
using namespace std;

typedef long long ll;

queue<ll>* Q;


void rec(ll n, ll k, ll& mn,ll& mx){
	Q=new queue<ll>();
	map<ll,ll> m;
	m[n]=1;
	ll p=n;
	ll num=1;
	while(k>num){
		k-=num;
		if(p%2==1)
		{
			p--;
			p/=2;
			num*=2;
			if(!m[p]){
				Q->push(p);
				m[p]=num;
			}else{
				m[p]+=num;
			}
		}else{
			p--;
			ll q=p;
			p=p/2+1;
			if(!m[p]){
				Q->push(p);
				m[p]=num;
			}else{
				m[p]+=num;
			}
			if(q>1){
				p--;
				if(!m[p]){
					Q->push(p);
					m[p]=num;
				}else{
					m[p]+=num;
				}
			}
		}
		p=Q->front();
		Q->pop();
		num=m[p];
	}
	p--;
	mx=mn=p/2;
	if(p%2==1)
		mx++;
	delete Q;
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		ll mn,mx;
		ll n,k;
		cin>>n>>k;
		rec(n,k,mn,mx);
		cout<<"Case #"<<t<<": "<<mx<<" "<<mn<<endl;
	}
	return 0;
}