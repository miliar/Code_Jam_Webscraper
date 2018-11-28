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
typedef vector<string> StringVec;

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

void FillRectangle(StringVec& vs, int R, int C, char c, int iMin, int iMax, int jMin, int jMax) {
    assert(iMin >=0 && iMax < R);
    assert(jMin >=0 && jMax < C);
    for (int i=iMin; i<=iMax; i++)
	for (int j=jMin; j<=jMax; j++)
	    vs[i][j] = c;
}

void Solve(StringVec& vs, int R, int C, int start=0) {
    // cout << "start=" << start << endl; // DEBUG!!!
    assert((int)vs.size()==R && (int)vs[0].size()==C);
    if (start >= R)
	return;
    string empty(C, '?');
    int iMin; // first non-empty line since start
    for (iMin=start; iMin<R; iMin++) {
	if (vs[iMin] != empty)
	    break;
    }
    assert(Within(iMin, start, R-1) && vs[iMin] != empty);
    int iNext; // first non-empty line after iMin, or R
    for (iNext=iMin+1; iNext<R; iNext++) {
	if (vs[iNext] != empty)
	    break;
    }
    // cout << "iMin=" << iMin << " iNext=" << iNext << endl; // DEBUG!!!
    int ind=0;
    char cLast='?';
    forall (j, C) {
	char c = vs[iMin][j];
	if (c == '?')
	    continue;
	cLast = c;
	FillRectangle(vs, R, C, c, start, iNext-1, ind, j);
	ind = j+1;
    }
    assert(cLast != '?');
    FillRectangle(vs, R, C, cLast, start, iNext-1, ind, C-1);
    assert(iNext > start);
    Solve(vs, R, C, iNext);
}

int main() {
    // cout << setprecision(10);
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	int R=0, C=0;
	cin >> R >> C;
	assert(Within(R, 1, 25) && Within(C, 1, 25));
	StringVec vs(R);
	forall (i, R) {
	    cin >> vs[i];
	    assert((int)vs[i].size() == C);
	}
	assert(cin);
	cout << "Case #" << iTask << ":" << endl;
	Solve(vs, R, C);
	forall (i, R)
	    cout << vs[i] << '\n';
	cout << flush;
    }
}
