#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int n, Q;
int e[110], s[110];
int d[110][110];
int u, v;
priority_queue<pair<double,pair<int,pair<int, int> > > > q;
map<pair<int,pair<int, int> >, double> dist;

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>n>>Q;
        for (int i=0; i<n; i++) {
            cin>>e[i]>>s[i];
            //e[i] = rand();
            //s[i] = rand();
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) scanf("%d", &d[i][j]);
            //for (int j=0; j<n; j++) d[i][j] = rand()%100;
            //d[i][i] = -1;
        }

        printf("Case #%d: ", cas);
        for (int i=0; i<Q; i++) {
            scanf("%d%d", &u, &v);
            u--; v--;

            dist.clear();
            while (!q.empty()) {
                q.pop();
            }

            double res = -1;

            dist[make_pair(u, make_pair(e[u], u))] = 0.0;
            q.push(make_pair(0.0, make_pair(u, make_pair(e[u], u))));

            while (!q.empty()) {

                int p = q.top().second.first;
                int left = q.top().second.second.first;
                int idx = q.top().second.second.second;
                double cur = -q.top().first;
                q.pop();

                //cout<<p<<" "<<cur<<" "<<idx<<endl;

                if (p == v) {
                    res = cur;
                    break;
                }

                for (int i=0; i<n; i++) if (i!=p && d[p][i]!=-1) {

                    if (left >= d[p][i]) {
                        double tmp = cur + 1.0*d[p][i] / s[idx];

                        pair<int,pair<int, int> > key = make_pair(i, make_pair(left - d[p][i], idx));

                        if (dist.find(key) == dist.end() || dist[key] > tmp) {
                            dist[key] = tmp;
                            q.push(make_pair(-tmp, key));
                        }
                    }

                    if (e[p] >= d[p][i]) {
                        double tmp = cur + 1.0*d[p][i] / s[p];

                        pair<int,pair<int, int> > key = make_pair(i, make_pair(e[p] - d[p][i], p));

                        if (dist.find(key) == dist.end() || dist[key] > tmp) {
                            dist[key] = tmp;
                            q.push(make_pair(-tmp, key));
                        }
                    }
                }

            }

            printf("%.12f ", res);
        }

        printf("\n");
    }

    return 0;

}
