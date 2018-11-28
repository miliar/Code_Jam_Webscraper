//no comment needed
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <string.h>
#include <strings.h>
#include <math.h>
#include <time.h>
#include <map>
#include <climits>
using namespace std;

//Two of the most frequently used typical of long names, make life easier
typedef vector<int> VI;
typedef long long LL;

/* Loops */
// FOR - loop increasing 'x' from 'b' to 'e' inclusive
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
// FORD - loop decreasing 'x' from 'b' to 'e' inclusive
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
// REP - loop increasing 'x' from '0' to 'n'. Used to search and build DS
#define REP(x, n) for(int x = 0; x < (n); ++x)
// Clone long type of 'n'
#define VAR(v, n) __typeof(n) v = (n)
// ALL(c) represents the pair of iterators, indicating begin-end elements in the STL DS
#define ALL(c) (c).begin(), (c).end()
// Macro to get size of STL DS, used to avoid compilation warrning with int and uint comp
#define SIZE(x) ((int)(x).size())
// Very profitable macro aimed to iterate through all elements of STL DS
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
// Simple contain:
#define CONTAINS( v, x ) ( std::find(v.begin(), v.end(), x) != v.end() )
// Contain using binary search VI have to be sorted!
#define BCONTAINS( v, x) ( std::binary_search(v.begin(), v.end(), x) != v.end() )

/* Shortcuts for vectors most common use cases*/
#define PB push_back
#define POP pop_back
#define ST first
#define ND second
#define RM( v, x )  v.erase(v.begin() + x)
#define PF( v, x )  v.insert(v.begin(), x);
#define FIND(v, x)  find(v.begin(), v.end(), x)
#define Vit         std::vector<int>::iterator

/* some other usefull methods */
#define INF     INT_MAX/2-256
#define _il     inline
#define _ili    inline int
#define _ilv    inline void

#define IN      "in"
#define OUT     "out"
#define ERR     "err"

_ilv sol(int tc, int N, int K);
//debug print
void print_v(VI v){
fprintf(stderr, "vec:: ");
    FOREACH(it, v)
        fprintf(stderr, "%d, ", *it);
fprintf(stderr, "\n");
}

int main(){
    //sample
    freopen(IN,  "r", stdin);
//    freopen(OUT, "w", stdout);
//    freopen(ERR, "w", stderr);

    int TT; cin >> TT;

    REP(tt, TT){
        int N, K;
        cin >> N >> K;

        sol(tt+1, N, K); //run sol
    }

    return 0;
}

_ilv sol(int tc, int N, int K)
{
//cout << "-----------------------------------" << endl;
	vector<pair<int, int> > pair(N);
	VI val(N);
	VI occ(N, 0);
	int last = -1;
REP(x, K) {
	VI vmax;
	int l = -1;
	int max = 0;
	pair.clear();
	for(int i=0; i<N; i++){
		int r = N;
		if(occ[i] == 0){
			for(int j=i; j<N; j++)
				if(occ[j] == 1) { r = j; break;}
			pair[i].first = abs(i-l-1); pair[i].second = abs(r-i-1);
			val[i] = min(abs(i-l-1), abs(r-i-1));
			max = std::max(val[i], max);
			
//			cout << "## i: " << i << " L:" << l << " R:" << r << " val[i]:"<< val[i] << endl;
//			cout << "## Lval:abs(i-l-1)-> " << abs(i-l-1) << " Rval:abs(r-i-1)-> " << abs(r-i-1) << endl;
		} else {
			l = i;
		}
	}
/*	for(int i=0; i<N; i++)
		cout << val[i] << ",";
	cout << endl;
*/
	for(int i=0; i<N; i++)
		if(occ[i] == 0 && val[i] == max)
			vmax.PB(i);
//cout << "VMAX: " ;
//for(int i=0; i<vmax.size(); i++)
//	cout << vmax[i] << ",";
//cout << endl;

	if(vmax.size() == 1) {
		occ[vmax[0]] = 1;
		last = vmax[0];
	} else {
		int mmx = -1;
		for(int i=0; i<vmax.size(); i++){
			int sum = pair[vmax[i]].first + pair[vmax[i]].second;
			if(sum > mmx){
//				cout << "II: " << i << endl;
				mmx = sum;
				last = vmax[i];
			}
		}
		occ[last] = 1;
	}
//	cout << "## LAST = " << last << endl;
//	for(int i=0; i<N; i++)
//		cout << "(" << pair[i].first <<"," << pair[i].second <<"),";
//	cout << endl;
//	for(int i=0; i<N; i++)
//		if(occ[i]==0) cout << ". ";
//		else cout << "O ";
//	cout << endl;

}
	cout << "Case #"<<tc<<": " << pair[last].second << " " << pair[last].first  << endl; 
}
