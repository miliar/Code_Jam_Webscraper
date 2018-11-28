#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;
typedef long long LL;
#define For(i,a,b) for (int i = (a); i <= (b); i++)
#define Cor(i,a,b) for (int i = (a); i >= (b); i--)
#define rep(i,a) for (int i = 0; i < a; i++)
#define Fill(a,b) memset(a,b,sizeof(a))
char s[100];
void solve()
{
	scanf("%s", s);
	int n = strlen(s);
	for (int i = n - 1; i > 0; i--)
	{
		if (s[i] >= s[i - 1])
			continue;
		s[i - 1] -= 1;
		for (int j = i; j < n; j++)
			s[j] = '9';
	}
	for (int i = 0; i < n; i++)
		if (s[i] != '0')
			printf("%c", s[i]);
	printf("\n");
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int _;
	scanf("%d", &_);
	for (int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
