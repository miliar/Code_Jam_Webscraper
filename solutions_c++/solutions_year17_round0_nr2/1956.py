#include <bits/stdc++.h>
using namespace std;

#define INF (1000000001)

int getint() {
	char c = ' ';
	for(; c < '0' || c > '9'; c = getchar());
	int ret = 0;
	for(; c >= '0' && c <= '9'; c = getchar()) ret = ret * 10 + c - '0';
	return ret;
}

const int N = 50;
char data[N], answer[N];
int n;

string solve() {
	n = strlen(data);
	memset(answer, 0, sizeof(answer));
	for(int i = n - 1, minimum = INF; i >= 0; --i) {
		int v = data[i] - '0';
		minimum = min(minimum, v);
		if(v == minimum) answer[i] = data[i];
		else {
			answer[i] = v - 1 + '0', minimum = v - 1;
			for(int j = i + 1; j < n; ++j) answer[j] = '9';
		}
	}
	int start = 0;
	while(n - start > 1 && answer[start] == '0') ++start;
	return answer + start;
}

int main() {
	for(int cases = getint(), idx = 1; idx <= cases; ++idx) {
		printf("Case #%d: ", idx);
		scanf("%s", data);
		cout << solve() << endl;
	}
	return 0;
}

