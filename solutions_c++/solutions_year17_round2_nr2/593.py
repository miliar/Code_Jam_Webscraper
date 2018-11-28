#include <cstdio>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    int testCases;
    cin >> testCases;

    for (int testCase = 1; testCase <= testCases; testCase++) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;

        r -= g;
        y -= v;
        b -= o;

        map<char,char> m;
        map<char,char> m2;
        m2['R'] = 'G';
        m2['Y'] = 'V';
        m2['B'] = 'O';

        int A, B, C, D, E, F;

        if (r >= y && y >= b) {
            m['A'] = 'R'; m['B'] = 'Y'; m['C'] = 'B';
            A = r; B = y; C = b; D = g; E = v; F = o;
        } else if (r >= b && b >= y) {
            m['A'] = 'R'; m['B'] = 'B'; m['C'] = 'Y';
            A = r; B = b; C = y; D = g; E = o; F = v;
        } else if (y >= r && r >= b) {
            m['A'] = 'Y'; m['B'] = 'R'; m['C'] = 'B';
            A = y; B = r; C = b; D = v; E = g; F = o;

        } else if (y >= b && b >= r) {
            m['A'] = 'Y'; m['B'] = 'B'; m['C'] = 'R';
            A = y; B = b; C = r; D = v; E = o; F = g;

        } else if (b >= r && r >= y) {
            m['A'] = 'B'; m['B'] = 'R'; m['C'] = 'Y';
            A = b; B = r; C = y; D = o; E = g; F = v;

        } else if (b >= y && y >= r) {
            m['A'] = 'B'; m['B'] = 'Y'; m['C'] = 'R';
            A = b; B = y; C = r; D = o; E = v; F = g;
        }

        if (B + C < A || D > A || E > B || F > C) {
            cout << "Case #" << testCase << ": IMPOSSIBLE" << endl;
        } else {
            vector<char> ans;

            for (int i = 0; i < A; i++) {
                ans.push_back('A');
                if (D > 0) {
                    ans.push_back('D');
                    ans.push_back('A');
                    D--;
                }

                if (i < B) {
                    ans.push_back('B');

                    if (E > 0) {
                        ans.push_back('E');
                        ans.push_back('B');
                        E--;
                    }
                }

                if (A - i <= C) {
                    ans.push_back('C');

                    if (F > 0) {
                        ans.push_back('F');
                        ans.push_back('C');
                        F--;
                    }
                }
            }

            cout << "Case #" << testCase << ": ";

            for (int i = 0; i < ans.size(); i++) {
                if (ans[i] == 'A' || ans[i] == 'B' || ans[i] == 'C') {
                    cout << m[ans[i]];
                } else if (ans[i] == 'D') {
                    cout << m2[m['A']];
                } else if (ans[i] == 'E') {
                    cout << m2[m['B']];
                } else if (ans[i] == 'F') {
                    cout << m2[m['C']];
                }
            }
            
            cout << endl;
        }        
    }
}
