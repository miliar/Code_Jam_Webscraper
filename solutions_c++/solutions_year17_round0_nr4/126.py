#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <functional>
#include <climits>
#include <list>
#include <ctime>
#include <complex>

#define F1(x,y,z) for(int x=(y);x<(z);x++)
#define F2(x,y,z) for(int x=(y);x<=(z);x++)
#define F3(x,y,z) for(int x=(y);x>(z);x--)
#define F4(x,y,z) for(int x=(y);x>=(z);x--)
#define mp make_pair
#define pb push_back
#define LL long long
#define co complex<double>
#define fi first
#define se second

#define MAX 100005
#define AMAX 1025*1005
#define MOD 1000000007

#define f(c,d) ((1<<(c))*(d))

using namespace std;

int t,n,m,d[605],ans,cnt,ss,tt,nn,ta,tb,tc,td;
char y[5],x[105][105];
bool z[105][105],o[605];
vector<int> ed[605],to,l;
queue<int> q;

bool bfs(){
    F1(a,0,nn)d[a]=-1;
    d[ss]=0;
    q=queue<int>();
    q.push(ss);
    while(!q.empty()){
		F1(a,0,ed[q.front()].size())if(d[to[ed[q.front()][a]]]==-1&&l[ed[q.front()][a]]){
			d[to[ed[q.front()][a]]]=d[q.front()]+1;
			if(to[ed[q.front()][a]]==tt)return 1;
			q.push(to[ed[q.front()][a]]);
		}
        q.pop();
    }
    return 0;
}

int dfs(int a,int b){
    if(a==tt)return b;
    int re=0,tx;
	F1(c,0,ed[a].size())if(d[to[ed[a][c]]]==d[a]+1&&l[ed[a][c]]){
		tx=dfs(to[ed[a][c]],min(b,l[ed[a][c]]));
		b-=tx;
		l[ed[a][c]]-=tx;
		l[ed[a][c]^1]+=tx;
		re+=tx;
		if(!b)return re;
	}
    return re;
}

void add(int a,int b,int c=1){
	ed[a].pb(to.size());
	to.pb(b);
	l.pb(c);
	ed[b].pb(to.size());
	to.pb(a);
	l.pb(0);
}


int main(){
	scanf("%d",&t);
	F2(a,1,t){
		ans=cnt=0;
		to.clear();
		l.clear();
		scanf("%d%d",&n,&m);
		ss=0,tt=n*2+1,nn=n*6;
		F2(b,1,n)F2(c,1,n)x[b][c]=0,z[b][c]=0;
		F1(b,0,nn)ed[b].clear(),o[b]=1;
		F2(b,1,n)F2(c,1,n)add(b,n+c),add(n*2+(b+c),n*5+(b-c));
		while(m--){
			scanf("%s%d%d",y,&ta,&tb);
			if(y[0]=='+')x[ta][tb]=1;
			else if(y[0]=='x')x[ta][tb]=2;
			else x[ta][tb]=3;
			if(x[ta][tb]&1)ans++,o[n*2+(ta+tb)]=o[n*5+(ta-tb)]=0;
			if(x[ta][tb]&2)ans++,o[ta]=o[n+tb]=0;
		}
		F2(b,1,n)if(o[b])add(ss,b);
		F2(b,1,n)if(o[n+b])add(n+b,tt);
		F2(b,2,n*2)if(o[n*2+b])add(ss,n*2+b);
		F2(b,1-n,n-1)if(o[n*5+b])add(n*5+b,tt);
		while(bfs())ans+=dfs(ss,INT_MAX);
		F2(b,1,n)F1(c,0,ed[b].size())if(!l[ed[b][c]]){
			ta=to[ed[b][c]]-n;
			if(1<=ta&&ta<=n){
				x[b][ta]|=2;
				if(!z[b][ta])z[b][ta]=1,cnt++;
			}
		}
		F2(b,2,n*2){
			ta=n*2+b;
			F1(c,0,ed[ta].size())if(!l[ed[ta][c]]){
				tb=to[ed[ta][c]]-n*5;
				if(1-n<=tb&&tb<=n-1){
					tc=(b+tb)/2;
					td=(b-tb)/2;
					x[tc][td]|=1;
					if(!z[tc][td])z[tc][td]=1,cnt++;
				}
			}
		}
		printf("Case #%d: %d %d\n",a,ans,cnt);
		F2(b,1,n)F2(c,1,n)if(z[b][c]){
			if(x[b][c]==1)printf("+ %d %d\n",b,c);
			else if(x[b][c]==2)printf("x %d %d\n",b,c);
			else printf("o %d %d\n",b,c);
		}
	}
	return 0;
}
