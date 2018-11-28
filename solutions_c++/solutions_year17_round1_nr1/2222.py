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
#include <unordered_map>
#include <unordered_set>
#include <tuple>

using namespace std;


int main() {
    ifstream cin("in.in");
    ofstream cout("out.in");

    int T;
    cin>>T;
    for (int t = 1; t<=T; t++) {
        int i, j, k;
        int r, c;
        cin>>r>>c;
        string f[25];
        vector<int> x, y;
        vector<pair<int,int>> p;
        x.push_back(-1), x.push_back(r);
        y.push_back(-1), y.push_back(c);
        for (i=0; i<r; i++) cin>>f[i];
        for (i=0; i<r; i++) {
            for (j=0; j<c; j++) {
                if (f[i][j] != '?') {
                    x.push_back(i);
                    y.push_back(j);
                    p.push_back(make_pair(j,i));
                }
            }
        }
        sort(p.begin(), p.end());
        sort(x.begin(), x.end());
        sort(y.begin(), y.end());

        for (auto e: p) {
            int sy = e.first, sx = e.second;
            int ll, rr, uu, dd;
            for (uu=sx-1; uu>=0&&f[uu][sy]=='?'; uu--) {}
            for (dd=sx+1; dd<r&&f[dd][sy]=='?';dd++) {}
            for (i=0; i<y.size(); i++) {
                if (y[i] > sy) {
                    rr = y[i];break;
                }
            }
            for (i=sy; i<rr; i++) {
                for (j=uu+1; j<dd; j++) {
                    if ((i!=sy||j!=sx) && f[j][i]!='?') cout<<"..."<<j<<" "<<i<<" "<<f[j][i];
                    f[j][i] = f[sx][sy];
                }
            }
        }
        for (i=0; i<r; i++) {
            for (j=0; j<p[0].first; j++) {
                f[i][j] = f[i][p[0].first];
            }
        }

        cout<<"Case #"<<t<<":\n";
        for (i=0; i<r; i++) cout<<f[i]<<endl;
    }
}