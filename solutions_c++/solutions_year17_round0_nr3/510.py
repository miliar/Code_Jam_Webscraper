#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <iomanip>
#include <map>
#include <string>
#define INF 1000000000
#define HAND_TYPE 1
#define TEST 10
#define SMALL 100
#define LARGE 1000
#define INPUT_SITUATION LARGE
#define MAKE_OUTFILE
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
int T,ans;
u64 N,K,m,M;
void getSol(u64 n, u64 k, u64 &maxi, u64 &mini) {
	u64 a = (n-1)/2, b = n-1-a;
	if (k-- == 1) {
		maxi = b;
		mini = a;
		return;
	}
	if (k%2) {
		getSol(b, k-k/2, maxi, mini);
	}
	else {
		getSol(a, k/2, maxi, mini);
	}
	return;
}

int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("C-small2.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("C-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output2.txt","w",stdout);
	#endif
	cin >> T;
	for (int cas=0; cas<T; cas++) {
		cin >> N >> K;
		getSol(N,K,M,m);
		cout << "Case #" << cas+1 << ": " << M << ' ' << m << '\n';
	}
	return 0;
}
