/* g++ -std=c++14 */

/* standard things */
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

/* std io */
#include <iostream>
#include <sstream>

/* useful std stuff */
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <unordered_map>
#include <unordered_set>
#include <limits>

/* useful defines */
using namespace std;

#define forn(i, n) for (decltype(n) i = 0; i < n; i++)
#define for1(i, n) for (decltype(n) i = 1; i <= n; i++)
#define forr(i, n) for (decltype(n) i = n; i-- > 0; )

typedef long long int lli;
typedef unsigned long long int ulli;
typedef long double lld;

int ki[1009];
int si[1009];

struct horse {
	int k;
	int s;
};

vector<struct horse> h;

lld will_catch(struct horse a, struct horse b){
	lld eps = std::numeric_limits<lld>::epsilon();

//	cerr << "eps: " <<  eps << endl;

	if (a.k > b.k)
		swap(a, b);

	return ( lld(b.k - a.k) / lld(a.s - b.s) );
}

lld hhh_t[1009];
lld hhh_s[1009];
int hhh_n;

typedef struct {
	lld t;
	lld s;
} ultih;

void solve_testcase(int casenum)
{

	int d, n;
	cin >> d >> n;
	h.resize(n);
	forn(i, n){
	//	cin >> h[i].k >> h[i].s;
		scanf("%d%d", &h[i].k, &h[i].s);
	}

	sort(h.begin(), h.end(), [](struct horse& a, struct horse& b){
				return a.k < b.k;
			});
/*
	forn(i, h.size()){
		cerr << h[i].k << " " << h[i].s << ", ";
	}
	cerr << endl;
*/	
	
	int iii = h.size() - 1;
	vector<ultih> hhh;
	vector<struct horse> hh;

	ultih el;
	el.t = 0.0;
	el.s = lld(h[iii].s);
	hhh.push_back(el);
	hh.push_back(h[iii]);
	iii--;

	while(iii >= 0) {
//		cerr << "in loop" << endl;
		lld tc = -1.0;
		int jjj = iii + 1;
		while (tc < 0.0 && jjj < n){
			tc = will_catch(h[iii], h[jjj]);
			jjj++;
		}

//		cerr << tc << " " << h[iii].k << " " << h[iii].s << endl;
		if (tc > lld(0.0)){
			// add p
			ultih eel;
			eel.t = lld(tc); 
			eel.s = lld(h[jjj - 1].s);
			hh.push_back(h[iii]);
			hhh.push_back(eel);
		} else {
			// reset
			hhh.clear();
			hh.clear();
			ultih eel;
			eel.t = lld(0.0); 
			eel.s = lld(h[iii].s);
			hh.push_back(h[iii]);
			hhh.push_back(eel);
		}
		iii--;
	}

//	cerr << hh[0].k << " " << hh[0].s << endl;	
	lld ov_time = lld(d - hh[0].k) / lld(hh[0].s);
	lld ov_speed = lld(d) / lld(ov_time);


//	cerr << hh.size() << " " << (d - hh.back().k) << " "<<h.back().s<< " "  << ov_time << " " << ov_speed << endl;

//	cout << "Case #" << casenum << ": " << ov_speed << std::edl;
	printf("Case #%d: %.6Lf\n", casenum, ov_speed);
}


void solve2(int casenum){
	int d, n;
	cin >> d >> n;
	h.resize(n);
	forn(i, n){
		cin >> h[i].k >> h[i].s;
	}

	struct horse hhh = *min_element(h.begin(), h.end(), [=](struct horse& a, struct horse& b){
				lld ta = lld(d - a.k)/lld(a.s);
				lld tb = lld(d - b.k)/lld(b.s);
				return ta > tb;
			});

	lld ov_time = lld(d - hhh.k) / lld(hhh.s);
	lld ov_speed = lld(d) / lld(ov_time);

	printf("Case #%d: %.6Lf\n", casenum, ov_speed);

}

int main()
{	
	int total_casenum;
	scanf("%d", &total_casenum);
//	cin >> total_casenum;

	for1(T, total_casenum)
	//	solve_testcase(T);
		solve2(T);

	return 0;
}
