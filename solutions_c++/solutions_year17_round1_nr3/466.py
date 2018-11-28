#include<bits/stdc++.h>
using namespace std;
int Hd,Ad,Hk,Ak,B,D;

int calc(int b,int d){
	int Hd=::Hd,Ad=::Ad,Hk=::Hk,Ak=::Ak;
	int rounds=0;
	for(int i=0;i<d;){
		if(Ak-min(D,Ak)>=Hd){
			Hd=::Hd;
			Hd-=Ak;
		}else{
			Ak-=min(D,Ak);
			Hd-=Ak;
			i++;
		}
		if(++rounds>500||Hd<=0)
			return -1;
	}
	for(int i=0;i<b;){

		if(Ak>=Hd){
			Hd=::Hd;
			Hd-=Ak;
		}else{
			Ad+=B;
			Hd-=Ak;
			i++;
		}
		
		if(++rounds>500||Hd<=0)
			return -1;
	}
	while(1){
		if(Ak<Hd){
			Hk-=Ad;
			if(Hk<=0)return rounds+1;
			Hd-=Ak;
		}else{
			if(Hk<=Ad)
				return rounds+1;
			Hd=::Hd;
			Hd-=Ak;
		}
		if(++rounds>500||Hd<=0)
			return -1;
	}
}

void solve(){
	cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
	const int inf=1e9;
	int ans=inf;
	for(int b=0;;b++){
		for(int d=0;;d++){
			int res=calc(b,d);
//			cerr<<b<<" "<<d<<" "<<res<<endl;
			if(res!=-1){
				ans=min(ans,res);
			}
			if(!D||d*D>Ak)break;
		}
		if(!B||b*B>Hk)
			break;
	}
	if(ans==inf)
		puts("IMPOSSIBLE");
	else cout<<ans<<endl;
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
