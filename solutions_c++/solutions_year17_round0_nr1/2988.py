#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

char buffer[N];
char ans[N];

void test()
{
	vector<bool> cakes;
	int n, k;
	scanf("%s%d", buffer, &k);
	n = strlen(buffer);
	cakes.resize(n);
	for (int i = 0; i < n; i ++) {
		cakes[i] = (buffer[i] == '+');
	}
	int ile = 0;
	for (int i = 0; i < n; i ++) {
		if (!cakes[i]) {
//			fprintf(stderr, "flip %d\n", i);
			if (i + k > n) {
				sprintf(ans, "IMPOSSIBLE");
				return;
			}
			ile ++;
			for (int j = 0; j < k; j ++) {
				cakes[i + j] = !cakes[i + j];
			}
		}
	}
	sprintf(ans, "%d", ile);
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		test();
		printf("Case #%d: %s\n", i, ans);
	}
}
