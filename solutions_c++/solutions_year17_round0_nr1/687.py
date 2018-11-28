#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 1010;

char st[MAX_N];
int k;
int n;

//flip [l,r)
void flip(char* st, int l, int r) {
	for (int i = l; i < r; i++) {
		if (st[i] == '-')
			st[i] = '+';
		else
			st[i] = '-';
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	int case_num = 0;
	while (t--)
	{
		case_num++;
		printf("Case #%d: ", case_num);
		scanf("%s", st);
		n = strlen(st);
		scanf("%d", &k);
		int ans = 0;
		for (int i = 0; i <= n - k; i++) {
			if (st[i] == '-') {
				flip(st, i, i + k);
				ans++;
			}
		}
		if (find(st, st + n, '-') != st + n) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
