#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <sstream>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cstdlib>
using namespace std;

struct State {
    int hd, ad, hk, ak;
    State(int hd, int ad, int hk, int ak): hd(hd), ad(ad), hk(hk), ak(ak) {
    }
    bool operator<(const State &s) const {
        if (hd != s.hd) {
            return hd < s.hd;
        }
        if (ad != s.ad) {
            return ad < s.ad;
        }
        if (hk != s.hk) {
            return hk < s.hk;
        }
        return ak < s.ak;
    }
    void dump() {
        cerr << hd << ' ' << ad << ' ' << hk << ' ' << ak << endl;
    }
};



int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        int hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        State init(hd, ad, hk, ak);
        map<State, int> steps;
        steps[init] = 0;
        queue<State> q;
        q.emplace(hd, ad, hk, ak);
        int sol = -1;
        while (!q.empty()) {
            State cur = q.front();
            q.pop();
            int curstep = steps[cur];
            //cerr << curstep << ": ";
            //cur.dump();
            if (cur.hk <= cur.ad) {
                sol = curstep + 1;
                break;
            }
            
            State att = cur;
            att.hd -= att.ak;
            att.hk -= att.ad;
            if (att.hd > 0 && steps.find(att) == steps.end()) {
                steps[att] = curstep + 1;
                q.push(att);
            }

            State buff = cur;
            buff.ad += b;
            buff.hd -= buff.ak;
            if (buff.hd > 0 && steps.find(buff) == steps.end()) {
                steps[buff] = curstep + 1;
                q.push(buff);
            }

            State cure = cur;
            cure.hd = hd - buff.ak;
            if (cure.hd > 0 && steps.find(cure) == steps.end()) {
                steps[cure] = curstep + 1;
                q.push(cure);
            }

            if (cur.ak > 0) {
                State debuff = cur;
                debuff.ak -= d;
                if (debuff.ak < 0) {
                    debuff.ak = 0;
                }
                debuff.hd -= debuff.ak;
                if (debuff.hd > 0 && steps.find(debuff) == steps.end()) {
                    steps[debuff] = curstep + 1;
                    q.push(debuff);
                }
            }
        }
        cout << "Case #" << cc << ": ";
        if (sol == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << sol << endl;
        }
    }
}
