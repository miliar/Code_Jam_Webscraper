#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#define maxn 120
using namespace std;
struct twosat
{
    int n,c;
    vector<int>map[2*maxn+10];
    bool mark[2*maxn+10];
    int stack[2*maxn+10];
    void Init(int n)
    {
        this->n=n;
        for(int i=0;i<2*n;++i)
            map[i].clear();
        memset(mark,0,sizeof(mark));
        return ;
    }
    void add_edge(int s,int t)
    {
        map[s].push_back(t);
        return;
    }
    bool DFS(int i)
    {
        if(mark[i^1]) return false;
        if(mark[i]) return true;
        mark[i]=true;
        stack[c++]=i;
        int len=map[i].size();
        for(int j=0;j<len;++j)
            if(!DFS(map[i][j])) return false;
        return true;
    }
    bool solve()
    {
        for(int i=0;i<2*n;i+=2)
            if(!mark[i]&&!mark[i+1])
            {
                c=0;
                if(!DFS(i))
                {
                    while(c>0) mark[stack[--c]]=false;
                    if(!DFS(i+1)) return false;
                }
            }
        return true;
    }
}solve;
int dd[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
char c[maxn][maxn];
int x[maxn], y[maxn];
int p[maxn][maxn][2];
bool flag1[maxn], flag2[maxn];
int n, m;
int N;
int idx(int i, int k) {
	return (i - 1) * 2 + k;
}
bool DFS(int i, int j, int d, int N, bool s, int k) {
	if((c[i][j] == '|' || c[i][j] == '-') && !s) return false;
	if(c[i][j] == '#' || i < 1 || i > n || j < 1 || j > m) return true;
	if(c[i][j] == '\\') {
		if(d == 0) d = 1;
		else if(d == 1) d = 0;
		else if(d == 2) d = 3;
		else d = 2;
	}
	else if(c[i][j] == '/') {
		if(d == 0) d = 3;
		else if(d == 1) d = 2;
		else if(d == 2) d = 1;
		else d = 0;
	}
	int ii = i + dd[d][0], jj = j + dd[d][1];
	bool f = DFS(ii, jj, d, N, 0, k);
	if(f && c[i][j] == '.') {
		p[i][j][k] = N;
	}
	return f;
}
int main() {
	freopen("C-small-attempt3.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int T;
	cin >> T;
	for(int ii = 1; ii <= T; ++ii) {
		scanf("%d%d", &n, &m);
		N = 0;
		for(int i = 1; i <= n; ++i)
			scanf("%s", c[i] + 1);
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j) {
				if(c[i][j] == '|' || c[i][j] == '-') {
					N++;
					flag1[N] = flag2[N] = true;
					x[N] = i; y[N] = j;
					flag2[N] = min(DFS(i, j, 0, N, true, 1), DFS(i, j, 2, N, true, 1));
					flag1[N] = min(DFS(i, j, 1, N, true, 0), DFS(i, j, 3, N, true, 0));
				}
			}
		solve.Init(N);
		bool flag = true;
		for(int i = 1; i <= N; ++i)
			if(!flag1[i] && !flag2[i]) flag = false;
			else if(!flag1[i])
				solve.add_edge(idx(i, 0), idx(i, 1));
			else if(!flag2[i])
				solve.add_edge(idx(i, 1), idx(i, 0));
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
				if(c[i][j] == '.') {
					if(!p[i][j][0] && !p[i][j][1])
						flag = false;
					else if(!p[i][j][0])
						solve.add_edge(idx(p[i][j][1], 0), idx(p[i][j][1], 1));
					else if(!p[i][j][1])
						solve.add_edge(idx(p[i][j][0], 1), idx(p[i][j][0], 0));
					else {
						solve.add_edge(idx(p[i][j][0], 1), idx(p[i][j][1], 1));
						solve.add_edge(idx(p[i][j][1], 0), idx(p[i][j][0], 0));
					}
				}
		printf("Case #%d: ", ii);
		if(!flag) printf("IMPOSSIBLE\n");
		else {
			flag = solve.solve();
			if(!flag) printf("IMPOSSIBLE\n");
			else {
				printf("POSSIBLE\n");
				for(int i = 0; i <2*solve.n; i += 2)
				{
					if(solve.mark[i]) c[x[i / 2 + 1]][y[i / 2 + 1]] = '-';
					else c[x[i / 2 + 1]][y[i / 2 + 1]] = '|';
				}
				for(int i = 1; i <= n; ++i)
					printf("%s\n", c[i] + 1);
			}
		}
		memset(p, 0, sizeof p);
	}
	return 0;
}