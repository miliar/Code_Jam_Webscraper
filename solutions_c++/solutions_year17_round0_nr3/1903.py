#include<bits/stdc++.h>

#define ll long long

using namespace std;

map<ll,ll> has;

ll n,k;

int cas;

void Work(){
	printf("Case #%d: ",++cas);
	while(k){
		pair<ll,ll> tmp=*--has.end();
		has.erase(--has.end());
		if(tmp.second>=k){
			ll tmp2=tmp.first-1;
			cout<<tmp2/2+(tmp2&1)<<' '<<tmp2/2<<endl;
			return;
		}else{
			k-=tmp.second;
			ll tmp2=tmp.first-1;
			ll tmp3=tmp2/2,tmp4=tmp3+(tmp2&1);
			has[tmp3]+=tmp.second;has[tmp4]+=tmp.second;
		}
	}
}

void Init(){
	cin>>n>>k;
	has.clear();
	has[n]=1;
}

int main(){
	freopen("C3.in","r",stdin);
	freopen("C3.out","w",stdout);
	int T;
	scanf("%d",&T);
	while(T--){
		Init();
		Work();
	}
	return 0;
}
