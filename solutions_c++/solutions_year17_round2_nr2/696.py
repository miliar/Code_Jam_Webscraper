#include<stdio.h>
#include<string.h>
#include <algorithm>
#include<queue>
#include<string>
#include<math.h>
#include<vector>
#include <map>
#include <stack>
#include<set>

using namespace std;
const int MAXV = 18;

int S = MAXV - 1;
int E = MAXV - 2;
int INF = 1000000001;
int f[MAXV][MAXV];
int c[MAXV][MAXV];
int visit[MAXV];
int pre[MAXV];
vector<int> v[MAXV];
void mili() {
	int i;
	for (i = 1; i <= 6; i++) {
		v[i].push_back(S);
		v[S].push_back(i);
		
		v[i + 6].push_back(E);
		v[E].push_back(i + 6);
	}
	v[1].push_back(3 + 6);
	v[3 + 6].push_back(1);
	c[1][3 + 6] = INF;
	v[1].push_back(5 + 6);
	v[5 + 6].push_back(1);
	c[1][5 + 6] = INF;
	v[1].push_back(4 + 6);
	v[4 + 6].push_back(1);
	c[1][4 + 6] = INF;

	v[3].push_back(1 + 6);
	v[1 + 6].push_back(3);
	c[3][1 + 6] = INF;
	v[3].push_back(5 + 6);
	v[5 + 6].push_back(3);
	c[3][5 + 6] = INF;
	v[3].push_back(6 + 6);
	v[6 + 6].push_back(3);
	c[3][6 + 6] = INF;

	v[5].push_back(1 + 6);
	v[1 + 6].push_back(5);
	c[5][1 + 6] = INF;
	v[5].push_back(3 + 6);
	v[3 + 6].push_back(5);
	c[5][3 + 6] = INF;
	v[5].push_back(2 + 6);
	v[2 + 6].push_back(5);
	c[5][2 + 6] = INF;

	v[2].push_back(5 + 6);
	v[5 + 6].push_back(2);
	c[2][5 + 6] = INF;

	v[4].push_back(1 + 6);
	v[1 + 6].push_back(4);
	c[4][1 + 6] = INF;

	v[6].push_back(3 + 6);
	v[3 + 6].push_back(6);
	c[6][3 + 6] = INF;
}
int main() {
	mili();
	int tc, t, i, j;
	FILE *fp1,*fp2;
	fp1= fopen("1.in", "r");
	fp2 = fopen("2.out","w");
	fscanf(fp1, "%d", &tc);
	for (t = 1; t <= tc; t++) {
		memset(f, 0, sizeof(f));
		memset(visit, 0, sizeof(visit));
		memset(pre, 0, sizeof(pre));
		fprintf(fp2, "Case #%d: ", t);
		int n;
		int x[6];//r,o,y,g,b,v
		fscanf(fp1, "%d", &n);
		for (i = 1; i <= 6;i++)
			fscanf(fp1, "%d", &x[i]);
		for (i = 1; i <= 6; i++) {
			c[S][i] = x[i];
			c[i+6][E] = x[i];
		}
		int dap = 0;
		while (1) {
			memset(visit, 0, sizeof(visit));
			queue<int> Q;
			Q.push(S);
			visit[S] = 1;
			while (!Q.empty()) {
				int temp = Q.front(); Q.pop();
				if (temp == E)break;
				int l =v[temp].size(), i;
				for (i = 0; i < l; i++) {
					if (!visit[v[temp][i]] && c[temp][v[temp][i]] - f[temp][v[temp][i]]>0) {
						visit[v[temp][i]] = 1;
						Q.push(v[temp][i]);
						pre[v[temp][i]] = temp;
					}
				}
			}
			if (!visit[E])break;
			int cur = E,mnf=INF;
			while (cur != S) {
				int p = pre[cur];
				mnf = min(mnf, c[p][cur]-f[p][cur]);
				cur = p;
			}
			cur = E;
			dap += mnf;
			while (cur != S) {
				int p = pre[cur];
				f[p][cur]+=mnf;
				f[cur][p]-=mnf;
				cur = p;
			}
		}
		if (dap != n)
			fprintf(fp2,"IMPOSSIBLE\n");
		else {
			int before=0;//r,o,y,g,b,v
			for (before = 1; before <= 6; before++) {
				if (f[S][before] > 0)break;
			}
			while (1) {
				char temp;
				if (before == 1)temp = 'R';
				else if (before == 2)temp = 'O';
				else if (before == 3)temp = 'Y';
				else if (before == 4)temp = 'G';
				else if (before == 5)temp = 'B';
				else if (before == 6)temp = 'V';
				f[S][before]--;
				dap--;
				fprintf(fp2,"%c", temp);
				if (dap == 0)break;
				for (i = 1; i <= 6; i++) {
					if (f[before][i + 6] > 0&&f[S][i]>0) {
						f[before][i + 6]--;
						before = i;
						break;
					}
				}
			}
			fprintf(fp2, "\n");
		}
	}
	fclose(fp1);
	fclose(fp2);
}


