#include <bits/stdc++.h>

#define ll double
#define M 1000000007
#define INF 9999999999999999 // 9223372036854775807
#define mp(x, y) make_pair(x,y)
#define pb(x) push_back(x)
#define pmp(x, y) pb(mp(x,y))
#define ld double
#define PI 3.14159265
#define len(a) (ll)a.size()    //
#define F first
#define S second
#define endl "\n"
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;

ll horse[101], speed[101], mat[101][101],timee[102];


int main() {

    ll t;

    cin >> t;

    for (ll hell = 1; hell <= t; hell++) {

        ll n, q;
        cin >> n >> q;

        for (int i = 0; i < n; i++) {
            cin >> horse[i] >> speed[i];
        }


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> mat[i][j];
            }
        }


        ll start, end;
        while (q--) {
            cin >> start >> end;

            for (int i = 0; i < n; i++) {
                timee[i]=INF;
            }

            timee[0]=0;

            for (int i = 0; i < n - 1; i++) {
                ll dist = mat[i][i+1];

                for (int j = i + 1;j < n;j++) {

                    timee[j] = min(timee[j], (dist / speed[i]) +timee[i]);
                    dist += mat[j][j + 1];

                    if(dist > horse[i])
                        break;

                }


            }

            cout<<"Case #"<<hell<<": ";
            printf("%lf\n",timee[(int)n-1]);

        }

    }


    return 0;
}
