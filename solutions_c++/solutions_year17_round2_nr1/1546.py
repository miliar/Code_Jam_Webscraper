/// Bismillahir Rahmanir Rahim

/// Pure_Protea

#include <bits/stdc++.h>
using namespace std;
typedef long long lng;
const double PI = acos(-1.0);
inline int getInt()
{
    int x;
    scanf("%d", &x);
    return x;
}
#define II getInt()
#define dbg(x) cerr << #x << " -->  " << x << endl;
#define theromeo421 main()
#define min3(x,y,z) min(x, min(y, z))
#define read(a) freopen(a, "r", stdin);
#define write(a) freopen(a, "w", stdout);

const int inf = 1 << 30;

void solve();


void IO()
{
    read("A-large.in");
    write("out.txt");
}

int theromeo421
{
    IO();

    int T = II;
    cerr << T << " Cases to be completed" << endl << endl;
    for(int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        solve();
        cerr << cas << " Done" << endl;
    }
    return 0;
}


void solve()
{
    int D = II, N = II;
    double mxtime = -1.0;
    for(int i = 0; i < N; ++i)
    {
        double K, S;
        cin >> K >> S;
        mxtime = max(mxtime, (double)(((double)D - K)) / S);
    }
    mxtime = (double)D / mxtime;
    //cout << (double)D / mxtime << endl;
    printf("%0.10f\n", mxtime);
}
