#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<climits>
#include<string>
#include<set>
#include<map>
#include<iostream>
using namespace std;
#define rep(i,n) for(int i=0;i<((int)(n));i++)
#define reg(i,a,b) for(int i=((int)(a));i<=((int)(b));i++)
#define irep(i,n) for(int i=((int)(n))-1;i>=0;i--)
#define ireg(i,a,b) for(int i=((int)(b));i>=((int)(a));i--)
typedef long long int lli;
typedef pair<int,int> mp;
#define fir first
#define sec second
#define IINF INT_MAX
#define LINF LLONG_MAX
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define pque(type) priority_queue<type,vector<type>,greater<type> >
#define memst(a,b) memset(a,b,sizeof(a))
#define iter(v,ite) for(auto ite=(v).begin();ite!=(v).end();ite++)
#define mimunum(v,x) distance((v).begin(),lower_bound((v).begin(),(v).end(),x))


int w,h;
char dat[55][55];

int dx[4]={1,0,-1,0};
int dy[4]={0,-1,0,1};


int p2i(int y,int x,int d){
	return y*w*2+x*2+d%2;
}

int inv(int t){
	return (t%2)?t-1:t+1;
}

int tod(char c,int d){
	if(c=='/'){
		d=inv(d);
	}
	else if(c=='\\'){
		d=3-d;
	}
	return d;
}


vector<int> tr[55][55];

bool upd(int y,int x,int idx,int d,bool cap){
	//printf("search %d %d %d %d %d\n",y,x,idx,d,cap?1:0);
	if(x<0 || x>=w || y<0 || y>=h)return true;
	int c=dat[y][x];
	if(c=='-' || c=='|')return false;
	else if(c=='#')return true;
	else{
		d=tod(c,d);
		int tx=x+dx[d],
			ty=y+dy[d];
		bool b = upd(ty,tx,idx,d,cap);
		if(b && cap){
			tr[y][x].push_back(idx);
			//printf("serve %d %d %d\n",y,x,idx);
		}
		return b;
	}
}


vector<int> vs[5005];
vector<int> rvs[5005];

int gone[5005];
int cmp[5005];

vector<int> kae;
void dfs(int no){
	gone[no]=1;
	rep(i,vs[no].size()){
		int to=vs[no][i];
		if(!gone[to])dfs(to);
	}
	kae.push_back(no);
}

void adde(int p,int q){
	vs[p].push_back(q);
	rvs[q].push_back(p);
	
	//printf("add %d %d\n",p,q);
}

void rdfs(int no,int k){
	gone[no]=true;
	cmp[no]=k;
	rep(i,rvs[no].size()){
		int to=rvs[no][i];
		if(!gone[to])rdfs(to,k);
	}	
}

void scc(){
	memst(gone,0);
	rep(i,5005){
		if(!gone[i])dfs(i);
	}
	memst(gone,0);
	int k = 0;
	irep(i,kae.size()){
		if(!gone[kae[i]])rdfs(kae[i],k++);
	}
}

bool updba(int y,int x,int d,bool cap){
	return upd(y+dy[d],x+dx[d],p2i(y,x,d),d,cap);
}

bool solve(){
	rep(y,h){
		rep(x,w){
			tr[y][x].clear();
		}
	}
	rep(i,5005){
		vs[i].clear();
		rvs[i].clear();
		gone[i]=0;
	}
	
	
	rep(y,h){
		rep(x,w){
			char c = dat[y][x];
			if(c=='|' || c=='-'){
				rep(d,2){
					int p = p2i(y,x,d);
					if(updba(y,x,d,false) && updba(y,x,d+2,false)){
						updba(y,x,d,true);
						updba(y,x,d+2,true);
					}
					else{
						//printf("fald .. %d %d %d\n",y,x,d);
						adde(p,inv(p));
					}
				}
			}
		}
	}
	
	rep(y,h){
		rep(x,w){
			char c = dat[y][x];
			if(c=='.'){
				int ls = tr[y][x].size();
				//printf("%d %d %d\n",y,x,ls);
				if(ls<=0)return false;
				else if(ls==1){
					int p=tr[y][x][0];
					//printf("must .. %d %d %d\n",p/w/2,(p%(w*2))/2,p%2);
					adde(inv(p),p);
				}
				else{
					int p=tr[y][x][0];
					int q=tr[y][x][1];
					//printf("%d %d\n",p,q);
					adde(inv(p),q);
					adde(inv(q),p);
				}
			}
		}
	}
	
	scc();
	
	rep(y,h){
		rep(x,w){
			char c = dat[y][x];
			if(!(c=='|' || c=='-'))continue;
			int p=p2i(y,x,0),
				q=p2i(y,x,1);
			if(cmp[p]==cmp[q])return false;
			else{
				if(cmp[p]<cmp[q])dat[y][x]='|';
				else dat[y][x]='-';
			}
		}
	}
	return true;
}

int main(void){
	int qn;
	scanf("%d",&qn);
	reg(qqq,1,qn){
		scanf("%d%d",&h,&w);
		rep(y,h)scanf("%s",dat[y]);
		bool b=solve();
		printf("Case #%d: %s\n",qqq,b?"POSSIBLE":"IMPOSSIBLE");
		if(b){
			rep(y,h)printf("%s\n",dat[y]);
		}
	}

	return 0;
}




