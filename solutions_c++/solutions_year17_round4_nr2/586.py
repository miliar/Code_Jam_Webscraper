#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define PB push_back
#define MP make_pair

const int INF = 0x3f3f3f3f;
const int mod = 1e9 + 7;
const double eps = 1e-8;
const int maxn = 1e5+5;
const int maxm = 3e6+5;

int b[2][2];
int t[2][maxn];

int head[maxn],point[maxm],nxt[maxm],size;
int match[maxn],vis[maxn];

void init(){
    memset(head,-1,sizeof(head));
    size=0;
    memset(match,-1,sizeof(match));
}

void add(int a,int b){
    point[size]=b;
    nxt[size]=head[a];
    head[a]=size++;
}

int dfs(int s){
    for(int i=head[s];~i;i=nxt[i]){
        int j=point[i];
        if(!vis[j]){
            vis[j]=1;
            if(match[j]==-1||dfs(match[j])){
                match[j]=s;
                return 1;
            }
        }
    }
    return 0;
}


int main(){
	int T;
	scanf("%d",&T);
	for(int q=1;q<=T;++q){
		int n,m,c;
		scanf("%d%d%d",&n,&c,&m);
		if(c==2){
			init();
			b[0][0]=b[0][1]=b[1][0]=b[1][1]=0;
			int cnt0=0,cnt1=0;
			for(int i=1;i<=m;++i){
				int x,y;
				scanf("%d%d",&x,&y);
				y--;
				if(x==1)b[y][0]++;
				else{
					b[y][1]++;
					if(y==0)t[0][++cnt0]=x;
					else t[1][++cnt1]=x;
				}
			}
			int ans=0;
			int tmp;
			tmp=min(b[0][0],b[1][1]);
			ans+=tmp;
			b[0][0]-=tmp;
			b[1][1]-=tmp;
			ans+=b[0][0];
			tmp=min(b[1][0],b[0][1]);
			ans+=tmp;
			b[1][0]-=tmp;
			b[0][1]-=tmp;
			ans+=b[1][0];
			tmp=max(b[0][1],b[1][1]);
			ans+=tmp;
			tmp=min(b[0][1],b[1][1]);
			for(int i=1;i<=cnt0;++i){
				for(int j=1;j<=cnt1;++j){
					if(t[0][i]!=t[1][j]){
						add(i,cnt0+j);
						add(cnt0+j,i);
					}
				}
			}
			int num=0;
			for(int i=1;i<=cnt0;++i){
				memset(vis,0,sizeof(vis));
				if(dfs(i)==1)num++;
			}
			int ans2=0;
			if(num<tmp)ans2=tmp-num;
			printf("Case #%d: %d %d\n",q,ans,ans2);
		}
	}
	return 0;
}
