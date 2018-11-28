/*
Bipartite Maximum Matching
    Augment Path Algorithm
        O(VE)
*/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>

#define Max 255

using namespace std;

vector<int> e[Max];
vector<int> x;
bool vis[Max];
int match[Max];


bool dfs(int now)
{
    if(vis[now])
        return 0;

    vis[now] = 1;

    for(int i=0;i<(int)e[now].size();i++)
    {
        int b = e[now][i];
        if(match[b] == -1 || dfs(match[b]))
        {
            match[b] = now;
            return 1;
        }
    }
    return 0;
}

int augment_path()
{
    memset(match, -1, sizeof(match));
    int ans = 0;
    for(int i=0;i<(int)x.size();i++)
    {
        memset(vis, 0, sizeof(vis));
        if(dfs(x[i]))
            ans++;
    }
    return ans;
}

int T, N, M;

bool tablex[Max][Max]; // x 號的: 城堡問題 
bool tablep[Max][Max]; // + 號的: 主教問題 

// 對照答案用 
char table_old[Max][Max];
char table_new[Max][Max];


// 城堡用 
bool rdie[Max], cdie[Max]; 
std::vector<int> ralive, calive;

// 主教用 
bool xdie[Max], ydie[Max];

void init() {
	memset(tablex, 0, sizeof(tablex));
	memset(tablep, 0, sizeof(tablep));
	memset(rdie, 0, sizeof(rdie));
	memset(cdie, 0, sizeof(cdie));
	ralive = std::vector<int>();
	calive = std::vector<int>();
	memset(xdie, 0, sizeof(xdie));
	memset(ydie, 0, sizeof(ydie));
	x = std::vector<int>();
	for(int i=0; i<N+N-1; i++) {
		x.push_back(i);
		e[i] = std::vector<int>();
	}
	for(int r=1; r<=N; r++) {
		for(int c=1; c<=N; c++) {
			table_old[r][c] = '.';
		}
	}
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		int M;
		scanf("%d%d", &N, &M);
		// init something
		init();
		// input
		for(int mi=0; mi<M; mi++) {
			char s[2];
			int r, c;
			// o 可以當作 x 配上 + 
			scanf("%s%d%d", s, &r, &c);
			table_old[r][c] = s[0];
			if(s[0] == 'o') {
				tablex[r][c] = true;
				tablep[r][c] = true;
			}
			else if(s[0] == 'x') {
				tablex[r][c] = true;
			}
			else if(s[0] == '+') {
				tablep[r][c] = true;
			}
			// x: 主教問題
			if(tablex[r][c]) {
				rdie[r] = true;
				cdie[c] = true;
			}
			// +: 城堡問題 
			if(tablep[r][c]) {
				int X, Y;
				X = r+c-2;   // 2~N+N    平移到 0~N+N-2 
				Y = r-c+N-1; // -N+1~N-1 平移到 0~N+N-2
				xdie[X] = true;
				ydie[Y] = true;
				//printf("die x=%d y=%d\n", X, Y);
			}
		}
		// 城堡問題: 總之亂湊
		for(int i=1; i<=N; i++) {
			if(!rdie[i]) {
				ralive.push_back(i);
			}
			if(!cdie[i]) {
				calive.push_back(i);
			}
		}
		for(int i=0; i<(int)ralive.size(); i++) {
			tablex[ralive[i]][calive[i]] = true;
		}
		/////////////////////////
		/*
		for(int i=1; i<=N; i++)
			for(int j=1; j<=N; j++)
				printf("%c%c", tablex[i][j]?'x':'.', j==N?'\n':' ');
		//*/
		/////////////////////////
		// 主教問題: 二分圖匹配
		for(int r=1; r<=N; r++) {
			for(int c=1; c<=N; c++) {
				int X, Y;
				X = r+c-2;
				Y = r-c+N-1;
				if(!xdie[X] && !ydie[Y]) {
					// make edge
					//printf("make %d %d\n", X, Y);
					e[X].push_back(Y);
				}
			}
		}
		augment_path();
		for(int Y=0; Y<N+N-1; Y++) {
			if(match[Y] != -1) {
				int X, r, c;
				X = match[Y];
				r = (X+Y-N+3)/2;
				c = (X-Y+N+1)/2;
				//printf("pair x%d y%d (%d %d)\n", X, Y, r, c);
				tablep[r][c] = true;
			}
		}
		/////////////////////////
		/*
		for(int i=1; i<=N; i++)
			for(int j=1; j<=N; j++)
				printf("%c%c", tablep[i][j]?'+':'.', j==N?'\n':' ');
		//*/
		/////////////////////////
		// 建立新的 table
		int style = 0, modi = 0; // style point & modify point
		for(int r=1; r<=N; r++) {
			for(int c=1; c<=N; c++) {
				char md = '.';
				if(tablex[r][c] && tablep[r][c]) {
					md = 'o';
				}
				else if(tablex[r][c]) {
					md = 'x';
				}
				else if(tablep[r][c]) {
					md = '+';
				}
				table_new[r][c] = md;
				style += (tablex[r][c] + tablep[r][c]);
			}
		}
		for(int r=1; r<=N; r++) {
			for(int c=1; c<=N; c++) {
				if(table_old[r][c] != table_new[r][c]) {
					modi++;
				}
			}
		}
		/////////////////////////
		/*
		printf(">>> old\n");
		for(int i=1; i<=N; i++)
			for(int j=1; j<=N; j++)
				printf("%c%c", table_old[i][j], j==N?'\n':' ');
		printf(">>> new\n");
		for(int i=1; i<=N; i++)
			for(int j=1; j<=N; j++)
				printf("%c%c", table_new[i][j], j==N?'\n':' ');
		//*/
		/////////////////////////
		// output
		printf("Case #%d: %d %d\n", tc, style, modi);
		for(int r=1; r<=N; r++) {
			for(int c=1; c<=N; c++) {
				if(table_old[r][c] != table_new[r][c]) {
					printf("%c %d %d\n", table_new[r][c], r, c);
				}
			}
		}
	}
	return 0;
}

