// -*- compile-command: "g++ -g -Wno-return-type -Wall -Wextra -DLOCAL -std=c++11 -D_GLIBCXX_DEBUG a.cpp -oa && ./a " -*-
#include <bits/stdc++.h>
using namespace std;
using LL=long long;
#define int LL
#define vc vector
#define pb push_back
#define pr pair
#define fi first
#define se second
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define f(i,n) for(int i=0;i<(n);i++)
#define fv(i,v) f(i,sz(v))

void solve(){
	int r,c;
	cin>>r>>c;
	vc<string> cake(r);
	f(i,r) cin>>cake[i];
	int tot[256]={0};
	f(i,r){
		f(j,c){
			tot[(int)cake[i][j]]++;
		}
	}
	for(char k='A';k<='Z';k++){
		if(!tot[(int)k]) continue;
		bool done=false;
		for(int a=0;a<r&&!done;a++){
			for(int b=r-1;b>=a&&!done;b--){
				for(int x=0;x<c&&!done;x++){
					for(int y=c-1;y>=x&&!done;y--){
						int cnt=0;
						for(int i=a;i<=b&&cnt!=-1;i++){
							for(int j=x;j<=y&&cnt!=-1;j++){
								if(cake[i][j]==k){
									cnt++;
								}else if(cake[i][j]!='?'){
									cnt=-1;
								}
							}
						}
						if(cnt==tot[(int)k]){
							for(int i=a;i<=b;i++){
								for(int j=x;j<=y;j++){
									cake[i][j]=k;
								}
							}
							done=true;
						}
					}
				}
			}
		}
	}
	cout<<'\n';
	f(i,r) cout<<cake[i]<<'\n';
}

main(){
	ios::sync_with_stdio(0),cin.tie(0);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		solve();
	}
}
