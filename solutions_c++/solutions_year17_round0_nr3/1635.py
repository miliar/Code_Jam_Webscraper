#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cassert>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

typedef vector<int> IntVec;
typedef long long ll;
typedef unsigned long long ull;

template<class T, class T1, class T2> inline bool Within(T x, T1 xMin, T2 xMax)
    {return (x >= xMin && x <= xMax);}
template<class T, class T1> inline bool Within(T x, T1 xMax)
    {return (x >= 0 && x < xMax);}

template<class T> void PrintVec(const vector<T>& v, const char* s=NULL) {
    if (s)
	cout << s << ' ';
    forall (i, v.size())
	cout << v[i] << ' ';
    cout << endl;
}

template<class T> void PrintVec(const char* s, const vector<T>& v) {
    PrintVec(v, s);
}

void MaxMin(ull& maxDist, ull& minDist, ull nStalls, ull nMen) {
    while (nMen > 1) {
	if (nMen % 2 == 0)
	    nStalls /= 2;
	else
	    nStalls = (nStalls - 1) / 2;
	nMen /= 2;
    }
    maxDist = nStalls / 2;
    minDist = (nStalls - 1) / 2;
}

void MaxMinSimple(ull& maxDist, ull& minDist, ull nStalls, ull nMen) {
    vector<bool> vb(nStalls, false);
    forall (iMan, nMen) {
	vector<int> dl(nStalls), dr(nStalls);
	int d=0;
	forall (i, nStalls) {
	    if (vb[i])
		d=0;
	    else
		++d;
	    dl[i] = d;
	}
	d=0;
	for (int i=nStalls-1; i>=0; i--) {
	    if (vb[i])
		d=0;
	    else
		++d;
	    dr[i] = d;
	}
	int iBest = nStalls;
	forall (i, nStalls) {
	    const ull mind = min(dl[i], dr[i]);
	    const ull maxd = max(dl[i], dr[i]);
	    if (i == 0 || mind > minDist || (mind == minDist && maxd > maxDist)) {
		minDist = mind;
		maxDist = maxd;
		iBest = i;
	    }
	}
	assert(iBest < (int)nStalls);
	vb[iBest] = true;
    }
    minDist--;
    maxDist--;
}

int main() {
    // cout << setprecision(10);
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	ull nStalls, nMen, maxDist, minDist;
	cin >> nStalls >> nMen;
	assert (nMen > 0 && nStalls >= nMen);
	MaxMin(maxDist, minDist, nStalls, nMen);
	// MaxMinSimple(maxDist, minDist, nStalls, nMen);
	cout << "Case #" << iTask << ": " << maxDist << ' ' << minDist << '\n';
    }
}
