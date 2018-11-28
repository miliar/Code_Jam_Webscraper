#include <cstring>
#include <iostream>
using namespace std;
const int nmax = 1000 + 18;

int T;
long long k[2], tmpk[2], n[2], tmpn[2], N, K, ansl, ansr;

void add(long long kk, long long nn)
{
	if (kk == 0) return;
	//printf("add %I64d %I64d\n", kk, nn);
	if (k[0] == -1 || k[0] == kk) {
		if (k[0] == -1)
			k[0] = kk;
		n[0] += nn;
	}
	else
		if (k[1] == -1 || k[1] == kk) {
			if (k[1] == -1)
				k[1] = kk;
			n[1] += nn;
		}
		else 
			printf("fk!\n");
}

void getans(long long k) 
{
	if (k & 1)
		ansl = ansr = k / 2;
	else
		ansl = k / 2, ansr = ansl - 1;
}

void swap(long long &a, long long &b) 
{
	long long tmp = a;
	a = b;
	b = tmp;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%I64d%I64d", &N, &K);
		k[0] = N, n[0] = 1;
		n[1] = 0;
		for (;;) {
			if (n[0] >= K) {
				getans(k[0]);
				break;
			}
			K -= n[0];
			if (n[1] >= K) {
				getans(k[1]);
				break;
			}
			K -= n[1];
			tmpk[0] = k[0];
			tmpk[1] = k[1];
			tmpn[0] = n[0];
			tmpn[1] = n[1];
			n[0] = n[1] = 0;
			k[0] = k[1] = -1;
			
			for (int i = 0; i < 2; ++i) 
				if (tmpn[i] > 0) {
					long long L, R;
					if (tmpk[i] & 1)
						L = R = tmpk[i] / 2;
					else {
						L = tmpk[i] / 2 - 1;
						R = tmpk[i] / 2;
					}
					add(L, tmpn[i]);
					add(R, tmpn[i]);
				}
			
			if (k[0] < k[1])
				swap(n[0], n[1]), swap(k[0], k[1]);
		}
		printf("Case #%d: %I64d %I64d\n", cases, ansl, ansr);
		
	}
	return 0;
}
