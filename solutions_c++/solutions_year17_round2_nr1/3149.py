#include <bits/stdc++.h>
using namespace std;

const int maxn = 1005;

struct Node {
	double st, speed;
}horse[maxn];

struct resNode {
	int tot;
	double st[maxn], ed[maxn], speed[maxn];
}divide[maxn];

double D;
int n;

bool operator < (const Node &a, const Node &b)
{
	return ((D - a.st) / a.speed) < ((D - b.st) / b.speed);
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T, caseT = 0;
	cin >> T;
	while (T--) {
		cin >> D >> n;
		for (int i = 0; i < n; i++)
			cin >> horse[i].st >> horse[i].speed;
		sort(horse, horse + n);
		/*divide[n - 1].tot = 1;
		divide[n - 1].st[0] = horse[n - 1].st;
		divide[n - 1].ed[0] = D;
		divide[n - 1].speed[0] = horse[n - 1].speed;
		for (int i = n - 2; i >= 0; i--) {
			double ttime = 0, len = -1.0;
			for (int j = 0; j < divide[i + 1].tot; j++) {
				if (divide[i + 1].speed[j] > horse[i].speed) {
					ttime += (divide[i + 1].ed[j] - divide[i + 1].st[j]) / divide[i + 1].speed[j];
					continue;
				}
				double pos = horse[i].st + ttime * horse[i].speed;
				if ( (divide[i + 1].ed[j] - pos) / horse[i].speed > 
				     (divide[i + 1].ed[j] - divide[i + 1].st[j]) / divide[i + 1].speed[j] ) {
				    ttime += (divide[i + 1].ed[j] - divide[i + 1].st[j]) / divide[i + 1].speed[j];
					continue;	
				}
				len = (divide[i + 1].st[j] - pos) / (divide[i + 1].speed[j] - horse[i].speed) * horse[i].speed + pos;
				divide[i].st[0] = horse[i].st;
				divide[i].ed[0] = len;
				divide[i].speed[0] = horse[i].speed;
				divide[i].tot = 1;
				for (int k = j; k < divide[i + 1].tot; k++) {
					int tmp = divide[i].tot;
					divide[i].st[tmp] = max(len, divide[i + 1].st[k]);
					divide[i].ed[tmp] = divide[i + 1].ed[k];
					divide[i].speed[tmp] = divide[i + 1].speed[k];
					divide[i].tot++;
				}
				break; 
			}
			if (len < 0) {
				divide[i].tot = 1;
				divide[i].st[0] = horse[i].st;
				divide[i].ed[0] = D;
				divide[i].speed[0] = horse[i].speed;
			} 
		}
		double res = 0.0;
		for (int i = 0; i < divide[0].tot; i++)
			res += (divide[0].ed[i] - divide[0].st[i]) / divide[0].speed[i];
		res = D / res;*/
		printf("Case #%d: %.6lf\n", ++caseT, D / (D - horse[n - 1].st) * horse[n - 1].speed);
	} 
	return 0;
} 
