#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

bool check (const vector< vector <char> >& v, int i1, int i2, int j, char c) {
    for (int i = i1; i <= i2; ++i)
        if (v[i][j] != c && v[i][j] != '?')
            return false;
    return true;
}

int main () {
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int t1 = 0; t1 < t; ++t1) {
        int n, m;
        cin >> n >> m;
        vector < vector <char> > v(n, vector <char> (m));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> v [i][j];
        vector < vector <bool> > first (n, vector <bool> (m));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (v[i][j] != '?')
                    first[i][j] = true;
        for (int j = 0; j < m; ++j) {
            for (int i = 0; i < n; ++i) {
                if (!first[i][j])
                    continue;
                int curi1 = i;
                char c = v[i][j];
                while (curi1 > 0 && (v[curi1-1][j] == c || v[curi1-1][j] == '?'))
                    --curi1;
                int curi2 = i;
                while (curi2 < v.size() - 1 && (v[curi2 + 1][j] == c || v[curi2 + 1][j] == '?'))
                    ++curi2;
                int curj1 = j;
                while (curj1 > 0 && check(v, curi1, curi2, curj1 - 1, c))
                    --curj1;
                int curj2 = j;
                while (curj2 < m - 1 && check(v, curi1, curi2, curj2 + 1, c))
                    ++curj2;
                for (int l1 = curi1; l1 <= curi2; ++l1)
                    for (int l2 = curj1; l2 <= curj2; ++l2)
                        v[l1][l2] = c;
            }
        }
        cout << "Case #" << t1 + 1 << ": " << endl;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j)
                cout << v[i][j];
            cout << endl;
        }
    }
}

