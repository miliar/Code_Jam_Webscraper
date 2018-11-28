#include <bits/stdc++.h>
#define forn(i,n) for(auto i=0; i < n; i++)
#define forit(it,c) for(auto it=c.begin(); it != c.end(); ++it)
#define f first
#define s second
using namespace std;

char fill(vector<string>& cake, int i, int j, int dir)
{
    if(cake[i][j] != '?') return cake[i][j];
    if((i == 0 and dir == 0) or (i == cake.size() -1 and dir == 1) or (j == 0 and dir == 2) or (j == cake[i].size() -1 and dir == 3)) return '?';
    if(dir == 0) return fill(cake, i-1, j, dir);
    if(dir == 1) return fill(cake, i+1, j, dir);
    if(dir == 2) return fill(cake, i, j-1, dir);
    if(dir == 3) return fill(cake, i, j+1, dir);
}

void solve(vector<string>& cake, int r, int c)
{
    int mins = min(r,c);
    int inc, dir;
    forn(i, r) {
        forn(j, c) {
            if(cake[i][j] == '?') {
                cake[i][j] = fill(cake, i, j, 0);
                if(cake[i][j] == '?') cake[i][j] = fill(cake, i, j, 1);
            }
        }
    }
    forn(i, r) {
        forn(j, c) {
            if(cake[i][j] == '?') {
                cake[i][j] = fill(cake, i, j, 2);
                if(cake[i][j] == '?') cake[i][j] = fill(cake, i, j, 3);
            }
        }
    }
}

int main()
{
    int tests, r, c;
    vector<string> cake;
    string in;

    cin >> tests;
    forn(tt,tests) {
        cake.clear();
        cin >> r >> c;
        forn(i, r) {
            cin >> in;
            cake.push_back(in);
        }
        solve(cake, r, c);
        printf("Case #%d:\n", tt+1);
        forn(i, r) {
            cout << cake[i] << endl;
        }
    }

    return 0;
}
