/*
	By: facug91
	From: 
	Name: 
	Date: 21/04/2017
*/

#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
#define endl "\n"
#define EPS 1e-9
#define MP make_pair
#define F first
#define S second
#define prev bjasdbi132ge79qwgdi
#define next usayhkdgisaydgiy212
#define move sdjifha978dyd9sag89
#define DB(x) cerr << " #" << (#x) << ": " << (x)
#define DBL(x) cerr << " #" << (#x) << ": " << (x) << endl
const double PI = acos(-1.0);

#define INF 1000000000
//#define MOD 100000007
#define MAXN 1000

using namespace std;
//using namespace __gnu_pbds;

typedef long long ll;
typedef unsigned long long llu;
typedef pair<ll, ll> ii; typedef pair<ii, int> iii; typedef pair<ii, ii> iiii;
typedef vector<int> vi; typedef vector<ii> vii; typedef vector<iiii> viiii;
//typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set; //insert, find_by_order, order_of_key, erase

int n, r, o, y, g, b, v, c[3];

int main () {
	#ifdef ONLINE_JUDGE
		ios_base::sync_with_stdio(0); cin.tie(0);
	#endif
	cout<<fixed<<setprecision(9); cerr<<fixed<<setprecision(9); //cin.ignore(INT_MAX, ' '); //cout<<setfill('0')<<setw(9)
	int i, j;
	
	int tc;
	cin >> tc;
	for (int it=1; it<=tc; it++) {
		cout << "Case #" << it << ": ";
		cin>>n>>r>>o>>y>>g>>b>>v;
		c[0] = b-o;
		c[1] = y-v;
		c[2] = r-g;
		sort(c, c+3);
		if ((o > 0 && b <= o) || (v > 0 && y <= v) || (g > 0 && r <= g) || c[2] > c[1]+c[0]) {
			if (o > 0 && b == o && v + y + g + r == 0) {
				for (i=0; i<b; i++) cout << "BO";
				cout << endl;
			} else if (v > 0 && y == v && o + b + g + r == 0) {
				for (i=0; i<y; i++) cout << "YV";
				cout << endl;
			} else if (g > 0 && r == g && v + y + o + b == 0) {
				for (i=0; i<r; i++) cout << "RG";
				cout << endl;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
			continue;
		}
		
		map<char,string> special_case;
		
		special_case['B'] = "B";
		for (i=0; i<o; i++) special_case['B'] += "OB";
		
		special_case['R'] = "R";
		for (i=0; i<g; i++) special_case['R'] += "GR";
		
		special_case['Y'] = "Y";
		for (i=0; i<v; i++) special_case['Y'] += "VY";
		
		vector<pair<int, char>> aux;
		aux.emplace_back(b-o, 'B');
		aux.emplace_back(y-v, 'Y');
		aux.emplace_back(r-g, 'R');
		
		sort(aux.begin(), aux.end(), greater<pair<int, char>>());
		char last = 'Z';
		char first = aux[0].S;
		aux[0].F++;
		while (aux[0].F + aux[1].F + aux[2].F > 0) {
			if (aux[0].F == 1 && aux[0].S == first) aux[0].F--;
			else {
				if (last != aux[0].S) {
					cout<<special_case[aux[0].S];
					special_case[aux[0].S] = aux[0].S;
					aux[0].F--;
					last = aux[0].S;
				} else {
					if (aux[1].F == 1 && aux[1].S == first) aux[1].F--;
					else {
						cout<<special_case[aux[1].S];
						special_case[aux[1].S] = aux[1].S;
						aux[1].F--;
						last = aux[1].S;
					}
				}
			}
			sort(aux.begin(), aux.end(), greater<pair<int, char>>());
		}
		cout<<endl;
		
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
