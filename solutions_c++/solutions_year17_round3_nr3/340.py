#include <bits/stdc++.h>
using namespace std;
int n, k;
double in[105];

void solve(int Case) {
    cin >> n >> k;
    double u;
    cin >> u;

    for (int i = 0; i < n; i++) {
        cin >> in[i];
    }

    sort(in,in+n);

    /*for (int i = 0; i < n; i++) {
        cout << in[i] << " ";
    }*/

    while( u > 0) {
        double minn = in[0], gab = u;
        int want = 1;

        for(int i = 1; i<n; i++) {
            if(in[i] == minn) {
                want++;
            } else {
                gab = in[i] - minn;
                break;
            }
        }
        //cout << gab << " " << want << "\n";
        if( gab * want <= u) {
            for(int i = 0; i<want ; i++) {
                in[i] += gab;
                u -= gab;
            }
        } else {
            for(int i = 0; i<want ; i++) {
                in[i] += u/want;
            }
            u = 0;
            break;
        }
    }
    double ans = 1;
    for (int i = 0; i < n; i++) {
        ans = ans * in[i];
    }
    cout << "Case #" << (Case+1) <<": ";
    printf("%lf\n", ans);
}

int main () {
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=0;i<T;i++) solve(i);
}
