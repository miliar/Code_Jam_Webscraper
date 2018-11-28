#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef long long ll;

#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d%d", &x, &y)
#define FOR(i,S,E) for(int i=S; i<E; i++)
#define fst first
#define snd second
#define pb push_back

const double EPS = 0.000001;

int main () {
	int T; ri(T);
	FOR(t,1, T+1) {
		int D, N; rii(D, N);
		vector<pair<double, double> > H;
		FOR(i,0,N) {
			int K, S; rii(K,S);
			H.pb({K,S});
		}
		sort(H.begin(), H.end());
		vector<double> time; time.resize(N);
		double K = H[N-1].fst, V = H[N-1].snd;
		time[N-1] = (D-K)/V;
		
		for(int i=N-2; i>-1; i--) {
			K = H[i].fst; V = H[i].snd;
			double K1 = H[i+1].fst, V1 = H[i+1].snd;
			
			double colisionTime = (K1-K)/(V-V1),
				colision = K + V*colisionTime;
			if ((colision > D && abs(colision - D) > EPS) || colisionTime < 0) {
				time[i] = (D-K)/V;
			}
			else {
				time[i] = time[i+1];
			}
		}
		printf("Case #%d: %lf\n", t, D/time[0]);
	}
}
