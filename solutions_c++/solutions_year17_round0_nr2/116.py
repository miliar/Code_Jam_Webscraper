#include <cstdio>
#include <cstring>

const int MAX = 20;

char data[MAX];

void solve() {
	int len = strlen(data);
	int lastIncrease = 0;

	int now;
	for (now = 1; now < len; now++) {
		if (data[now-1] > data[now]) {
			break;
		} else if (data[now-1] < data[now]) {
			lastIncrease = now;
		}
	}

	if (now == len) {
		// monotonic
		puts(data);
	} else {
		char ans[MAX];
		for (int i = 0; i < lastIncrease; i++)
			ans[i] = data[i];
		ans[lastIncrease] = data[lastIncrease]-1;
		for (int i = lastIncrease+1; i < len; i++)
			ans[i] = '9';
		ans[len] = 0;

		for (int i = 0; i < data[i]; i++) {
			if (ans[i] != '0') {
				puts(ans+i);
				return;
			}
		}
	}
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for (int nowCase = 1; nowCase <= numCase; nowCase++) {
		scanf("%s", data);

		printf("Case #%d: ", nowCase);
		solve();
	}

	return 0;
}