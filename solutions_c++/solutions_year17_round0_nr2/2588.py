#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

string llts(ll x){
	stringstream ss;
	ss<<x;
	string y;
	ss>>y;
	return y;
}
ll stll(string x){
	stringstream ss(x);
	ll ret;
	ss>>ret;
	return ret;
}


int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	int t;
	cin>>t;
	lop(C,t){
		printf("Case #%d: ",C+1);
		ll n;
		cin>>n;
		string x=llts(n);
		if(n<stll( string( x.size() ,'1'))){
			cout<<string(x.size()-1,'9')<<endl;
			continue;
		}
		for(int i=0;i+1<x.size();i++){
			if(x[i]>x[i+1]){
				int j=i;
				while(j&&x[j-1]==x[j])j--;
				x[j]-=1;
				for(i=j+1;i<x.size();i++)x[i]='9';
			}
		}
		cout<<x<<endl;
	}
}
