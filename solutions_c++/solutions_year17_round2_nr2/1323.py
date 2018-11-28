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

int n;

vector <int> res;

bool isOk(int a, int b) {
    switch (a) {
        case 0: return b == 2 || b == 3 || b == 4;
        case 1: return b == 4;
        case 2: return b == 0 || b == 4 || b == 5;
        case 3: return b == 0;
        case 4: return b == 0 || b == 1 || b == 2;
        case 5: return b == 2;
        default: return false;
    }
}

bool dfs(int depth, int r, int o, int y, int g, int b, int v) {
    if (r < 0 || o < 0 || y < 0 || g < 0 || b < 0 || v < 0) return false;
    if (depth == n) return isOk(res[0], res.back());
    int prev = (res.size() > 0 ? res.back() : -1);
    
    if (prev == -1) {
        if (o > 0) {
            res.push_back(1);
            if (dfs(depth+1, r, o-1, y, g, b, v)) return true;
            res.pop_back();
        }
        else if (v > 0) {
            res.push_back(5);
            if (dfs(depth+1, r, o, y, g, b, v-1)) return true;
            res.pop_back();
        }
        else if (g > 0) {
            res.push_back(3);
            if (dfs(depth+1, r, o, y, g-1, b, v)) return true;
            res.pop_back();
        }
        else if (r > 0) {
            res.push_back(0);
            if (dfs(depth+1, r-1, o, y, g, b, v)) return true;
            res.pop_back();
        }
        else if (y > 0) {
            res.push_back(2);
            if (dfs(depth+1, r, o, y-1, g, b, v)) return true;
            res.pop_back();
        }
        else {
            res.push_back(4);
            if (dfs(depth+1, r, o, y, g, b-1, v)) return true;
            res.pop_back();
        }
        
        return false;
    }
    
    switch (prev) {
        case 1:
        {
            res.push_back(4);
            if (dfs(depth+1, r, o, y, g, b-1, v)) return true;
            res.pop_back();
            return false;
        }
        case 5:
        {
            res.push_back(2);
            if (dfs(depth+1, r, o, y-1, g, b, v)) return true;
            res.pop_back();
            return false;
        }
        case 3:
        {
            res.push_back(0);
            if (dfs(depth+1, r-1, o, y, g, b, v)) return true;
            res.pop_back();
            return false;
        }
        case 0:
        {
            res.push_back(3);
            if (dfs(depth+1, r, o, y, g-1, b, v)) return true;
            res.pop_back();
            if (g > 0) return false;
            
            res.push_back(2);
            if (dfs(depth+1, r, o, y-1, g, b, v)) return true;
            res.pop_back();
            
            res.push_back(4);
            if (dfs(depth+1, r, o, y, g, b-1, v)) return true;
            res.pop_back();
            
            return false;
        }
        case 2:
        {
            res.push_back(5);
            if (dfs(depth+1, r, o, y, g, b, v-1)) return true;
            res.pop_back();
            if (v > 0) return false;
            
            res.push_back(0);
            if (dfs(depth+1, r-1, o, y, g, b, v)) return true;
            res.pop_back();
            
            res.push_back(4);
            if (dfs(depth+1, r, o, y, g, b-1, v)) return true;
            res.pop_back();
            
            return false;
        }
        case 4:
        {
            res.push_back(1);
            if (dfs(depth+1, r, o-1, y, g, b, v)) return true;
            res.pop_back();
            if (o > 0) return false;
            
            res.push_back(0);
            if (dfs(depth+1, r-1, o, y, g, b, v)) return true;
            res.pop_back();
            
            res.push_back(2);
            if (dfs(depth+1, r, o, y-1, g, b, v)) return true;
            res.pop_back();
            
            return false;
        }
    }
//    
//    if (isOk(prev, 1)) {
//        res.push_back(1);
//        if (dfs(depth+1, r, o-1, y, g, b, v)) return true;
//        res.pop_back();
//    }
//    else
//    if (isOk(prev, 5)) {
//        res.push_back(5);
//        if (dfs(depth+1, r, o, y, g, b, v-1)) return true;
//        res.pop_back();
//    }
//    else
//    if (isOk(prev, 3)) {
//        res.push_back(3);
//        if (dfs(depth+1, r, o, y, g-1, b, v)) return true;
//        res.pop_back();
//    }
//    else
//    if (isOk(prev, 0)) {
//        res.push_back(0);
//        if (dfs(depth+1, r-1, o, y, g, b, v)) return true;
//        res.pop_back();
//    }
//    else
//    if (isOk(prev, 2)) {
//        res.push_back(2);
//        if (dfs(depth+1, r, o, y-1, g, b, v)) return true;
//        res.pop_back();
//    }
//    else
//    if (isOk(prev, 4)) {
//        res.push_back(4);
//        if (dfs(depth+1, r, o, y, g, b-1, v)) return true;
//        res.pop_back();
//    }
    
    return false;
}

int main() {
    
    freopen("/Users/Lukas/Desktop/in.txt", "r", stdin);
    freopen("/Users/Lukas/Desktop/out.txt", "w", stdout);
    
    int T;
    vector<ii> v;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int R, O, Y, G, B, V;
        cin >> n >> R >> O >> Y >> G >> B >> V;
//        bool pos = dfs(0, R, O, Y, G, B, V);
        cout << "Case #" << t << ": ";
        v.clear();
        
        v.push_back(ii(R, 'R'));
        v.push_back(ii(Y, 'Y'));
        v.push_back(ii(B, 'B'));
        sort(v.begin(), v.end());
        
        if (v[0].first + v[1].first < v[2].first) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            string s = "";
            while(v[0].first > 0) {
                s += v[0].second;
                v[0].first--;
                if (v[0].first > 0) {
                    s += v[2].second;
                    v[2].first--;
                }
                sort(v.begin(), v.end());
            }
            while(v[2].first > 0) {
                s += v[2].second;
                v[2].first--;
                if (v[1].first > 0) {
                    s += v[1].second;
                    v[1].first--;
                }
            }
            
            cout << s << endl;
        }
        
        
//        
//        if (pos) {
//            while (res.size() > 0) {
//                int last = res.back();
//                res.pop_back();
//                char c = 'z';
//                switch (last) {
//                    case 0: c = 'R'; break;
//                    case 1: c = 'O'; break;
//                    case 2: c = 'Y'; break;
//                    case 3: c = 'G'; break;
//                    case 4: c = 'B'; break;
//                    case 5: c = 'V'; break;
//                }
//                cout << c;
//            }
//            cout << endl;
//        }
//        else {
//            
//        }
    }
    
    return 0;
}
