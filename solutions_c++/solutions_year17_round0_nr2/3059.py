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

char cad[100];
int dig[100];
int len;

void menor() {
	for(int i=1;i<len;i++) printf("9");
	printf("\n");
}

bool dfs() {
	int pos = 0;
	while (pos + 1 < len && dig[pos] <= dig[pos + 1])
		pos++;
	if (pos == len - 1) return true;

	while (pos >= 0 && dig[pos] == 0) pos--;
	if (pos == -1 || (pos == 0 && dig[pos] == 1)) return false;

	dig[pos]--;

	for(int i=pos + 1 ;i<len;i++) dig[i] = 9;
	return dfs();
}

void solve() {
	scanf("%s", cad);
	len = strlen(cad);
	for(int i=0;i<len;i++) dig[i] = cad[i] - '0';

	if (dfs()) {
		for(int i=0;i<len;i++) printf("%d", dig[i]);
		printf("\n");
	} else {
		menor();
	}
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
