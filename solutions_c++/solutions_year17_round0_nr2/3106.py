#include <cstdio>
using namespace std;

char buf[100];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		scanf("%s", buf);
		for (int i=0; buf[i]; ++i) {
			bool ok = true;
			for (int j=i+1; buf[j]; ++j) {
				if (buf[j] < buf[i]) {
					ok = false;
					break;
				}
				if (buf[j] > buf[i])
					break;
			}
			if (ok) continue;
			--buf[i];
			for (int j=i+1; buf[j]; ++j)
				buf[j] = '9';
			break;
		}
		printf("Case #%d: ", TN);
		printf("%s\n", buf + (buf[0] == '0'));
	}
	return 0;
}