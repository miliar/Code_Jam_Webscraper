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

struct nod{
	long long x;
	long long cnt;
};

nod a[100000];
int f = 0;
void add(long long x, long long y) {
	if (f && a[f - 1].x == x) {
		a[f - 1].cnt += y;
	} else {
		a[f].x = x;
		a[f].cnt = y;
		f++;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc) {
		f = 0;
		int r = 0;
		long long n, k;
		cin >> n >> k;
		add(n, 1);
		long long ans = n;
		while(k > 0) {
			k -= a[r].cnt;
			ans = a[r].x;
			add(a[r].x / 2, a[r].cnt);
			add((a[r].x - 1) / 2, a[r].cnt);
			r++;
		}
		cout<<"Case #"<<cc<<": "<<ans / 2<<" "<<(ans - 1) / 2<<endl;
	}
	return 0;
}

