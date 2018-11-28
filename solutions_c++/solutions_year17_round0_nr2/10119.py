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

_ilv sol(int tc, string N);
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
        string N;
        cin >> N;

        sol(tt+1, N); //run sol
    }

    return 0;
}

_ili precheck(string N){
	int result = -1;
	for(int i=1; i<N.length(); i++){
		if(!(N[i] >= N[i-1])) {
			return -1;
		}
	}
	return 0;
}
_ili check_increasing(string N){
	int result = -1;
	for(int i=1; i<N.length(); i++){
		if(!(N[i] > N[i-1])) {
			result = i-1;
			break;
		}
	}
	return result;
}

_ilv sol(int tc, string N )
{
	if(precheck(N) == 0){
		cout << "Case #"<<tc << ": " << N << endl;
		return;
	}
	int index = check_increasing(N);
	N[index] = N[index]-1;
	for(int i=index+1; i<N.length(); i++)
		N[i] = '9';

	int zeros = 0;
	while(N[zeros]=='0')
		zeros++;

	if(zeros)
		N.erase(0,zeros);
	cout << "Case #"<<tc << ": " << N << endl;
	return;
}
