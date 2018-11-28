#include<bits/stdc++.h>
using namespace std;
int col[1007];

int main(void)
{
    freopen("B-small-attempt0 (1).in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    int t, ti, n, r, o, y, g, b, v, i, al, be, ga;
    cin >> t;
    for (ti = 1; ti <= t; ti++) {
        cin >> n >> r >> o >> y >> g >> b >> v;
        vector< pair< int, int > > v(3);
        v[0].first = r;
        v[0].second = 1;
        v[1].first = y;
        v[1].second = 2;
        v[2].first = b;
        v[2].second = 3;
        sort(v.begin(), v.end());
        if (v[2].first>v[1].first+v[0].first) {
            cout << "Case #" << ti << ": IMPOSSIBLE" << endl;
            continue;
        }
        memset(col, 0, sizeof(col));
        al = v[0].first;
        be = v[1].first;
        ga = v[2].first;
        //cout << al << ' ' << be << ' ' << ga << endl;
        for (i = 0; i < ga; i++) {
            col[i*3] = v[2].second;
        }
        for (i = 0; i < be; i++) {
            col[i*3+1] = v[1].second;
        }
        for ( ; i < ga; i++) {
            col[i*3+1] = v[0].second;
            al--;
        }
        for (i = 0; i < al; i++) {
            col[i*3+2] = v[0].second;
        }
        string ot = "";
        for (i = 0; i < 3*ga; i++) {
            //cout << i << ' ' << col[i] << endl;
            if (col[i]==1) ot += 'R';
            else if (col[i]==2) ot += 'Y';
            else if (col[i]==3) ot += 'B';
        }
        cout << "Case #" << ti << ": " << ot << endl;
    }


    return 0;
}
