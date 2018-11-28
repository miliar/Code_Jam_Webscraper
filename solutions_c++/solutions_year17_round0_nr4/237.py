// -*- compile-command: "g++ -g -Wno-return-type -Wall -Wextra -DLOCAL -std=c++11 -D_GLIBCXX_DEBUG d.cpp -od && ./d " -*-
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

struct Matching{
	vc<bool> blocked,visited;
	vc<vc<int>> g;
	vc<int> matched;
	Matching(int n){
		blocked.resize(n);
		visited.resize(n);
		g.resize(n);
		matched=vc<int>(n,-1);
	}
	void edge(int a,int b){
		if(blocked[a]||blocked[b]) return;
		g[a].pb(b);
		g[b].pb(a);
	}
	void clearv(){ fill(visited.begin(),visited.end(),0); }
	void remove(int a,int b){
		assert(~matched[a]&&~matched[b]);
		matched[a]=matched[b]=-1;
	}
	void add(int a,int b){
		assert(!~matched[a]&&!~matched[b]);
		matched[a]=b;
		matched[b]=a;
	}
	int augment(int i){
		if(visited[i]) return 0;
		visited[i]=true;
		for(int j:g[i]){
			if(visited[j]) continue;
			visited[j]=true;
			if(!~matched[j]||augment(matched[j])){
				if(~matched[i])
					remove(i,matched[i]);
				add(i,j);
				return 1;
			}
		}
		return 0;
	}
	void match(){
		int n=sz(g);
		bool done=false;
		while(!done){
			done=true;
			bool improved=true;
			while(improved){
				improved=false;
				for(int i=0;i<n;i++){
					if(!~matched[i]&&augment(i)){
						improved=true;
						done=false;
					}
				}
			}
			clearv();
		}
	}
};

void update(char &a,char b){
	assert(a!='o');
	if(a=='x'&&b=='+') a='o';
	else if(a=='+'&&b=='x') a='o';
	else a=b;
}

void solve(){
	set<pr<int,int>> k;
	int n,m;
	cin>>n>>m;
	vc<vc<char>> orig(n,vc<char>(n,'.'));
	Matching rcM(2*n),dgM(2*(2*n-1));
	f(i,m){
		char x;
		int r,c;
		cin>>x>>r>>c, r--,c--;
		if(x=='x'||x=='o') rcM.blocked[r]=rcM.blocked[n+c]=true;
		if(x=='+'||x=='o') dgM.blocked[r+c]=dgM.blocked[2*n-1+r-c+n-1]=true;
		orig[r][c]=x;
	}
	vc<vc<char>> res=orig;
	f(r,n) f(c,n){
		rcM.edge(r,n+c);
		dgM.edge(r+c,2*n-1+r-c+n-1);
	}
	rcM.match(), dgM.match();
	f(i,n){
		if(!~rcM.matched[i]) continue;
		int r=i,c=rcM.matched[i]-n;
		update(res[r][c],'x');
	}
	f(i,2*n-1){
		if(!~dgM.matched[i]) continue;
		int da=i,db=dgM.matched[i]-(2*n-1)-(n-1);
		int r=(da+db)/2,c=(da-db)/2;
		update(res[r][c],'+');
	}
	int y=0,z=0;
	f(r,n) f(c,n){
		y+=res[r][c]=='x'||res[r][c]=='o';
		y+=res[r][c]=='+'||res[r][c]=='o';
		if(res[r][c]!=orig[r][c]) z++;
	}
	cout<<y<<' '<<z<<'\n';
	f(r,n) f(c,n){
		if(res[r][c]==orig[r][c]) continue;
		cout<<res[r][c]<<' '<<r+1<<' '<<c+1<<'\n';
	}
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
