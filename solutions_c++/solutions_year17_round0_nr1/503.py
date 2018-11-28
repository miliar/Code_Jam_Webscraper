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
string s;
int N,K;
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("A-small.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("A-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output.txt","w",stdout);
	#endif
	cin >> T;
	for (int cas=0; cas<T; cas++) {
		cin >> s;
		N = s.length();
		cin >> K;
		cout << "Case #" << cas+1 << ": ";
		ans = 0;
		for (int i=0; i<N-K+1; ++i) {
			if (s[i] == '+') continue;
			++ans;
			for (int j=i; j<i+K; ++j) 
				s[j] = (s[j] == '+') ? '-' : '+';
		}
		for (int i=N-K+1; i<N; ++i)
			if (s[i] == '-') 
				goto skip;
		cout << ans << "\n";
		continue;
skip: cout << "IMPOSSIBLE\n";	
	}
	return 0;
}
