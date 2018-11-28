#include <algorithm>
#include <bitset>
#include <cassert>
#include <deque>
#include <queue>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <float.h>
#include <limits>
#include <list>
#include <map>
#include <math.h>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<unsigned> vu;
typedef vector<ll> vl;
typedef vector<pi> vp;
typedef vector<string> vs;
typedef set<int> si;
typedef map<int, int> mi;

#define MAXD 1e12
int N, Q;
vector<double> s;
vector<double> e;
vector<int> u, v;
vector<bool> done;
vector < pair<int, double> > adj[100];

double getMin(int i, int j, int prev, double distDone){
	if(i==j) return 0;
	double minT = MAXD;
	for( int k=0; k<adj[i].size(); k++){
		int m = adj[i][k].first;
		if ( done[m] ) continue;	
		done[m] = 1;

		double d = adj[i][k].second;
		if(prev != -1 && e[prev] >= d + distDone )
			minT = min(minT, d/s[prev]  + getMin(m, j, prev, d + distDone) );

		if( e[i] >= d  )
			minT = min( minT,  d/s[i] +  getMin(m, j, i, d) );

		done[m] = 0;
	}
	return minT;
}

int main(){
    int t;
    cin >> t;
    for(int Case=1; Case<=t; Case++){
        cin >> N >> Q;
        s.resize(N);
        e.resize(N);
        done.resize(N);
        u.resize(Q);
        v.resize(Q);

        for( int i=0; i<N; i++){
        	cin >> e[i] >> s[i];
        	done[i] = 0;
        	adj[i].resize(0);
        }
        int x, y;
        double d;
        for( int i=0; i<N; i++){
        	for( int j=0; j<N; j++){
        		cin >> d;
        		if(d > 0 )
        			adj[i].push_back( make_pair(j, d) );
        	}
        }
        for(int i=0; i<Q; i++){
        	cin >> x >> y;
        	x--; y--;
        	u[i] = x;
        	v[i] = y;
        }
        cout << "Case #" << Case << ": ";
        for( int i=0; i<Q; i++){
        	done[u[i]] = 1;
        	//cout << u[i] << " to " << v[i] << endl;
        	printf("%.6f", getMin(u[i], v[i], -1, 0));
        	done[u[i]] = 0;
        	cout << " ";
        }
        cout << endl;
    }
    return 0;
}