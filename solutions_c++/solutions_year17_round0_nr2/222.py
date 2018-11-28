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

int is(long long x) {
	if(x < 10) return x;
	int tmp = is(x / 10), now = x % 10;
	if(tmp == -1 || tmp > now) return -1;
	return now;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc) {
		long long a[20], x, tmp;
		cin >> x;
		int f = 0;
		memset(a, 0, sizeof(a));
		{
			tmp = x;
			while(tmp) {
				a[f++] = tmp % 10;
				tmp /= 10;
			}
			tmp = 1;
			for(int i = 0; i < f; ++i){
				a[i] *= tmp;
				tmp *= 10;
			}
			a[f - 1]--;
			for(int i = f - 2; i >= 0; --i){
				a[i] += a[i + 1];
			}
		}
		long long ans = 0;
		for(int i = 0; i < f; ++i) {
			if(is(a[i]) != -1) {
				ans = max(ans, a[i]);
			}
		}
		if(is(x) != -1) ans = x;
		cout<<"Case #"<<cc<<": "<<ans<<endl;
	}
	return 0;
}

