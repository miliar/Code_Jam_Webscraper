#include <bits/stdc++.h>
#define prev fjioweajiof
#define x1 fjweoifakewop
#define y1 zfewfjwieofajoi
#define ld long double
#define ll long long
#define int long long
using namespace std;

const int nmax = 100010;
const int inf = ((ll)1e15);

int n, q, t, d[151][151], e[1001], s[1001], u, v;
ld d2[151][151];

main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

cin >> t;
int sv  = t;
while (t--){
    cin >> n >> q;
    for (int i=1; i<=n; i++) cin >> e[i] >> s[i];


    for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++){
        cin >> d[i][j];
        if (d[i][j]==-1) d[i][j]=inf;
    }
    for (int k=1; k<=n; k++)
    for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++){
        if (i==j || j==k || i==k) continue;
        d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
    }



    for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++){
        if (d[i][j]==inf) continue;

        d2[i][j]=inf;
        if (d[i][j]<=e[i]) d2[i][j]=1.0*(d[i][j]/(s[i]+0.0));

    }

    for (int i=1; i<=n; i++){
    for (int j=1; j<=n; j++){
        //cout << setprecision(2) << fixed << d2[i][j] << " ";
        //if (i==j || j==k || i==k) continue;
        //d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
    }
    //cout << endl;
    }


    for (int k=1; k<=n; k++)
    for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++){
        if (i==j || j==k || i==k) continue;
        d2[i][j]=min(d2[i][j],d2[i][k]+d2[k][j]);
    }

    cout << "Case #" << sv-t << ": ";
    while (q--){
        cin >> u >> v;
        cout << setprecision(8) << fixed << d2[u][v]<< " ";

    }
    cout << endl;

    //break;

}





return 0;
}
