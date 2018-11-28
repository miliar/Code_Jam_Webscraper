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

struct inter {
    int a;
    int b;
    bool type;
    inter(int a, int b, bool t) : a(a), b(b), type(t) {};
};

bool sortByA(const inter & a, const inter & b) { return a.a < b.a; }

int main() {
    
    freopen("/Users/Lukas/Desktop/in.txt", "r", stdin);
    freopen("/Users/Lukas/Desktop/out.txt", "w", stdout);
    
    vector<inter> v;
    vector<int> va, vb, vc;
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        int A, B;
        cin >> A >> B;
        
        int ta = 12 * 60;
        int tb = 12 * 60;
        
        v.clear();
        va.clear();
        vb.clear();
        vc.clear();
        
        for (int i = 0; i < A; i++) {
            int a, b;
            cin >> a >> b;
            tb -= (b-a);
            v.push_back(inter(a, b, false));
        }
        
        for (int i = 0; i < B; i++) {
            int a, b;
            cin >> a >> b;
            ta -= (b-a);
            v.push_back(inter(a, b, true));
        }
        
        sort(v.begin(), v.end(), sortByA);
        
        for (int i = 1; i < v.size(); i++) {
            if (!v[i].type && !v[i-1].type) {
                va.push_back(v[i].a - v[i-1].b);
            }
            else if (v[i].type && v[i-1].type) {
                vb.push_back(v[i].a - v[i-1].b);
            }
            else {
                vc.push_back(v[i].a - v[i-1].b);
            }
        }
        
        if (!v.back().type && !v[0].type) {
            va.push_back(v[0].a + 24 * 60 - v.back().b);
        }
        else if (v.back().type && v[0].type) {
            vb.push_back(v[0].a + 24 * 60 - v.back().b);
        }
        else {
            vc.push_back(v[0].a + 24 * 60 - v.back().b);
        }
        
        sort(va.begin(), va.end());
        sort(vb.begin(), vb.end());
        
        int ca = 0;
        int cb = 0;
        
        for (int i = 0; i < va.size(); i++) if (va[i] <= tb) { ca++; tb -= va[i]; }
        for (int i = 0; i < vb.size(); i++) if (vb[i] <= ta) { cb++; ta -= vb[i]; }
        
        cout << (va.size() - ca) * 2 + (vb.size() - cb) * 2 + vc.size() << endl;
    }
    
    return 0;
}
