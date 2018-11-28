#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;
 
#define FOR(i,a,b) for(int i=(a);(int)i<(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back
 
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

bool isTidy(string s) {
    string r = s;
    sort(ALL(r));
    return s == r;
}

int main()
{
    
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("B-small-attempt0.out","w",stdout);

    string s; 
    int cases;
    scanf("%d", &cases);
    REP(k, cases) {
        int x;
        scanf("%d", &x);
        for(int i = x; i>= 0; i--) {
            if(isTidy(i2a(i))) {
                printf("Case #%d: %d\n", k + 1,i);
                break;
            }
        }
    }
    
    return 0;
}
 
