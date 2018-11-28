#include <bits/stdc++.h>
#define ll long long
using namespace std;
vector<string>S;
vector<ll>K;
vector<ll>res;

int main(){
	ll T;cin>>T;
	for(ll a=0;a<T;++a){
		string s;ll k;
		cin>>s>>k;
		S.push_back(s);K.push_back(k);
	}
	for(ll a=0;a<T;++a){
		ll ret=0;
		for(string::iterator it=S[a].begin(),end=S[a].end()-(K[a]-1);it!=end;++it)
		{
			if(*it=='-'){
				++ret;
				for(ll b=0;b<K[a];++b)*(it+b)=*(it+b)=='+'?'-':'+';
			}
		}
		bool p=true;
		for(string::iterator it=S[a].begin(),end=S[a].end();it!=end;++it){
			if(*it=='-'){
				p=false;
				break;
			}
		}
		if(!p)ret=-1;
		res.push_back(ret);
	}
    for(ll a=0;a<T;++a){
		if(res[a]>-1)cout<<"Case #"<<a+1<<": "<<res[a]<<endl;
		else cout<<"Case #"<<a+1<<": IMPOSSIBLE"<<endl;
	}
}
