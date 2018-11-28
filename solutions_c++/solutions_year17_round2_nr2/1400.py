#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>

using namespace std;

int main() {
    int T; cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ": ";

        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        //Special cases: only one color and its complement, and they're equal.
        if(R == G && O + Y + B + V == 0) {
            for(int i = 0; i < R; i++)
                cout << "RG";
            cout << endl;
            continue;
        }
        if(O == B && R + Y + G + V == 0) {
            for(int i = 0; i < O; i++)
                cout << "OB";
            cout << endl;
            continue;
        }
        if(Y == V && O + G + B + R == 0) {
            for(int i = 0; i < V; i++)
                cout << "YV";
            cout << endl;
            continue;
        }

        // impossible: too many of a complex color.
        if((V >= Y && V != 0) || (O >= B && O !=0) || (G >= R && G != 0)) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        //impossible: too much of one of the simple colors.
        if(R > Y + B || Y > R + B || B > R + Y) {
            cout << "IMPOSSIBLE" << endl;
            continue;

        }

        char c1, c2, c3;
        int n1, n2, n3;
        if(R >= Y && Y >= B) {
            c1 = 'R';
            c2 = 'Y';
            c3 = 'B';
            n1 = R;
            n2 = Y;
            n3 = B;
        }
        if(Y >= B && B >= R) {
            c1 = 'Y';
            c2 = 'B';
            c3 = 'R';
            n1 = Y;
            n2 = B;
            n3 = R;
        }
        if(B >= R && R >= Y) {
            c1 = 'B';
            c2 = 'R';
            c3 = 'Y';
            n1 = B;
            n2 = R;
            n3 = Y;
        }
        if(R >= B && B >= Y) {
            c1 = 'R';
            c2 = 'B';
            c3 = 'Y';
            n1 = R;
            n2 = B;
            n3 = Y;
        }
        if(Y >= R && R >= B) {
            c1 = 'Y';
            c2 = 'R';
            c3 = 'B';
            n1 = Y;
            n2 = R;
            n3 = B;
        }
        if(B >= Y && Y >= R) {
            c1 = 'B';
            c2 = 'Y';
            c3 = 'R';
            n1 = B;
            n2 = Y;
            n3 = R;
        }
        vector<char> v;
        for(int k = 0; k < n1; k++) {
            v.push_back(c1);
            if(k < n2)
                v.push_back(c2);
            else if (k < n2 + n3)
                v.push_back(c3);
            if(k < n3 - (n1 - n2))
                v.push_back(c3);
        }

        bool Od = false, Gd = false, Vd = false;
        for(char c : v) {
            cout << c;
            if(c == 'B' && !Od) {
                for(int i = 0; i < O; i++) {
                    cout << "OB";
                }
                Od = true;
            }
            if(c == 'R' && !Gd) {
                for(int i = 0; i < G; i++) {
                    cout << "GR";
                }
                Gd = true;
            }
            if(c == 'Y' && !Vd) {
                for(int i = 0; i < V; i++) {
                    cout << "VY";
                }
                Vd = true;
            }
        }
        cout << endl;
    }
    return 0;
}
