#include <iostream>
#include <thread>
#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <unistd.h>
#include <cmath>
#include <set>
#include <queue>

using namespace std;

typedef long long ll;
typedef double dd;
const ll size = 111002;
const ll mod = 1000000007;
#define P(a) cout<<(a)<<endl;
#define PP(a) cout<<(a)<<' ';
#define FOR(i, a, b)   for (int i = (a); i <= (b); ++i)
#define FORD(i, a, b)  for (int i = (a); i >= (b); --i)
#define REP(i, b)      for (int i =  0 ; i <  (b); ++i)
#define mid ((l+r)/2)
#define lp (p*2)
#define rp (p*2+1)
void PLL(initializer_list<ll> li) {
	for (auto beg = li.begin(); beg != li.end(); beg++) {
		if (beg != li.begin()) cout << ' '; cout << *beg;
	} cout << endl;
}

int n, m, t;
char ch[55][55], TOT = 0;
vector<int> vec[55][55][2];
int dir[][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
int vis[55][55][2];
map<int, int> M[2];
int tot, idn[55][55], ok[3000][2];

void dfs(int x, int y, int p, int d) {
	int tag = idn[x][y] * 2 + p;
	TOT ++;
	while (1) {
		x += dir[d][0];
		y += dir[d][1];
		if (x < 0 || y < 0 || x >= n || y >= m) return;
		if (vis[x][y][d%2] == TOT) return;
		if (ch[x][y] == '#') return;
		vis[x][y][d%2] = TOT;
		if (ch[x][y] == '\\') {
			d = M[0][d];
		}
		else if(ch[x][y] == '/') d = M[1][d];
		else {
			vec[x][y][d%2].push_back(tag);
		}
	}

}
const int maxn=10000+10;
struct TwoSAT
{
    int n;//原始图的节点数(未翻倍)
    vector<int> G[maxn*2];//G[i]==j表示如果mark[i]=true,那么mark[j]也要=true
    bool mark[maxn*2];//标记
    int S[maxn*2],c;//S和c用来记录一次dfs遍历的所有节点编号

    void init(int n)
    {
        this->n=n;
        for(int i=0;i<2*n;i++) G[i].clear();
        memset(mark,0,sizeof(mark));
    }

    //加入(x,xval)或(y,yval)条件
    //xval=0表示假，yval=1表示真
    void add_clause(int x,int xval,int y,int yval)
    {
        x=x*2+xval;
        y=y*2+yval;
        G[x^1].push_back(y);
        G[y^1].push_back(x);
    }
	void add2(int x, int y) {
		G[x].push_back(y);
	}

    //从x执行dfs遍历,途径的所有点都标记
    //如果不能标记,那么返回false
    bool dfs(int x)
    {
        if(mark[x^1]) return false;//这两句的位置不能调换
        if(mark[x]) return true;
        mark[x]=true;
        S[c++]=x;
        for(int i=0;i<G[x].size();i++)
            if(!dfs(G[x][i])) return false;
        return true;
    }

    //判断当前2-SAT问题是否有解
    bool solve()
    {
        for(int i=0;i<2*n;i+=2)
        if(!mark[i] && !mark[i+1])
        {
            c=0;
            if(!dfs(i))
            {
                while(c>0) mark[S[--c]]=false;
                if(!dfs(i+1)) return false;
            }
        }
        return true;
    }
}S;

int main () {
	M[0][0] = 3; M[0][3] = 0; 
	M[0][1] = 2; M[0][2] = 1;
	M[1][0] = 1; M[1][1] = 0;
	M[1][2] = 3; M[1][3] = 2;
	cin >> t;
	for (int ca = 1; ca <= t; ca++) {
		cin >> n >> m;
		//cout<<n<<' '<<m<<endl;
		REP(i, n) {
			cin >> ch[i];
			REP(j, m) {
				vec[i][j][0].clear();
				vec[i][j][1].clear();
			}
		}
		memset(vis, -1, sizeof(vis));
		tot = 0;
		REP(i, n) REP(j, m) {
			if (ch[i][j] == '|' || ch[i][j] == '-') {
				idn[i][j] = tot ;
				ok[tot][0] = ok[tot][1] = 1;
				tot++;
			}
		}
		S.init(tot);
		REP(i, n) {
			REP(j, m) {
				if (ch[i][j] == '|' || ch[i][j] == '-') {
					dfs(i, j, 0, 1);
					dfs(i, j, 0, 3);
					dfs(i, j, 1, 0);
					dfs(i, j, 1, 2);
				}
			}
		}
		int fal = 0;
		REP(i, n) REP(j, m) {
			/*
			cout<<"+++++++++\n";
			cout<<i<<' '<<j<<endl;
			for (int p = 0; p < 2; p++) {
				for (auto x: vec[i][j][p]) cout <<x<<' ';cout<<endl;
				
			}
			*/
			if (ch[i][j] == '|' || ch[i][j] == '-') {
				for (int p = 0; p < 2; p++) {
					if (vec[i][j][p].size() > 0) {
						for (auto x: vec[i][j][p]) S.add2(x, x^1);
					}
				}
			}
			if (ch[i][j] == '.') {
				for (int p = 0; p < 2; p++) {
					if (vec[i][j][p].size() > 1) {
						for (auto x: vec[i][j][p]) S.add2(x, x^1);
					}
				}
				if (vec[i][j][0].size() == 1 && vec[i][j][1].size() == 1) {
					int x = vec[i][j][0][0], y = vec[i][j][1][0];
					S.add_clause(x/2, x%2, y/2, y%2);
				}
				else if (vec[i][j][0].size() == 1) {
					int x = vec[i][j][0][0];
					S.add2(x^1, x);
				}
				else if (vec[i][j][1].size() == 1) {
					int y = vec[i][j][1][0];
					S.add2(y^1, y);
				}
				else fal = 1;
			}
		}
		if (fal || !S.solve())
			printf("Case #%d: IMPOSSIBLE\n", ca);
		else {
			printf("Case #%d: POSSIBLE\n", ca);
			REP(i, n) {
				REP(j, m) {
					if (ch[i][j] == '|' || ch[i][j] == '-') {
						if (S.mark[idn[i][j]<<1] == true) ch[i][j] = '-';
						else ch[i][j] = '|';
					}
					cout << ch[i][j];
				}
				cout << endl;
			}	
		}
	}
}
