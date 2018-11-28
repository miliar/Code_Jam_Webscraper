#include <bits/stdc++.h>

using namespace std;

int t, w = 1, r, o, y, g, b, v, n;

string s;

void out(){
    for(int i = 0; i < s.size(); ++i){
        if(s[i] == 'R'){
            for(int j = 0; j < g; ++j){
                cout << "GR";
            }
            g = 0;
        }
        if(s[i] == 'Y'){
            for(int j = 0; j < v; ++j){
                cout << "VY";
            }
            v = 0;
        }
        if(s[i] == 'B'){
            for(int j = 0; j < o; ++j){
                cout << "OB";
            }
            o = 0;
        }
        cout << s[i];
    }
    cout << "\n";
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(w <= t){
        cout << "Case #" << w << ": ";
        ++w;
        cin >> n >> r >> o >> y >> g >> b >> v;
        s.clear();
        int q = r + o + y + g + b + v;
        if(o == b && q == 2 * b){
            for(int j = 0; j < o; ++j){
                cout << "OB";
            }
            cout << "\n";
            continue;
        }
        if(v == y && q == 2 * y){
            for(int j = 0; j < y; ++j){
                cout << "VY";
            }
            cout << "\n";
            continue;
        }
        if(g == r && q == 2 * r){
            for(int j = 0; j < o; ++j){
                cout << "RG";
            }
            cout << "\n";
            continue;
        }
        if((o >= b && o != 0) || (g >= r && g != 0) || (v >= y && v != 0)){
            cout << "IMPOSSIBLE\n";
            continue;
        }
        if(max(r, max(y, b)) > r + y + b - max(r, max(y, b))){
            cout << "IMPOSSIBLE\n";
            continue;
        }
        if(max(r, max(y, b)) == r){
            s += 'R';
            --r;
            while(r + y + b != 0){
                if(s[s.size() - 1] == 'R'){
                    if(y > b) s += 'Y', --y;
                    else s += 'B', --b;
                }else {
                    if(r != 0){
                        s += 'R', --r;
                    } else {
                        if(s[s.size() - 1] == 'B') s += 'Y', --y;
                        else s += 'B', --b;
                    }
                }
            }
            out();
            continue;
        }
        if(max(r, max(y, b)) == y){
            s += 'Y';
            --y;
            while(r + y + b != 0){
                if(s[s.size() - 1] == 'Y'){
                    if(r > b) s += 'R', --r;
                    else s += 'B', --b;
                }else {
                    if(y != 0){
                        s += 'Y', --y;
                    } else {
                        if(s[s.size() - 1] == 'B') s += 'R', --r;
                        else s += 'B', --b;
                    }
                }
            }
            out();
            continue;
        }
        if(max(r, max(y, b)) == b){
            s += 'B';
            --b;
            while(r + y + b != 0){
                if(s[s.size() - 1] == 'B'){
                    if(y > r) s += 'Y', --y;
                    else s += 'R', --r;
                }else {
                    if(b != 0){
                        s += 'B', --b;
                    } else {
                        if(s[s.size() - 1] == 'R') s += 'Y', --y;
                        else s += 'R', --r;
                    }
                }
            }
            out();
            continue;
        }
        cout << s;
    }
    return 0;
}