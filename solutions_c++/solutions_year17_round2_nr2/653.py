#include <bits/stdc++.h>

using namespace std;

map<char, int> cont;

void mix(string &s, char c1, char c2, char c3){
    char cs[] = {c1, c2, c3};
    int last = 0;
    while (true){
        int t = 0, id = -1;
        for (int i = 0; i < 3; i++){
            if (t < cont[cs[i]] && ((1<<i) & last) == 0){
                t = cont[cs[i]];
                id = i;
            }
        }
        if (id == -1) break;
        cont[cs[id]]--;
        s += cs[id];
        last = 1<<id;
    }
    if (s[s.size()-1] == s[0]){
        if (s.size() >= 3){
            swap(s[s.size()-1], s[s.size()-2]);
            if (s[s.size()-2] == s[s.size()-3])
                s = "";
            return;
        }
        s = "";
    }
}

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        cont['R'] = r;
        cont['O'] = o;
        cont['Y'] = y;
        cont['G'] = g;
        cont['B'] = b;
        cont['V'] = v;

        cout << "Case #" << cases++ << ": ";

        string s = "";
        mix(s, 'R', 'Y', 'B');
        if (s.size() < n){
            cout << "IMPOSSIBLE" << endl;
        }
        else
            cout << s << endl;
    }
    return 0;
}
