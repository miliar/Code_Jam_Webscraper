#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long int ll;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
#define present(c,e) ((c).find(e) != (c).end())
#define cpresent(c,e) (find(all(c),e) != (c).end())
#define REP(i,a,b) for(int i=int(a); i<=int(b); i++)
#define mp make_pair
#define ff first
#define ss second

int main() {
	int T;
	cin >> T;
	REP(caseno,1,T) {
		cout << "Case #" << caseno << ": ";
		int D, N;
		cin >> D >> N;
		vector<pair<double, double> >horse(N);
		REP(i, 0, N-1) {
			cin >> horse[i].ff >> horse[i].ss;
		}
		sort(all(horse));
		double critical_distance = horse[0].ff;
		double cricitcal_speed = horse[0].ss;
		for (int i = N-2; i >= 0; i--) {
			double s1 = horse[i].ss, s2 = horse[i+1].ss, p1 = horse[i].ff, p2 = horse[i+1].ff;
			if (s1 > s2) {
				double x = (s2*p1 - s1*p2)/(s2 - s1);
				if (x <= D) {
					horse[i].ff = x;
					horse[i].ss = s2;
					critical_distance = x;
					cricitcal_speed = s2;
				}
			}
		}
		// REP(i, 0, N-1) {
		// 	cout << horse[i].ff << " " << horse[i].ss << "\n";
		// }
		sort(all(horse));
		double ans = (double)D*horse[0].ss/(D-horse[0].ff);
		printf("%.6lf\n", ans);
	}
	return 0;
}