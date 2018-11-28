#include <bits/stdc++.h>
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)
using namespace std;

#define x first
#define y second

char a[66][66];
int jid[66][66], hid[66][66], sid[66][66];
int n, m;

struct eheng
{
	int x, y1, y2;
} eh[6666]; int ehn;
struct eshu
{
	int x1, x2, y;
} es[6666]; int esn;
typedef pair<int, int> jing;
jing js[6666]; int jn;
bool canh[6666], cans[6666];
// [0, jn) heng = true, shu = false
// [jn, jn + eh) have = true, no = false
// [jn + eh, jn + eh + es) have = true, no = false
int satn;
vector<vector<int>> sate;
vector<bool> visit;

void ae(int x, int y)
{
	// printf("ae %d %d\n", x, y);
	sate[x].push_back(y);
	sate[y].push_back(x);
}

void fill(int x)
{
	if(visit[x]) return;
	visit[x] = true;
	for(int y: sate[x])
		fill(y);
}
vector<int> tofill;

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		cin >> n >> m;
		f(i, 1, n) cin >> (a[i] + 1);
		f(i, 0, n + 1) f(j, 0, m + 1) if(i == 0 || i == n + 1 || j == 0 || j == m + 1) a[i][j] = '#';
		ehn = esn = 0;
		f(i, 1, n) f(j, 1, m) if(a[i][j] == '.')
		{
			int k = j;
			while(a[i][k + 1] == '.') ++k;
			f(l, j, k) hid[i][l] = ehn;
			// printf("heng %d %d %d\n", i, j, k);
			eh[ehn++] = (eheng) {i, j, k};
			j = k + 1;
		}
		f(j, 1, m) f(i, 1, n) if(a[i][j] == '.')
		{
			int k = i;
			while(a[k + 1][j] == '.') ++k;
			f(l, i, k) sid[l][j] = esn;
			es[esn++] = (eshu) {i, k, j};
			// printf("shu %d %d %d\n", i, k, j);
			i = k + 1;
		}
		jn = 0;
		f(i, 1, n) f(j, 1, m) if(a[i][j] == '-' || a[i][j] == '|')
		{
			jid[i][j] = jn;
			js[jn++] = jing(i, j);
			a[i][j] = '-';
		}
		g(jid, 0, jn)
		{
			int x = js[jid].x, y = js[jid].y;
			canh[jid] = true;
			{
				int k = y - 1;
				while(a[x][k] == '.') --k;
				if(a[x][k] == '-') canh[jid] = false;
			}
			{
				int k = y + 1;
				while(a[x][k] == '.') ++k;
				if(a[x][k] == '-') canh[jid] = false;
			}
			cans[jid] = true;
			{
				int k = x - 1;
				while(a[k][y] == '.') --k;
				if(a[k][y] == '-') cans[jid] = false;
			}
			{
				int k = x + 1;
				while(a[k][y] == '.') ++k;
				if(a[k][y] == '-') cans[jid] = false;
			}
			if(!canh[jid] && !cans[jid])
				goto impossible;
		}
		satn = jn + ehn + esn;
		sate.clear();
		sate.resize(satn * 2);
		visit.clear();
		visit.resize(satn * 2);
		tofill.clear();
		g(i, 0, ehn)
		{
			int x = eh[i].x, y1 = eh[i].y1, y2 = eh[i].y2;
			bool ok = false;
			if(a[x][y1 - 1] == '-')
			{
				ae(jid[x][y1 - 1], jn + i);
				ae(jn + i + satn, jid[x][y1 - 1] + satn);
				ok = true;
			}
			if(a[x][y2 + 1] == '-')
			{
				ae(jid[x][y2 + 1], jn + i);
				ae(jn + i + satn, jid[x][y2 + 1] + satn);
				ok = true;
			}
			if(!ok)
				tofill.push_back(jn + i + satn);
		}
		g(i, 0, esn)
		{
			bool ok = false;
			int x1 = es[i].x1, x2 = es[i].x2, y = es[i].y;
			if(a[x1 - 1][y] == '-')
			{
				ae(jid[x1 - 1][y] + satn, jn + ehn + i);
				ae(jn + ehn + i + satn, jid[x1 - 1][y]);
				ok = true;
			}
			if(a[x2 + 1][y] == '-')
			{
				ae(jid[x2 + 1][y] + satn, jn + ehn + i);
				ae(jn + ehn + i + satn, jid[x2 + 1][y]);
				ok = true;
			}
			if(!ok)
				tofill.push_back(jn + ehn + i + satn);
		}
		f(i, 1, n) f(j, 1, m) if(a[i][j] == '.')
		{
			ae(jn + hid[i][j] + satn, jn + ehn + sid[i][j]);
			ae(jn + ehn + sid[i][j] + satn, jn + hid[i][j]);
		}
		g(i, 0, jn)
		{
			if(!canh[i]) fill(i + satn);
			if(!cans[i]) fill(i);
		}
		for(int x: tofill)
			fill(x);
		tofill.clear();
		g(i, 0, satn) if(visit[i] && visit[i + satn]) goto impossible;
		g(i, 0, jn)
		{
			if(visit[i + satn])
				a[js[i].x][js[i].y] = '|';
			else if(!visit[i] && !visit[i + satn])
			{
				fill(i);
				if(visit[i + satn])
				{
					printf("fuc\n");
					return 1;
				}
			}
		}
		g(i, 0, satn)
		
		{
			// printf("id %d vis %d vis+ %d\n", i, (int) visit[i], (int) visit[i + satn]);
			if((int) visit[i] + (int) visit[i + satn] != 1)
			{
				// printf("gg %d\n", i);
				goto impossible;
			}
		}
		printf("Case #%d: POSSIBLE\n", _);
		f(i, 1, n)
		{
			f(j, 1, m) putchar(a[i][j]);
			putchar('\n');
		}
		continue;
	impossible:
		printf("Case #%d: IMPOSSIBLE\n", _);
	}
	return 0;
}
