#include <bits/stdc++.h>

using namespace std;

int T;
int k;
int lena;
char stra[5000];
char strb[5000];

int begini[20];

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%s", stra);
		lena = strlen(stra);

		memset(begini, -1, sizeof(begini));

		int maxa = stra[0] - '0';
		begini[maxa] = 0;

		int flag0 = 0;
		for (int i = 0; i < lena; i++) {
			if (flag0) {
				strb[i] = '9';
				continue;
			}
			int nowa = stra[i] - '0';
			if (nowa > maxa) {
				maxa = nowa;
				begini[maxa] = i;
			} else if (nowa < maxa) {
				i = begini[maxa];
				begini[maxa] = -1;
				strb[i]--;
				flag0 = 1;
				continue;
			}
			strb[i] = maxa + '0';
		}
		strb[lena] = 0;

		long long ansa;
		sscanf(strb, "%lld", &ansa);

		printf("Case #%d: ", t);
		printf("%lld\n", ansa);
		outa: 0;
	}

	return 0;
}
