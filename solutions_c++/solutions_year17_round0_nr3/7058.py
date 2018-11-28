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

int _bmax, _bmin;

int bestStall(vector<pair<int, int> > stalls) {
    int bestmax, bestmin, besti = -1;

    REP(i, stalls.size()) {
        if(stalls[i].first == -1 && stalls[i].second == -1) continue;
        if(besti == -1) {
            bestmax = max(stalls[i].first, stalls[i].second),
            bestmin = min(stalls[i].first, stalls[i].second); 
            
            besti = i;         
        }
        int pmax = max(stalls[i].first, stalls[i].second);
        int pmin = min(stalls[i].first, stalls[i].second);
        if(pmin > bestmin) {
            bestmin = pmin;
            bestmax = pmax;
            besti = i;
        } else if(pmin == bestmin) {
            if(pmax > bestmax) {
                bestmin = pmin;
                bestmax = pmax;
                besti = i;               
            } else if(pmax == bestmax) {
                if(i < besti) {
                    bestmin = pmin;
                    bestmax = pmax;
                    besti = i;                     
                }
            }
        }
    }
    _bmax = bestmax;
    _bmin = bestmin;
    return besti;
}

void updateStalls(vector<pair<int, int> > &stalls, int index) {
    REP(i, stalls.size()) {
        int a = abs(i - index) - 1;
        a = max(a, 0);
        if(i > index) stalls[i].first = min(stalls[i].first, a);
        else stalls[i].second = min(stalls[i].second, a);
    }
}

int main()
{
    
    freopen ("C-small-1-attempt0.in","r",stdin);
    freopen ("C-small-1-attempt0.out","w",stdout);

    string s; 
    int cases;
    scanf("%d", &cases);
    REP(m, cases) {
        int k, n;
        scanf("%d %d", &n, &k);
        //printf("%d %d\n", n, k);
        _bmax = _bmin = 0;
        int x = -1, y = n; 
        vector<pair<int, int> > stalls;
        vector<int> stall_index;
        REP(i, n) {
            int a = i - x - 1, b = n - i - 1;
            a = max(a, 0); 
            b = max(b, 0);
            stalls.PB(make_pair(a, b)); 
        }
        int index;
        //REP(i, stalls.size()) printf("%d %d\n", stalls[i].first, stalls[i].second);
        
        REP(i, k) {
            index = bestStall(stalls);
            //printf("index = %d\n", index);

            stalls[index] = make_pair(-1, -1);
            stall_index.PB(index);
            updateStalls(stalls, index);
            //REP(i, stalls.size()) printf("%d %d\n", stalls[i].first, stalls[i].second);
        }
        
        printf("Case #%d: %d %d\n", m + 1, _bmax, _bmin);



    }
    
    return 0;
}
 
