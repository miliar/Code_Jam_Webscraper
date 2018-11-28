#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
#include <iterator>
using namespace std;

void solve(vector<string>& s)
{
    int h = s.size();
    int w = s[0].size();

    for(int y=0; y<h; ++y){
        for(int x=0; x<w-1; ++x){
            if(s[y][x+1] == '?')
                s[y][x+1] = s[y][x];
        }
        for(int x=w-1; x>0; --x){
            if(s[y][x-1] == '?')
                s[y][x-1] = s[y][x];
        }
    }
    for(int x=0; x<w; ++x){
        for(int y=0; y<h-1; ++y){
            if(s[y+1][x] == '?')
                s[y+1][x] = s[y][x];
        }
        for(int y=h-1; y>0; --y){
            if(s[y-1][x] == '?')
                s[y-1][x] = s[y][x];
        }
    }
}

int main()
{
    int tMax;
    cin >> tMax;

    for(int t=1; t<=tMax; ++t){
        int h, w;
        cin >> h >> w;
        vector<string> s(h);
        for(int i=0; i<h; ++i)
            cin >> s[i];

        solve(s);
        cout << "Case #" << t << ':' << endl;
        for(int i=0; i<h; ++i)
            cout << s[i] << endl;
    }

    return 0;
}
