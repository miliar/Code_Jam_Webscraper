#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 112;
int const MAX_CH = 300100;
int const INT_INF = 1000000000;

char st[MAX_CH];
int tst,n,m,surv[MAX_N],s[MAX_N][MAX_N];
pair<long long, long long> amnt[MAX_N][MAX_N];

int our_h,our_a,ene_h,ene_a,B,D;
short int dst[MAX_N][MAX_N][MAX_N][MAX_N];
struct pp {
	char our_h,our_a,ene_h,ene_a;
} q[MAX_N*MAX_N*MAX_N*MAX_N];
int p_read = 0, p_write = 1;
int ans = INT_INF;

void move_to_state(int our_h, int our_a, int ene_h, int ene_a, int new_dst) {
	if (ene_h <= 0) {
		ans = min(ans, new_dst);
		return;
	}

	our_h -= ene_a;
	if (our_h <= 0)
		return;

	if (dst[our_h][our_a][ene_h][ene_a] > new_dst) {
		dst[our_h][our_a][ene_h][ene_a] = new_dst;

		q[p_write].our_h = our_h;
		q[p_write].our_a = our_a;
		q[p_write].ene_h = ene_h;
		q[p_write].ene_a = ene_a;
		p_write++;
	}
}

short int const MX_DST = 20000; //126;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	sscanf(st,"%d",&tst);

	for (int i=0; i<MAX_N; i++)
		for (int j=0; j<MAX_N; j++)
			for (int qq=0; qq<MAX_N; qq++)
				for (int ww=0; ww<MAX_N; ww++)
					dst[i][j][qq][ww] = MX_DST;

	for (int qqq=1; qqq<=tst; qqq++) {
		scanf("%d%d%d%d%d%d",&our_h,&our_a,&ene_h,&ene_a,&B,&D);
		int init_H = our_h;

		ans = INT_INF;

		dst[our_h][our_a][ene_h][ene_a] = 0;
		p_read = 0, p_write = 1;
		q[p_read].our_h = our_h;
		q[p_read].our_a = our_a;
		q[p_read].ene_h = ene_h;
		q[p_read].ene_a = ene_a;
		while (p_read < p_write) {
			our_h = q[p_read].our_h;
			our_a = q[p_read].our_a;
			ene_h = q[p_read].ene_h;
			ene_a = q[p_read].ene_a;
			p_read++;

			int our_dst = dst[our_h][our_a][ene_h][ene_a];

			move_to_state(our_h, our_a, ene_h - our_a, ene_a, our_dst + 1);
			move_to_state(our_h, min(MAX_N-1, our_a + B), ene_h, ene_a, our_dst + 1);
			move_to_state(init_H, our_a, ene_h, ene_a, our_dst + 1);
			move_to_state(our_h, our_a, ene_h, max(0,ene_a-D), our_dst + 1);

			if (ans < INT_INF / 2)
				break;
		}

		for (int r=0; r<p_write; r++)
			dst[q[r].our_h][q[r].our_a][q[r].ene_h][q[r].ene_a] = MX_DST;

		if (ans >= INT_INF / 2)
			printf("Case #%d: IMPOSSIBLE\n",qqq);
		else
			printf("Case #%d: %d\n",qqq,ans);
	}
	return 0;
}
