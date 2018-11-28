//
// Created by Xuren Zhou on 22/4/2017.
//

#include <iostream>

using namespace std;

string stableNeighbors(int n, int r, int o, int y, int g, int b, int v) {

    if(o == b && o != 0) {
        if (n == o + b) {
            string res = "";
            for (int i = 0; i < o; i++) {
                res += "OB";
            }
            return res;
        }
        else {
            return "IMPOSSIBLE";
        }
    }

    if(g == r && g != 0) {
        if (n == g + r) {
            string res = "";
            for (int i = 0; i < g; i++) {
                res += "GR";
            }
            return res;
        }
        else {
            return "IMPOSSIBLE";
        }
    }

    if(v == y && v != 0) {
        if (n == v + y) {
            string res = "";
            for (int i = 0; i < v; i++) {
                res += "VY";
            }
            return res;
        }
        else {
            return "IMPOSSIBLE";
        }
    }

    if(o <= b && g <= r && v <= y) { // general case
        b = b - o;
        r = r - g;
        y = y - v;

        char a[3];

        if(b  >= r && b >= y) {
            a[0] = 'B';
            if(r >= y) {
                a[1] = 'R';
                a[2] = 'Y';
            }
            else {
                a[1] = 'Y';
                a[2] = 'R';
            }
        }
        else if(r >= b && r >= y) {
            a[0] = 'R';
            if(b >= y) {
                a[1] = 'B';
                a[2] = 'Y';
            }
            else {
                a[1] = 'Y';
                a[2] = 'B';
            }
        }
        else {
            a[0] = 'Y';
            if(b >= r) {
                a[1] = 'B';
                a[2] = 'R';
            }
            else {
                a[1] = 'R';
                a[2] = 'B';
            }
        }


        int val[3];
        val[0] = max(b, max(y, r));
        val[2] = min(b, min(y, r));
        val[1] = b + y + r - val[0] - val[2];

        if(val[1]+val[2] < val[0]) {
            return "IMPOSSIBLE";
        }
        else {
            string res = "";
            for(int i=0; i < val[1] + val[2] - val[0]; i++) {
                res += "XYZ";
            }

            for(int i=0; i < val[1] - val[2]; i++) {
                res += "XY";
            }

            for(int i=0; i < val[0] - val[1]; i++) {
                res += "XYXZ";
            }

            string true_res = "";
            for(int i=0; i < res.size(); i++) {
                true_res += a[res[i] - 'X'];
            }

            for(int i=0; i < true_res.size(); i++) {
                if(true_res[i] == 'B') {
                    string start = true_res.substr(0, i);
                    string end = true_res.substr(i, true_res.size() - i);
                    string middle = "";
                    for(int j=0; j < o; j++) {
                        middle += "BO";
                    }
                    true_res = start + middle + end;
                    break;
                }
            }

            for(int i=0; i < true_res.size(); i++) {
                if(true_res[i] == 'R') {
                    string start = true_res.substr(0, i);
                    string end = true_res.substr(i, true_res.size() - i);
                    string middle = "";
                    for(int j=0; j < g; j++) {
                        middle += "RG";
                    }
                    true_res = start + middle + end;
                    break;
                }
            }

            for(int i=0; i < true_res.size(); i++) {
                if(true_res[i] == 'Y') {
                    string start = true_res.substr(0, i);
                    string end = true_res.substr(i, true_res.size() - i);
                    string middle = "";
                    for(int j=0; j < v; j++) {
                        middle += "YV";
                    }
                    true_res = start + middle + end;
                    break;
                }
            }

            return true_res;
        }
    }

    return "IMPOSSIBLE";
}

int main() {
    int t;
    cin >> t;
    for(int i=1; i <=t; i++) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        cout << "Case #" << i << ": " << stableNeighbors(n, r, o, y, g, b, v) << endl;
    }

    return 0;
}