#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc) {
		double d, t;
		int n;
		cin >> d >> n;
		{
			int k, s;
			scanf("%d%d", &k, &s);
			t = (d - k) / s;
		}
		for(int i = 1; i < n; ++i)
		{
			int k, s;
			scanf("%d%d", &k, &s);
			t = max(t, (d - k) / s);
		}
		printf("Case #%d: %.10f\n", cc, d / t);
	}
	return 0;
}

