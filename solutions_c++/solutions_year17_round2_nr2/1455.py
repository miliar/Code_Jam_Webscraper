//
// Created by andy on 4/22/17.
//

#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <sstream>

using namespace std;



int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        if (V > Y / 2 || G > R / 2 || O > B / 2) {
            cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
            continue;
        }

        stringstream ss;
        char first = -1;
        char last = -1;
        for (int j = 0; j < O; j++) {
            last = first = 'B';
            ss << "B" << "O" << "B" << endl;
        }
        B -= 2 * O;
        for (int j = 0; j < G; j++) {
            if (first == -1) first = 'R';
            last = 'R';
            ss << "R" << "G" << "R" << endl;
        }
        R -= 2 * G;
        for (int j = 0; j < G; j++) {
            if (first == -1) first = 'Y';
            last = 'Y';
            ss << "Y" << "V" << "Y" << endl;
        }
        Y -= 2 * V;

        bool ok = true;

        // a > b && a > c
        auto solve = [&ss, i](pair<int, char> a, pair<int, char> b, pair<int, char> c) {
            for (int j = 0; j < b.first; j++)
                ss << a.second << b.second;
            a.first -= b.first;

            int v = min(a.first, c.first);
            for (int j = 0; j < v; j++)
                ss << a.second << c.second;
            a.first -= v;
            c.first -= v;

            if (a.first > 0) {
                cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
            } else {
                cout << "Case #" << i + 1 << ": ";
                string s = ss.str();
                int j = 0;
                for (; j < c.first; j++) {
                    cout << s[j] << c.second;
                }

                for (; j < s.length(); j++) {
                    cout << s[j];
                }
                cout << endl;
            }
        };

        if (Y >= B && Y >= R) {
            solve({Y, 'Y'}, {R, 'R'}, {B, 'B'});
        } else if (B >= Y && B >= R) {
            solve({B, 'B'}, {R, 'R'}, {Y, 'Y'});
        } else if (R >= Y && R >= B) {
            solve( {R, 'R'}, {Y, 'Y'}, {B, 'B'});
        }
    }

    return 0;
}
