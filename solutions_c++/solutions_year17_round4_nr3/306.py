#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

#define sss 500
#define esss 1000000

int v[sss], cnt, v2[sss], cnt2;
struct edge{int from, to, next;}e[esss], e2[esss];

void insert(int from, int to)
{
	//printf("adding %d -> %d\n", from, to);
    e[cnt].from = from, e[cnt].to = to; e[cnt].next = v[from]; v[from] = cnt++;
}
void insert2(int from, int to)
{
    e2[cnt2].from = from, e2[cnt2].to = to; e2[cnt2].next = v2[from]; v2[from] = cnt2++;
}

int index, dfn[sss], low[sss], instack[sss], sta[sss], top;
int belong[sss], cntnum, num[sss];
int cf[sss], rd[sss], que[sss], col[sss];
bool ans[sss];
void tarjan(int id)
{
    dfn[id] = low[id] = ++index;
    instack[id] = 1; sta[top++] = id;
    int tmp = v[id];
    while(tmp != -1)
    {
        if (!dfn[e[tmp].to])
        { tarjan(e[tmp].to);
            if (low[e[tmp].to] < low[id]) low[id] = low[e[tmp].to];
        }
        else if (instack[e[tmp].to] && dfn[e[tmp].to] < low[id])
            low[id] = dfn[e[tmp].to];
        tmp = e[tmp].next;
    }
    if (dfn[id] == low[id])
    {
        do
        { tmp = sta[--top]; instack[tmp] = 0;
            belong[tmp] = cntnum;
            num[cntnum]++;
        }while(tmp != id);
        cntnum++;
    }
}
bool solve2(int n) 
{
    index = cntnum = top = 0;
    memset(dfn, 0, sizeof(dfn));
    memset(num, 0, sizeof(num));
    for(int i = 0; i < 2 * n; i++)
        if (!dfn[i]) tarjan(i);
    for(int i = 0; i < n; i++)                  
    {
        if (belong[i] == belong[i + n])
        {
            return false;
        }
        cf[belong[i]] = belong[i + n];
        cf[belong[i + n]] = belong[i];
    }
    memset(rd, 0, sizeof(rd));
    memset(v2, -1, sizeof(v2));
    memset(col, 0, sizeof(col));cnt2 = 0;
    for(int i = 0; i < cnt; i++)     
        if (belong[e[i].from] != belong[e[i].to])
        {
            insert2(belong[e[i].to], belong[e[i].from]);
            rd[belong[e[i].from]]++;
        }
    int head = 0, tail = 0;                
    for(int i = 0; i < cntnum; i++)
        if (rd[i] == 0) que[tail++] = i;
    while(head < tail)
    {
        int tmp = que[head++];
        if (col[tmp] == 0)                   
        {
            col[tmp] = 1;
            col[cf[tmp]] = -1;
        }
        int id = v2[tmp];
        while(id != -1)
        {
            if (--rd[e2[id].to] == 0)
                que[tail++] = e2[id].to;
            id = e2[id].next;
        }
    }
    memset(ans, 0, sizeof(ans));
    for(int i = 0; i < 2 * n; i++) 
        if (col[belong[i]] == 1) ans[i] = 1;
    return true;
}


int r, c;
char board[51][51];
int idx[51][51];
vector<int> hits[51][51];
int lasers;

void read() {
	scanf("%d %d", &r, &c);

	for (int i = 0; i < r; i++) {
		scanf("%s", board[i]);
	}
}

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

bool ok(int x, int y) {
	if (x < 0 || x >= r) return false;
	if (y < 0 || y >= c) return false;
	return true;
}

int partner(int x) {
	if (x >= lasers) return x - lasers;
	return x + lasers;
}

void dfs(int x, int y, int orig, int d) {
	//printf("dfs %d %d %d %d\n", x,y,orig,d);
	if (!ok(x,y) || board[x][y] == '#') return;

	hits[x][y].push_back(orig);

	if (board[x][y] == '|' || board[x][y] == '-') return;

	if (board[x][y] == '\\') {
		if (d == 0) d = 1;
		else if (d == 1) d = 0;
		else if (d == 2) d = 3;
		else if (d == 3) d = 2;
	}
	if (board[x][y] == '/') {
		if (d == 0) d = 3;
		else if (d == 1) d = 2;
		else if (d == 2) d = 1;
		else if (d == 3) d = 0;
	}

	dfs(x + dx[d], y + dy[d], orig, d);
}

void solve() {
	lasers = 0;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			hits[i][j].clear();
			if (board[i][j] == '|' || board[i][j] == '-') {
				idx[i][j] = lasers++;
			}
		}
	}

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			for (int d = 0; d < 4; d++) {
				if (board[i][j] == '|' || board[i][j] == '-') {
					dfs(i+dx[d], j+dy[d], idx[i][j] + lasers*(d&1), d);
				}
			}
		}
	}

	memset(v, -1, sizeof(v)); 
	cnt = 0;

	bool error = false;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (board[i][j] == '|' || board[i][j] == '-') {
				for (int x : hits[i][j]) {
					//printf("%d hits %d,%d!\n", x,i,j);
					insert(x, partner(x));
				}
			}
			else if (board[i][j] == '.') {
				if (hits[i][j].size() == 1) {
					int k = hits[i][j][0];
					insert(partner(k), k);
				}
				else if (hits[i][j].size() == 2) {
					int k = hits[i][j][0];
					int kk = hits[i][j][1];
					insert(partner(kk), k);
					insert(partner(k), kk);
				}
				else {
					error = true;
				}
			}
		}
	}

	if (error || !solve2(lasers)) {
		printf("IMPOSSIBLE\n");
		return;
	}

	printf("POSSIBLE\n");
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (board[i][j] == '|' || board[i][j] == '-') {
				if (ans[idx[i][j]]) printf("|");
				else printf("-");
			}
			else printf("%c", board[i][j]);
		}
		printf("\n");
	}
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
		}
	}
}