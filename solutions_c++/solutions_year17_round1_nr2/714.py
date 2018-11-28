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
typedef vector<IntVec> IntVV;
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

// upper part of a/b
inline int Upper(int a, int b) {return (a+b-1)/b;}

bool MinMax(int weight, int need, int& min, int& max) {
    max = (10 * weight) / (9 * need);
    min = Upper(10 * weight, 11 * need);
    assert(min > 0);
    return min <= max;
}

int Solve(const IntVV& vvMin, const IntVV& vvMax, const IntVec& vNeed, int N) {
    IntVec vCol(N, 0);
    int n = 0;
    while (true) {
	int maxMin = -1;
	forall (iRow, N) {
	    const int iCol = vCol[iRow];
	    const IntVec& vMin = vvMin[iRow];
	    const IntVec& vMax = vvMax[iRow];
	    assert(vMin.size() == vMax.size());
	    if (iCol >= (int)vMin.size())
		return n;
	    int curMin = vMin[iCol];
	    assert(curMin <= vMax[iCol]);
	    if (curMin > maxMin)
		maxMin = curMin;
	}
	bool bInc = false;
	forall (iRow, N) {
	    int& iCol = vCol[iRow];
	    const IntVec& vMax = vvMax[iRow];
	    const int len = vMax.size();
	    while (iCol < len && vMax[iCol] < maxMin) {
		bInc = true;
		++iCol;
	    }
	}
	if (!bInc) {
	    ++n;
	    forall (iRow, N)
		vCol[iRow]++;
	}
    }
}
	

int main() {
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	int N, P;
	cin >> N >> P;
	IntVec vNeed(N);
	forall (i, N) {
	    cin >> vNeed[i];
	    assert(Within(vNeed[i], 1, 1000000));
	}
	IntVV vvMin(N), vvMax(N);
	forall (i, N) {
	    const int need = vNeed[i];
	    IntVec vWei(P);
	    forall (j, P) {
		cin >> vWei[j];
		assert(Within(vWei[j], 1, 1000000));
	    }
	    sort(vWei.begin(), vWei.end());
	    forall (j, P) {
		int min, max;
		MinMax(vWei[j], need, min, max);
		if (min <= max) {
		    vvMin[i].push_back(min);
		    vvMax[i].push_back(max);
		}
	    }
	}
	/*
	PrintVec("vNeed: ", vNeed);
	cout << "vvMin:\n";
	forall (i, vvMin.size())
	    PrintVec(vvMin[i]);
	cout << "\nvvMax:\n";
	forall (i, vvMax.size())
	    PrintVec(vvMax[i]);
	cout << '\n';
	*/

	int n = Solve(vvMin, vvMax, vNeed, N);
	cout << "Case #" << iTask << ": " << n << endl;
    }
}
