#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>

#define _USE_MATH_DEFINES
#define INF 99999999
using namespace std;

int n, k;
pair<int, int> p[1001];

double mem[1001][1001];
int done[1001][1001];

double go(int ind, int rem) {
    if(rem > ind+1) return -INF;
    if(rem == 0) return 0;
    if(ind < 0) return -INF;
    if(!done[ind][rem]) {
        mem[ind][rem] = go(ind-1, rem);
        double aux = 2*M_PI*p[ind].first*p[ind].second;
        if(rem == k) aux += M_PI*p[ind].first*p[ind].first;
        double tmp = aux + go(ind-1, rem-1);
        if(tmp > mem[ind][rem]) mem[ind][rem] = tmp;
        done[ind][rem] = 1;
    }
    return mem[ind][rem];
}

int main()
{
    int t;
    cin >> t;
    for(int caso=1; caso<=t; caso++) {
        cin >> n >> k;
        for(int i=0; i<n; i++) {
            cin >> p[i].first >> p[i].second;
        }
        sort(p, p+n);
        memset(done, 0, sizeof(done));
        printf("Case #%d: %.8f\n", caso, go(n-1, k));
    }
}
