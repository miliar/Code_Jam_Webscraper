
#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
// #include <cinttypes> // C++11?
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <new>
#include <algorithm>
#include <iostream>
#include <iostream>
#include <sstream> 
using namespace std;
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define RE(i, n) FOR(i, 1, n)
typedef vector<int> Vint;
typedef vector<int>::iterator Vit;
template <class _T> inline string tostr(const _T &a) { stringstream os(""); os << a; return os.str(); }
void  work(int & a,  int & b) {
	int k , n;
	cin >> n >> k;
	Vint D; 
//     cout << " Case :  " << k << " " << n << endl;
	D.push_back(n);
	RE(i, k) {
        std::sort(D.rbegin(), D.rend());

        int t = D[0] - 1;
        b = (int) ( t/2 );
        a = t - b; 
  //       cout << t << " " << a << " " << b << endl;
        D.erase(D.begin());
        D.push_back(a);
        D.push_back(b);
	}
}

int main () {
    int T;
    int a = 0 , b =0  ; 
    cin >> T; 
    RE(i , T) {
    	work(a,b );
    	cout << "Case #" << i<<": " << a << " " << b;
    	cout << endl;
    } 
	return 0;
}