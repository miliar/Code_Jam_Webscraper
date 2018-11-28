#include <cstdio>
using namespace std;
typedef long long ll;

const int MAX_LEN = 19;

void solve() {
	int arr[MAX_LEN];
	int len = 0;
	for (int c=getchar(); c!='\n'; c=getchar()) {
		arr[len++] = c;
	}

	bool fail = false;
	int i;
	for (i=0; i<len-1; i++) {
		if (arr[i] > arr[i+1]) {
			fail = true;
			arr[i]--;
			break;
		}
	}
	if (fail) {
		while (i>0 && arr[i-1] > arr[i]) {
			i--;
			arr[i]--;
		}
		for (i++; i<len; i++) {
			arr[i] = '9';
		}
	}

	for (i=(arr[0]=='0' ? 1 : 0);  i<len;  i++) {
		putchar(arr[i]);
	}
	putchar('\n');
}

int main() {
	int t;
	scanf("%d\n", &t);

	for (int i=1; i<=t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
