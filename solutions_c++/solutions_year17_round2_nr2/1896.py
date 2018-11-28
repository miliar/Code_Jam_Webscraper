#include <iostream>
#include <fstream>
#include <map>
#include <cstdio>
#include <algorithm>

using namespace std;

//ifstream in("input.txt");
ifstream in("B-small-attempt1.in");
ofstream out("B-small-attempt1.out");

//#define out cout

struct clr {
    int pri;
    int sec;
    int val;
    string pc;
    string sc;
} m[3];

bool f(clr a, clr b) {
    return a.val > b.val;
}

int main()
{
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        int n, r, o, y, g, b, v;
        in >> n >> r >> o >> y >> g >> b >> v;
        m[0] = {y, v, y - v, "Y", "V"};
        m[1] = {r, g, r - g, "R", "G"};
        m[2] = {b, o, b - o, "B", "O"};
        int total = 0;
        int maxi = 0;
        bool special = 0;
        for (int j = 0; j < 3; ++j) {
            //out << m[j].val;
            //out << m[j].val << ' ' << i + 1 << '\n';
            if (m[j].val < 0) goto imp;
            if (m[0].val + m[1].val + m[2].val == 0) {m[j].val = 1;special = 1;}
            total += m[j].val;
            if (maxi < m[j].val) maxi = m[j].val;
        }
        sort(m, m + 3, f);
        //out << total << maxi;
        if (maxi > total/2 && total != 1) goto imp;
        goto pos;
        imp:
            out << "Case #" << i+1 << ": IMPOSSIBLE\n";
            continue;
        pos:
            out << "Case #" << i + 1 << ": ";
        int turn = 0;
        //out << total;
        for (int j = 0; j < total; ++j) {
                if (m[turn].sec > 0) {
                    for (int l = 0; l < m[turn].sec; ++l) {
                        out << m[turn].pc << m[turn].sc;
                    }
                    if (m[turn].pri != m[turn].sec) out << m[turn].pc;
                    m[turn].pri -= m[turn].sec + ((m[turn].pri == m[turn].sec)?0:1);
                    m[turn].sec = 0;
                } else {
                    out << m[turn].pc;
                    m[turn].pri -= 1;
                }
                m[turn].val -= 1;
                int maxi2 = -1;
                int turn2 = -1;
                for (int l = 0; l < 3; ++l) {
                    if (m[l].val > maxi2 && l != turn) {
                        turn2 = l;
                        maxi2 = m[l].val;
                    }
                }
                turn = turn2;
        }
        out << '\n';
    }
    return 0;
}
