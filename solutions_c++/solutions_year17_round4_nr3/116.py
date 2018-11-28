#include<stdio.h>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
#define SIZE 5000
class twosat
{
public:
	int num;//ïœêîÇÃå¬êî
	vector<int>pat[SIZE * 2];
	vector<int>rpat[SIZE * 2];
	bool flag[SIZE * 2];
	int bun[SIZE * 2];
	vector<int>topo;
	void print()
	{
		for (int i = 0; i < num * 2; i++)
		{
			for (int j = 0; j < pat[i].size(); j++)
			{
				printf("%d %d\n", i, pat[i][j]);
			}
		}
	}
	void init(int n)
	{
		num = n;
		for (int i = 0; i < SIZE * 2; i++)
		{
			pat[i].clear();
			rpat[i].clear();
		}
	}
	void adde(int ax, bool ay, int bx, bool by)//ay ax or by bx Çí«â¡
	{
		int t = ax * 2, s = bx * 2;
		if ((ay) && (by))
		{
			pat[t + 1].push_back(s);
			pat[s + 1].push_back(t);
			rpat[t].push_back(s + 1);
			rpat[s].push_back(t + 1);
		}
		if ((!ay) && (by))
		{
			pat[t].push_back(s);
			pat[s + 1].push_back(t + 1);
			rpat[t + 1].push_back(s + 1);
			rpat[s].push_back(t);
		}
		if ((ay) && (!by))
		{
			pat[t + 1].push_back(s + 1);
			pat[s].push_back(t);
			rpat[t].push_back(s);
			rpat[s + 1].push_back(t + 1);
		}
		if ((!ay) && (!by))
		{
			pat[t].push_back(s + 1);
			pat[s].push_back(t + 1);
			rpat[t + 1].push_back(s);
			rpat[s + 1].push_back(t);
		}
	}
	void dfs(int node)
	{
		if (flag[node])return;
		flag[node] = true;
		for (int i = 0; i < pat[node].size(); i++)dfs(pat[node][i]);
		topo.push_back(node);
	}
	void rdfs(int node, int b)
	{
		if (flag[node])return;
		flag[node] = true;
		bun[node] = b;
		for (int i = 0; i < rpat[node].size(); i++)rdfs(rpat[node][i], b);
	}
	void scc()
	{
		fill(flag, flag + SIZE * 2, false);
		topo.clear();
		for (int i = 0; i < num * 2; i++)if (!flag[i])dfs(i);
		fill(flag, flag + SIZE * 2, false);
		int pt = 0;
		for (int i = num * 2 - 1; i >= 0; i--)if (!flag[topo[i]])rdfs(topo[i], pt++);
	}
	bool issatisfiable()
	{
		for (int i = 0; i < num; i++)
		{
			if (bun[i * 2] == bun[i * 2 + 1])return false;
		}
		return true;
	}
	vector<bool>getval()
	{
		vector<bool>ret;
		for (int i = 0; i < num; i++)
		{
			if (bun[i * 2] < bun[i * 2 + 1])ret.push_back(false);
			else ret.push_back(true);
		}
		return ret;
	}
};
twosat sat;
int dat[50][50];
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
int slash[4] = { 3,2,1,0 };
int bslash[4] = { 1,0,3,2 };
int dd[50][50][2];
typedef pair<int, int>pii;
typedef pair<pii, int>pi3;
int mx, my;
vector<pi3>get(int x, int y, int d)
{
	vector<pi3>r;
	//printf("\n");
	for (;;)
	{
		//printf("%d %d %d\n", x, y, d);
		x += dx[d], y += dy[d];
		if (!(0 <= x&&x < mx && 0 <= y&&y < my))return r;
		else if (dat[x][y] == -1)return r;
		else if (dat[x][y] == 0)r.push_back(make_pair(make_pair(x, y), d % 2));
		else if (dat[x][y] == 1)d = slash[d];
		else if (dat[x][y] == 2)d = bslash[d];
		else
		{
			r.clear();
			r.push_back(make_pair(make_pair(-1, -1), -1));
			return r;
		}
	}
}
bool check[50][50];
int main()
{
	freopen("c-large.in", "r", stdin);
	freopen("outl.txt", "wb", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		scanf("%d%d", &mx, &my);
		int cnt = 0;
		for (int i = 0; i < mx; i++)
		{
			for (int j = 0; j < my; j++)
			{
				char z;
				scanf(" %c", &z);
				if (z == '#')dat[i][j] = -1;
				else if (z == '/')dat[i][j] = 1;
				else if (z == '\\')dat[i][j] = 2;
				else if (z == '.')dat[i][j] = 0;
				else dat[i][j] = 3, cnt++;
			}
		}
		sat.init(cnt);
		for (int i = 0; i < mx; i++)for (int j = 0; j < my; j++)dd[i][j][0] = dd[i][j][1] = -1;
		int pt = 0;
		for (int i = 0; i < mx; i++)
		{
			for (int j = 0; j < my; j++)
			{
				if (dat[i][j] != 3)continue;
				for (int k = 0; k < 4; k++)
				{
					vector<pi3>z = get(i, j, k);
					if ((!z.empty()) && z[0].second == -1)
					{
						sat.adde(pt, (k % 2 == 1), pt, (k % 2 == 1));
						continue;
					}
					for (int l = 0; l < z.size(); l++)dd[z[l].first.first][z[l].first.second][z[l].second] = pt * 2 + k % 2;
				}
				pt++;
			}
		}
		bool f = true;
		for (int i = 0; i < mx; i++)
		{
			for (int j = 0; j < my; j++)
			{
				if (dd[i][j][0] != -1)
				{
					if (dd[i][j][1] != -1)sat.adde(dd[i][j][0] / 2, (dd[i][j][0] % 2 == 0), dd[i][j][1] / 2, (dd[i][j][1] % 2 == 0));
					else sat.adde(dd[i][j][0] / 2, (dd[i][j][0] % 2 == 0), dd[i][j][0] / 2, (dd[i][j][0] % 2 == 0));
				}
				else
				{
					if (dd[i][j][1] != -1)sat.adde(dd[i][j][1] / 2, (dd[i][j][1] % 2 == 0), dd[i][j][1] / 2, (dd[i][j][1] % 2 == 0));
					else if (dat[i][j] == 0)f = false;
				}
				//printf("%d %d   ", dd[i][j][0], dd[i][j][1]);
			}
			//printf("\n");
		}
		sat.scc();
		f &= sat.issatisfiable();
		printf("Case #%d: ", p);
		if (!f)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		printf("POSSIBLE\n");
		vector<bool>v = sat.getval();
		pt = 0;
		for (int i = 0; i < mx; i++)
		{
			for (int j = 0; j < my; j++)
			{
				char c;
				if (dat[i][j] == -1)c = '#';
				else if (dat[i][j] == 1)c = '/';
				else if (dat[i][j] == 2)c = '\\';
				else if (dat[i][j] == 0)c = '.';
				else
				{
					if (v[pt])c = '|';
					else c = '-';
					pt++;
				}
				printf("%c", c);
			}
			printf("\n");
		}
	}
}