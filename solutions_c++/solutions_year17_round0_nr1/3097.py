#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string.h>

#include <vector>
#include <limits>
#include <queue>
#include <cstdlib>
#include <map>
#include <math.h>
#include <limits>
#include <time.h>
#include <bitset>
#include <set>
#include <stack>
#include <complex>
#include <ctime>
using namespace std;
#define ll long long

#define endl '\n'

char cad[10000];
bool val[1000];
int len, k;

void solve() {
	scanf("%s%d",cad,&k);
	len = strlen(cad);
	for(int i=0;i<len;i++) val[i] = (cad[i] == '+');

	int ans = 0;
	for(int i=0;i+k<=len;i++) {
		if (val[i]) continue;
		ans++;
		for(int j=i;j<i+k;j++) val[j] ^= 1;
 	}

	bool ok = true;
	for(int i=0;i<len;i++) ok &= val[i];
	if (ok)
		printf("%d\n", ans);
	else
		printf("IMPOSSIBLE\n");
}

int main(){
	//freopen("/Users/jcfernandez/Downloads/CodeJam/input.txt", "r", stdin);
	//freopen("/Users/jcfernandez/Downloads/CodeJam/output.txt", "w", stdout);

	int cas, caso = 1;
	scanf("%d", &cas);
	while(cas--) {
		printf("Case #%d: ", caso++);
		solve();
	}
	return 0;
}
