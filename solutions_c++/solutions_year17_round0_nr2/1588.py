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

string Solve(string s) {
    int len = s.size();

    // make i the first digit s.t. s[i]>s[i+1], e.g. 23555*5*4
    int i;
    for (i = 0; i < len - 1; i++)
	if (s[i] > s[i+1])
	    break;
    if (i == len - 1)
	return s;

    // make i the first digit followed by same digits and then a smaller digit, e.g. 23*5*5554
    // note that i is either the first digit or preceded by a smaller digit
    const char dig = s[i];
    while (i >= 0 && s[i] == dig)
	--i;
    ++i;

    s[i]--;
    for (int j = i + 1; j < len; j++)
	s[j] = '9';
    if (s[0] == '0')
	s = s.substr(1);
    return s;
}

int main() {
    // cout << setprecision(10);
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	string s;
	cin >> s;
	cout << "Case #" << iTask << ": " << Solve(s) << '\n';
    }
}
