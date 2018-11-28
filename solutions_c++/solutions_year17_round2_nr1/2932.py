#include <bits/stdc++.h>
#define lli long long int
#define ulli unsigned long long int
#define DEBUG(A); cout << "[DEBUG] " << (#A)  << " = " << (A) << endl;
#define INF (int)1e9
#define EPS 1e-9
#define fill(a,v) memset(a, v, sizeof a)
#define MAX(a,b)                     ( (a) > (b) ? (a) : (b))

using namespace std;

int D, N, K, S;
double maxtime;
double thistime;
double resp;

void process() {
	resp = (double) D/maxtime;
}

int main() {
	int tc, t;
	cin >> t;
	//ios_base::sync_with_stdio(false); 
	for(tc=1; tc <= t; ++tc) {
		cin >> D >> N;
		maxtime = 0;
		
		for(int i=0;i<N;++i) {
			cin >> K >> S;
			thistime = ((double) (D-K))/S;
			maxtime = MAX(maxtime, thistime);
		}
 
		process();
 
		cout << "Case #" << tc << ": " << setprecision(6) << fixed << resp << endl;
	}
	return 0;
}