#include <bits/stdc++.h>

using namespace std;

const double eps = 1e-9;

int Test, N, M, ans, len;
int A[60][60];
int B[60];
int Head[60];
int ls[10010];

class rec{
	public:
	int l, r;
};

class recline{
	public:
	rec a[60];
} T[60];

bool cmplr(const rec &A, const rec &B){
	if (A.l != B.l) return A.l < B.l;
	return A.r < B.r;
}

double down(double x){
	int y = int (x + eps);
	return y;
}

double up(double x){
	int y = int(x + eps);
	if (y < x) y++;
	return y;
}

int main(){
//	freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int tt = 1; tt <= Test; tt++){
		scanf("%d%d", &N, &M);
		for (int i = 1; i <= N; i++)
			scanf("%d", &B[i]);
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= M; j++){
				scanf("%d", &A[i][j]);
				int ll = up(double(A[i][j]) / (B[i] * 1.1));
				int rr = down(double(A[i][j]) / (B[i] * 0.9));
				T[i].a[j].l = ll;
				T[i].a[j].r = rr;
				ls[++len] = ll;
				ls[++len] = rr;
			}
		sort(ls + 1, ls + len + 1);
		len = unique(ls + 1, ls + len + 1) - ls - 1;
		for (int i = 1; i<= N; i++)
			sort(T[i].a + 1, T[i].a + M + 1, cmplr);
		ans = 0;
		for (int i = 1; i <= N; i++)
			Head[i] = 1;
		for (int i = 1; i <= len; i++){
			for (int j = 1; j <= N; j++)
				while (Head[j] <= M && (T[j].a[Head[j]].r < ls[i] || T[j].a[Head[j]].l > T[j].a[Head[j]].r))
					Head[j]++;
			bool flag = 1;
			while (flag){
				for (int j = 1; j <= N; j++)
					if (Head[j] > M || T[j].a[Head[j]].l > ls[i])
						flag = 0;
				if (flag){
					ans++;
					for (int j = 1; j <= N; j++)
						Head[j]++;
				} else break;
			}
		}
		printf("Case #%d: ", tt);
		printf("%d\n", ans);
	}
}