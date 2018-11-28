#include<stdio.h>
#include<algorithm>
using namespace std;
int n;
int a, b, c, d, e, f;
char res[100009];
int rl;
int able;
void push_a() {
	while (d) {
		res[rl++] = 'R';
		res[rl++] = 'G';
		a--; d--;
	}
	if (a) {
		res[rl++] = 'R';
		a--;
	}
}
void push_y() {
	while (f) {
		res[rl++] = 'Y';
		res[rl++] = 'V';
		c--; f--;
	}
	if (c) {
		res[rl++] = 'Y';
		c--;
	}
}
void push_b() {
	while (b) {
		res[rl++] = 'B';
		res[rl++] = 'O';
		e--; b--;
	}
	if (e) {
		res[rl++] = 'B';
		e--;
	}
}
int main() {
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small-attempt0.out", "wt", stdout);
//	freopen("B-large.in", "rt", stdin);
//	freopen("B-large.out", "wt", stdout);
	int t=1, tv = 0;
	int i, j, k, l;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d", &n);
		scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
		able = 1;
		int last = -1;
		int cycle = 0;
		if (a < d) able = 0;
		if (c < f) able = 0;
		if (e < b) able = 0;
		if (able == 1) {
			int ta, tc, te;
			ta = a - d;
			tc = c - f;
			te = e - b;
			if (last == -1 && ta <= tc + te)
			{
				cycle = tc + te - ta;
				if(cycle <= ta && cycle <= tc && cycle <= te)
				last = 0;
			}
			if (last == -1 && tc <= ta + te)
			{
				cycle = ta + te - tc;
				if (cycle <= ta && cycle <= tc && cycle <= te)
				last = 1;
			}
			if (last == -1 && te <= ta + tc)
			{
				cycle = tc + ta - te;
				if (cycle <= ta && cycle <= tc && cycle <= te)
				last = 2;
			}
			if (last == -1)
				able = 0;
		}
		if(able == 0)
			printf("Case #%d: %s\n", ++tv,"IMPOSSIBLE");
		else
		{
			rl = 0;
			while (a || b || c || d || e || f)
			{
				if (cycle && a && c && e) {
					if (last == 0)
					{
						push_a();
						push_y();
						push_b();
					}
					else if (last == 1) {
						push_y();
						push_b();
						push_a();
					}
					else if (last == 2) {
						push_b();
						push_a();
						push_y();
					}
					cycle--;
				}
				else if (last == 0) {
					if (c)
					{
						push_a();
						push_y();
					}
					else
					{
						push_a();
						push_b();
					}
				}
				else if (last == 1) {
					if (a)
					{
						push_y();
						push_a();
					}
					else
					{
						push_y();
						push_b();
					}
				}
				else if (last == 2) {
					if (a)
					{
						push_b();
						push_a();
					}
					else
					{
						push_b();
						push_y();
					}
				}
				else
				{
					printf("wahaha %d %d %d\n", a, c, e);
				}
				res[rl] = 0;
		//		printf("%d , %s\n", rl, res);
			}
			res[rl] = 0;
			printf("Case #%d: %s\n", ++tv, res);

		}
	}
}