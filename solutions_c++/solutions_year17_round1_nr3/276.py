#include "bits/stdc++.h"
#include <sys/timeb.h>
#include <fstream>

using namespace std;

#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define replrev(i,a,b) for(int i=(int)(b)-1;i>=(int)(a);i--)
#define reprev(i,n) replrev(i,0,n)
#define repi(itr,ds) for(auto itr = ds.begin(); itr != ds.end(); ++itr)
#define mp make_pair
#define INF 2000000000
#define INFL 2000000000000000000LL
#define EPS 1e-9
#define MOD 1000000007
#define PI 3.1415926536
#define RMAX 4294967295

typedef long long ll;
typedef pair<int, int> P;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<bool> vb;
typedef vector<char> vc;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<P> vP;
typedef vector<vector<int> > vvi;
typedef vector<vector<bool> > vvb;
typedef vector<vector<ll> > vvll;
typedef vector<vector<char> > vvc;
typedef vector<vector<double> > vvd;
typedef vector<vector<P> > vvP;
typedef priority_queue<int, vector<int>, greater<int> > pqli;
typedef priority_queue<ll, vector<ll>, greater<ll> > pqlll;
typedef priority_queue<P, vector<P>, greater<P> > pqlP;
typedef pair<int, pair<int, int> > Edge;
typedef vector<Edge> vE;
typedef priority_queue<Edge, vector<Edge>, greater<Edge> > pqlE;


//#define DEBUG

#ifdef DEBUG
#define dprintf printf
#define dbg 
#define drepl(i,a,b) repl(i,a,b)
#define drep(i,n) rep(i,n)
#else
#define dprintf (true)?0:printf
#define dbg if(false)
#define drepl(i,a,b) int i; if(false)
#define drep(i,n) int i; if(false)
#endif // DEBUG



int main() {
	ifstream ifs("C1.in");
	ofstream ofs("C1.txt");

	int T;
	ifs >> T;
	rep(t, T) {
		int Hd, Ad, Hk, Ak, B, D;
		ifs >> Hd >> Ad >> Hk >> Ak >> B >> D;
		int maxd = 0, maxb = 0;
		if (D != 0) maxd = (int)(ceil((double)Ak / D) + 0.5);
		if (B != 0) maxb = (int)(ceil((double)(Hk - Ad) / B) + 0.5);
		int minturn = INF;
		bool impossible = true;

		rep(d, maxd + 1) {
			rep(b, maxb + 1) {
				int hd = Hd, ad = Ad, hk = Hk, ak = Ak;
				int numd = d, numb = b, turn = 0;
				bool lose = false, cure = false;

				while (hk > 0) {
					if ((numd > 0 && hd <= ak - D) 
							|| (numd == 0 && numb > 0 && hd <= ak) 
							|| (numd == 0 && numb == 0 && hk > ad && hd <= ak)) {
						// Cure
						if (cure) {
							// Cure2˜A‘±
							lose = true;
							break;
						}
						hd = Hd;
						cure = true;
					}
					else if (numd > 0) {
						// Debuff
						ak = max(ak - D, 0);
						numd--;
						cure = false;
					}
					else if (numb > 0) {
						// Buff
						ad += B;
						numb--;
						cure = false;
					}
					else {
						// Attack
						hk -= ad;
						cure = false;
					}
					hd -= ak;
					if (hk > 0 && hd <= 0) {
						lose = true;
						break;
					}
					turn++;
				}
				if (!lose) {
					impossible = false;
					minturn = min(minturn, turn);
				}
			}
		}

		if (impossible) {
			ofs << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			ofs << "Case #" << t + 1 << ": " << minturn << endl;
		}
	}

	return 0;
}