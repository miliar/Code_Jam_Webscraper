#include<bits/stdc++.h>
using namespace std;
const int maxn=55;
char mp[maxn][maxn];
int n,m;
int id(int x,int y){
	return (x-1)*m+y;
}

int stamp, comps, top;
vector<int>edge[int(1e5+5)];
int dfn[int(1e5+5)], low[int(1e5+5)], comp[int(1e5+5)], stk[int(1e5+5)];
int ans[int(1e5+5)];
void add(int x, int a, int y, int b) {
//	cerr<<x<<" "<<a<<" "<<y<<" "<<b<<endl;
    edge[x << 1 | a].push_back(y << 1 | b);
}

void tarjan(int x) {
    dfn[x] = low[x] = ++stamp;
    stk[top++] = x;
    for (int i = 0; i < (int)edge[x].size(); ++i) {
        int y = edge[x][i];
        if (!dfn[y]) {
            tarjan(y);
            low[x] = std::min(low[x], low[y]);
        } else if (!comp[y]) {
            low[x] = std::min(low[x], dfn[y]);
        }
    }
    if (low[x] == dfn[x]) {
        comps++;
        do {
            int y = stk[--top];
            comp[y] = comps;
        } while (stk[top] != x);
    }
}

bool twosat(int n) {
    int counter = n + n + 1;
    stamp = top = comps = 0;
    std::fill(dfn, dfn + counter, 0);
    std::fill(comp, comp + counter, 0);
    for (int i = 0; i < counter; ++i) {
        if (!dfn[i]) {
            tarjan(i);
        }
    }
    for (int i = 0; i < n; ++i) {
        if (comp[i << 1] == comp[i << 1 | 1]) {
            return false;
        }
        ans[i] = (comp[i << 1 | 1] < comp[i << 1]);
    }
    return true;
}

// | 0 , - 1

vector<pair<int,int> >bel[maxn][maxn];
bool check(int ty,int x,int y){
	int ind=id(x,y);
	if(ty==0){
		for(int i=x+1;i<=n;i++){
			if(mp[i][y]=='-'||mp[i][y]=='|')return false;
			if(mp[i][y]=='#')break;
		}
		for(int i=x-1;i>=1;i--){
			if(mp[i][y]=='-'||mp[i][y]=='|')return false;
			if(mp[i][y]=='#')break;
		}
	}else{
		for(int i=y+1;i<=m;i++){
			if(mp[x][i]=='-'||mp[x][i]=='|')return false;
			if(mp[x][i]=='#')break;
		}
		for(int i=y-1;i>=1;i--){
			if(mp[x][i]=='-'||mp[x][i]=='|')return false;
			if(mp[x][i]=='#')break;
		}
	}
	return true;
}
bool push(int ty,int x,int y){
	int ind=id(x,y);
	if(ty==0){
		for(int i=x+1;i<=n;i++){
			if(mp[i][y]=='-'||mp[i][y]=='|')return false;
			if(mp[i][y]=='#')break;
			bel[i][y].push_back({ind,ty});
		}
		for(int i=x-1;i>=1;i--){
			if(mp[i][y]=='-'||mp[i][y]=='|')return false;
			if(mp[i][y]=='#')break;
			bel[i][y].push_back({ind,ty});
		}
	}else{
		for(int i=y+1;i<=m;i++){
			if(mp[x][i]=='-'||mp[x][i]=='|')return false;
			if(mp[x][i]=='#')break;
			bel[x][i].push_back({ind,ty});
		}
		for(int i=y-1;i>=1;i--){
			if(mp[x][i]=='-'||mp[x][i]=='|')return false;
			if(mp[x][i]=='#')break;
			bel[x][i].push_back({ind,ty});
		}
	}
	return true;
}

int can[maxn][maxn];

bool checker(){
	static int cnt[maxn][maxn];
	memset(cnt,0,sizeof cnt);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++){
			int x=i,y=j;
			if(mp[i][j]=='|'){
				for(int k=x+1;k<=n;k++){
					if(mp[k][y]=='-'||mp[k][y]=='|')return false;
					if(mp[k][y]=='#')break;
					cnt[k][y]++;
				}
				for(int k=x-1;k>=1;k--){
					if(mp[k][y]=='-'||mp[k][y]=='|')return false;
					if(mp[k][y]=='#')break;
					cnt[k][y]++;
				}
			}
			if(mp[i][j]=='-'){
				for(int k=y+1;k<=m;k++){
					if(mp[x][k]=='-'||mp[x][k]=='|')return false;
					if(mp[x][k]=='#')break;
					cnt[x][k]++;
				}
				for(int k=y-1;k>=1;k--){
					if(mp[x][k]=='-'||mp[x][k]=='|')return false;
					if(mp[x][k]=='#')break;
					cnt[x][k]++;
				}
			}

		}
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)if(mp[i][j]=='.')
			if(!cnt[i][j])return false;
	return true;
}

void solve(){
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++){
		scanf("%s",mp[i]+1);
	}

	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			bel[i][j].clear();
	
	for(int i=0;i<=n*m;i++)
		edge[i].clear();
	#define cls(a) memset(a,0,sizeof a)
	cls(dfn);
	cls(low);
	cls(comp);
	cls(stk);
	cls(can);
	cls(ans);
	stamp=comps=top=0;
	
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)if(mp[i][j]=='|'||mp[i][j]=='-'){
			if(check(0,i,j)){
				push(0,i,j);
				can[i][j]|=1;
			}
			if(check(1,i,j)){
				push(1,i,j);
				can[i][j]|=2;
			}
			
			if(!can[i][j]){
				puts("IMPOSSIBLE");
				return ;
			}
			if(can[i][j]==1){
				add(id(i,j),1,id(i,j),0);
			}
			if(can[i][j]==2){
				add(id(i,j),0,id(i,j),1);
			}
		}
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)if(mp[i][j]=='.'){
			if(bel[i][j].empty()){
				puts("IMPOSSIBLE");
				return ;
			}
			assert(bel[i][j].size()<=2);



			if(bel[i][j].size()==1){
				add(bel[i][j][0].first,!bel[i][j][0].second,bel[i][j][0].first,bel[i][j][0].second);
			}else{
				add(bel[i][j][0].first,!bel[i][j][0].second,bel[i][j][1].first,bel[i][j][1].second);
				add(bel[i][j][1].first,!bel[i][j][1].second,bel[i][j][0].first,bel[i][j][0].second);
			}
		}
	if(!twosat(n*m+1))	
		puts("IMPOSSIBLE");
	else{
		puts("POSSIBLE");
		for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)if(mp[i][j]=='|'||mp[i][j]=='-'){
			mp[i][j]=ans[id(i,j)]?'-':'|';
		}
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++){
				putchar(mp[i][j]);
			}
			puts("");
		}
		assert(checker());
	}
}

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
