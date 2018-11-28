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
int N,P;
int R[50];
int Q[50][50];
int minserv[50][50], maxserv[50][50];
int ptrs[50];
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("B-small.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("B-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output.txt","w",stdout);
	#endif
	cin >> T;
	set<int> v;
	bool win;
	for (int cas=0; cas<T; cas++) {
		ans = 0;
		cin >> N >> P;
		for (int i=0; i<N; ++i)
			cin >> R[i];
		for (int i=0; i<N; ++i)
			for (int j=0; j<P; ++j)
				cin >> Q[i][j];
		v.clear();
		for (int i=0; i<N; ++i) {
			for (int j=0; j<P; ++j) {
				maxserv[i][j] = (10*Q[i][j])/(9*R[i]);
				if ((10*Q[i][j])%(11*R[i]) == 0) 
					minserv[i][j] = (10*Q[i][j])/(11*R[i]);
				else 
					minserv[i][j] = (10*Q[i][j])/(11*R[i])+1;
				v.insert(minserv[i][j]);
				v.insert(maxserv[i][j]);
			}
			sort(minserv[i], minserv[i]+P);
			sort(maxserv[i], maxserv[i]+P);
			ptrs[i] = 0;
		}
		/*cout << "minvals:\n";
		for (int i=0; i<N; ++i) {
			for (int j=0; j<P; ++j) {
				cout << minserv[i][j] << ' ';
			}
			cout << endl;
		}
		cout << "maxvals\n";
		for (int i=0; i<N; ++i) {
			for (int j=0; j<P; ++j) {
				cout << maxserv[i][j] << ' ';
			}
			cout << endl;
		}*/
		for (auto it=v.begin(); it!=v.end(); ++it) {
			for (int i=0; i<N; ++i) {
				while (ptrs[i] < P && maxserv[i][ptrs[i]] < *it)
					ptrs[i]++;
				if (ptrs[i] == P)
					goto done;
			}
			/*cout << "target = " << *it << ": avail = ";
			for (int i=0; i<N; ++i) {
				cout << '[' << minserv[i][ptrs[i]] << ',' << maxserv[i][ptrs[i]] << "]; ";
			}
			cout << endl;*/
			do {
				win = 1;
				for (int i=0; i<N; ++i) {
					if (minserv[i][ptrs[i]] > *it) {
						win = 0;
						break;
					}
				}
				if (win) {
					ans++;
					for (int i=0; i<N; ++i) {
						ptrs[i]++;
						if (ptrs[i] == P)
							goto done;
					}
				}
			} while (win);
		}
		done:;
		cout << "Case #" << cas+1 << ": " << ans << '\n';
	}
	return 0;
}
