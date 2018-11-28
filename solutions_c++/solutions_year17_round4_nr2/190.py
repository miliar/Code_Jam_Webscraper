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
int T,ans,N,C,M;
int P[1000], B[1000];
int person[1000], position[1000];
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("B-small.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("B-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output_large.txt","w",stdout);
	#endif
	cin >> T;
	for (int cas=0; cas<T; cas++) {
		cin >> N >> C >> M;
		for (int i=0; i<C; ++i)
			person[i] = 0;
		for (int i=0; i<N; ++i)
			position[i] = 0;
		for (int i=0; i<M; ++i) {
			cin >> P[i] >> B[i];
			P[i]--; B[i]--;
			person[B[i]]++;
			position[P[i]]++;
		}
		cout << "Case #" << cas+1 << ": ";
		int R = 0;
		for (int i=0; i<C; ++i)
			if (person[i] > R)
				R = person[i];
		int s = 0;
		for (int i=0; i<N; ++i) {
			s += position[i];
			while (s > (i+1)*R) 
				++R;
		}		
		int x = 0;
		for (int i=1; i<N; ++i)
			if (position[i] > R)
				x += position[i]-R;
		cout << R << ' ' << x << '\n';
	}
	return 0;
}
