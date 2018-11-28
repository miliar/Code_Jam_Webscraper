#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <set>
#include <utility>
#include <algorithm>
#include <ctime>
using namespace std;

int const MAX_N = 1024 * 1024;
int const MAX_CH = 5000010;
int const INT_INF = 1000000000;

char st[MAX_CH];
double our_t[MAX_N];

struct pp {long long init, speed;} ms[MAX_N];

bool operator < (const pp &A, const pp &B) {
	return A.init < B.init || (A.init == B.init && A.speed > B.speed);
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	gets(st);
	sscanf(st,"%d",&tt);
	for (int qq=0; qq<tt; qq++) {
		long long DST;
		int n;
		scanf("%lld%d",&DST,&n);

		for (int i=0; i<n; i++) scanf("%lld%lld",&ms[i].init,&ms[i].speed);
		sort(ms,ms+n);

		our_t[n-1] = (DST - ms[n-1].init) / ((double) ms[n-1].speed);

		for (int i=n-2; i>=0; i--) {
			our_t[i] = -1e100;
			for (int j=i+1; j<n; j++)
				if (ms[i].speed > ms[j].speed)
					our_t[i] = max(our_t[i], our_t[j]);
			our_t[i] = max(our_t[i], (DST - ms[i].init) / ((double) ms[i].speed));
		}

		double mx = -1e100;
		for (int i=0; i<n; i++) mx = max(mx, our_t[i]);
				
		printf("Case #%d: ",qq+1);
		printf("%.15lf", DST / mx);
		printf("\n");
	}
	
	return 0;
}