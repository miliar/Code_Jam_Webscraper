#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); i++)

int main() {
    int T;
    cin >> T;
    forn(t, T) {
        int n;
        cin >> n;
        vector<int> v(6);
        string s = "", C = "ROYGBV";
        bool sirve = true, triang = true;
        forn(i, 6) cin >> v[i];
        forn(i, 6) if(v[i]) {
            s += C[i];
            v[i] --;
            break;
        }
        if(v[0] + v[2] < v[4] || v[0] + v[4] < v[2] || v[2] + v[4] < v[0]) triang = false;
        forn(p, n - 1) {
            if(!sirve) break;
            if(s[p] == 'R') {
                if(v[3]) {
                    s += "G";
                    v[3] --;
                } else {
                    if(v[2] > v[4]) {
                        s += "Y";
                        v[2] --;
                    } else if(v[4]) {
                        s += "B";
                        v[4] --;
                    } else {
                        sirve = false;
                    }
                }
            }
            if(s[p] == 'O') {
                if(v[4]) {
                    s += "B";
                    v[4] --;
                } else sirve = false;
            }
            if(s[p] == 'Y') {
                if(v[5]) {
                    s += "V";
                    v[5] --;
                } else {
                    if(v[0] > v[4]) {
                        s += "R";
                        v[0] --;
                    } else if(v[4]) {
                        s += "B";
                        v[4] --;
                    } else {
                        sirve = false;
                    }
                }
            }
            if(s[p] == 'G') {
                if(v[0]) {
                    s += "R";
                    v[0] --;
                } else sirve = false;
            }
            if(s[p] == 'B') {
                if(v[1]) {
                    s += "O";
                    v[1] --;
                } else {
                    if(v[2] > v[0]) {
                        s += "Y";
                        v[2] --;
                    } else if(v[0]){
                        s += "R";
                        v[0] --;
                    } else {
                        sirve = false;
                    }
                }
            }
            if(s[p] == 'V') {
                if(v[2]) {
                    s += "Y";
                    v[2] --;
                } else sirve = false;
            }
        }
        if(s[0] == 'O' && s[n - 1] != 'B') sirve = false;
        if(s[0] == 'G' && s[n - 1] != 'R') sirve = false;
        if(s[0] == 'V' && s[n - 1] != 'Y') sirve = false;
        if(s[n - 1] == 'O' && s[0] != 'B') sirve = false;
        if(s[n - 1] == 'G' && s[0] != 'R') sirve = false;
        if(s[n - 1] == 'V' && s[0] != 'Y') sirve = false;
        if(s[0] == s[n - 1]) sirve = false;
        if(!sirve) s = "IMPOSSIBLE";
        if(triang && !sirve) cerr << t + 1 << endl;
        cout << "Case #" << t + 1 << ": " << s << endl;
    }
}
