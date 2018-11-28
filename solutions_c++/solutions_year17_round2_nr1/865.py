#include <bits/stdc++.h>
using namespace std;

typedef double rl;

const int MX=1000+99;
int N, D;
int K[MX], S[MX];

rl solve()
{
    rl t=0.0;
    for(int i=0; i<N; i++)
    {
        t=max(t, (D-K[i]+0.0)/S[i]);
    }
    //cout << "T::" << t << endl;

    return D/t;
}

int main()
{
    cout << setprecision(10);

    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        //int N;
        //cin >> N;
        //int result=solve(N);
        cin >> D >> N;
        for(int i=0; i<N; i++) cin >> K[i] >> S[i];

        cout << "Case #" << t << ": " << solve() << endl;
    }
    return 0;
}
