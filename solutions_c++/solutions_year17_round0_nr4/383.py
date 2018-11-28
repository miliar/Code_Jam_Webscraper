
// In the name of God
#include <bits/stdc++.h>

using namespace std;
#define Size(x) ((int)(x).size())
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int>pii;
const int INF = 1e9 + 10;
const int MN = 1e2 + 5;

int n , m;
pii res[MN];
short inp[MN][MN] , ans[MN][MN];
bool mk[MN] , mk2[MN] , adj[MN<<1][MN<<1] , seen[MN<<1] , removed_r[MN<<1] , removed_c[MN<<1];
int match[MN<<1] , M[MN<<1];
int rs , sz_M;

void make_graph()
{
	for(int i=0;i<n;++i)
		for(int j=0;j<n;++j){
			int R = i+j;
			int C = i-j+n-1;
			if(inp[i][j]&2) removed_r[R] = removed_c[C] = true , ++sz_M;	
		}
	for(int i=0;i<n;++i)
		for(int j=0;j<n;++j){
			int R = i+j;
			int C = i-j+n-1;
			if(!removed_r[R] && !removed_c[C]) adj[R][C] = true;
		}
}

bool dfs(int s)
{
	seen[s] = true;
	for(int i=0;i<2*n-1;++i) if(adj[s][i]){
		if(match[i] == -1 || (!seen[match[i]] && dfs(match[i]))){
			match[i] = s , M[s] = i;
			return true;
		}
	}
	return false;
}

void func(int Sum,int Sub)
{
	Sub -= n-1;
	int r = (Sum + Sub)/2 , c = (Sum - Sub)/2;
	ans[r][c] |= 2;
}

int main()
{
	ios_base :: sync_with_stdio(false) ,cin.tie(0) , cout.tie(0);
	int T;scanf("%d\n" , &T);int cnt = 0;
	while(T--){
		++cnt;
		
		scanf("%d %d\n" , &n , &m);
		memset(inp , 0 , sizeof inp) , memset(ans , 0 , sizeof ans);
		while(m--){
			char ch;int r,c;
			scanf("%c %d %d\n" , &ch , &r , &c);
			--r,--c;
			if(ch == 'o') inp[r][c] = 3;
			else if(ch == 'x') inp[r][c] = 1;
			else inp[r][c] = 2;
			ans[r][c] = inp[r][c];
		}
		printf("Case #%d: " , cnt);
		// yekka ghotr parakande and
		memset(mk , 0 , sizeof mk) , memset(mk2 , 0 , sizeof mk2);
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j){
				if(inp[i][j]&1){
					mk[i] = true;
					mk2[j] = true;
				}
			}
		int pnt = 0;
		for(int i=0;i<n;++i) if(!mk[i]){
			while(pnt < n && mk2[pnt]) ++pnt;
			ans[i][pnt] |= 1;
			mk2[pnt] = true;
		}
		memset(adj , 0 , sizeof adj) , memset(removed_r , 0 , sizeof removed_r) , memset(removed_c , 0 , sizeof removed_c);
		sz_M = 0;
		make_graph();
	
		memset(M , -1 , sizeof M) , memset(match , -1 , sizeof match);
		bool finished;
		do{
			finished = true;
			memset(seen , 0 , sizeof seen);
			for(int i=0;i<2*n-1;++i)
				if(M[i] == -1 && !seen[i] && dfs(i)) finished = false , ++sz_M;
		}while(!finished);
		for(int i=0;i<2*n-1;++i){
			if(~match[i]) func(match[i] , i);
		}

		rs = 0;
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j) if(ans[i][j] != inp[i][j]) res[rs++] = {i,j};
		printf("%d %d\n" , n+sz_M , rs);
		for(int i=0;i<rs;++i){
			int r = res[i].first , c = res[i].second;
			if(ans[r][c] == 3) printf("o ");
			else if(ans[r][c] == 2) printf("+ ");
			else printf("x ");
			printf("%d %d\n" , r+1 , c+1);
		}
	}
	return 0;
}

