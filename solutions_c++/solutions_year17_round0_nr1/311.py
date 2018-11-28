#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

const int Maxs = 1005;

int t;
char s[Maxs];
int slen;
int k;

int Check()
{
	int res = 0;
	for (int i = 0; i < slen; i++) if (s[i] == '-')
		if (i + k <= slen) {
			res++;
			for (int j = i; j < i + k; j++)
				s[j] = s[j] == '+'? '-': '+';
		} else return -1;
	return res;
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%s", s); slen = strlen(s);
		scanf("%d", &k);
		int res = Check();
		printf("Case #%d: ", tc);
		if (res == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	return 0;
}