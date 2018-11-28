#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <valarray>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> pp;

const int CMAX = 1e5 + 5;
const int INF = 2e9 + 5;

struct pancake {
    int r, h;
    double area;
    double s;
    int i;
};

bool sortByArea(const pancake &a, const pancake &b) { return a.area > b.area; }
bool sortByS(const pancake &a, const pancake &b) { return a.s > b.s; }

int main() {
    
    freopen("/Users/Lukas/Desktop/in.txt", "r", stdin);
    freopen("/Users/Lukas/Desktop/out.txt", "w", stdout);
    
    vector <pancake> v, vs;
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, k;
        cin >> n >> k;
        v.clear();
        for(int i = 0; i < n; i++) {
            int r, h;
            cin >> r >> h;
            pancake p = pancake();
            p.r = r;
            p.h = h;
            p.i = i;
            p.area = (double)2.0 * M_PI * (double)r * (double)h;
            p.s = M_PI * (double)r * (double)r;
            v.push_back(p);
        }
        vs = vector<pancake>(v);
        
        sort(v.begin(), v.end(), sortByArea);
        sort(vs.begin(), vs.end(), sortByS);
        
        double maxres = 0.0;
        
        for (int j = 0; j <= vs.size() - k; j++) {
            int start = vs[j].i;
            double res = vs[j].s + vs[j].area;
            int got = 1;
            for (int i = 0; i < n && got < k; i++) {
                if (v[i].i != start && v[i].r <= vs[j].r) {
                    res += v[i].area;
                    got++;
                }
            }
            if (got == k) {
                maxres = max(maxres, res);
            }
        }
        
        cout << "Case #" << t << ": " << fixed << setprecision(10) << maxres << endl;
    }
    
    return 0;
}
