#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

#define LL unsigned long long
#define INF (1ULL<<63)

int T, nCase;
int R, C;
char cake[27][27];
int cnt[27][27];

void calc()
{
	memset(cnt, 0, sizeof(cnt));
	for (int i=1; i<=R; ++i)
		for (int j=1; j<=C; ++j)
			cnt[i][j] = cnt[i-1][j] + cnt[i][j-1] - cnt[i-1][j-1] + (cake[i][j] != '?'?1:0);
	return;
	for (int i=1; i<=R; ++i) {
		for (int j=1; j<=C; ++j)
			cout << cnt[i][j] << " ";
		cout<<endl;
	}

}

bool alone(int x1, int y1, int x2, int y2)
{
	int c = cnt[x2][y2] - cnt[x2][y1-1] - cnt[x1-1][y2] + cnt[x1-1][y1-1];
//	printf("range(%d-%d, %d-%d), cnt=%d\n", x1, y1, x2,y2, c);

	return c == 1;
}

void tofill(int x, int y)
{
	int best = 0;
	int xx1, yy1, xx2, yy2;
	calc();
	for (int x1=1; x1 <=x; ++x1) {
		for (int y1=1; y1 <=y; ++y1) {

			for (int x2=x; x2 <=R; ++x2) {
				for (int y2=y; y2 <=C; ++y2) {
					if (alone(x1, y1, x2, y2)) {
						if ((x2-x1+1) * (y2-y1+1) > best) {
							best = (x2-x1+1) * (y2-y1+1);
							xx1 = x1, yy1 = y1, xx2 = x2, yy2 = y2;
						}
					}
				}
			}
		}
	}
//	printf("fill range(%d-%d, %d-%d), cnt=%d\n", xx1, yy1, xx2,yy2, best);

	for (int i=xx1; i <=xx2; ++i) {
		for (int j=yy1; j <=yy2; ++j) {
			cake[i][j] = cake[x][y];
		}
	}
}

void solv()
{
	bool visit[26];
	memset(visit, 0, sizeof(visit));
	for (int i=1; i<=R; ++i)
		for (int j=1; j<=C; ++j)
			if (cake[i][j] != '?' && !visit[cake[i][j]-'A']) {
				visit[cake[i][j]-'A'] = true;
				tofill(i,j);
			}
	for (int i=1; i<=R; ++i) {
		cout << cake[i] + 1 << endl;
	}
}

int main ()
{
	cin >> T;
	for (nCase = 1; nCase <= T; ++nCase) {
		cin >> R >> C;
		memset(cake, 0, sizeof(cake));
		for (int i=1; i<=R; ++i)
			cin >> cake[i] + 1 ;
		cout << "Case #" << nCase << ":\n";
		solv();
	}
	return 0;
}