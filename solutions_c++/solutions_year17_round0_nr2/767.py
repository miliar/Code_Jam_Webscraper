#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
#define mi ((l+r)>>1)
#define fk puts("fuck!")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

char str[107];

int main()
{
	int T; scanf("%d",&T);
	for(int cas=1; cas<=T; ++cas) {
		scanf("%s", str);
		int la = strlen(str) - 1;
		for(int i=la; i>=1; --i)
			if(str[i-1] > str[i]) {
				str[i-1]--;
				for(int j=i; j<=la; ++j)
					str[j] = '9';
			}
		printf("Case #%d: %s\n", cas, str[0]=='0' ? str+1 : str);
	}
	return 0;
}





