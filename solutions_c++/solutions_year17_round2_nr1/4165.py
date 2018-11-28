#include <bits/stdc++.h>
#define optimezeio ios_base::sync_with_stdio(0);cin.tie
#define lli long long int

using namespace std;

struct horse
{
    double k, s;
};


void _main(int tcase) {
    cout << "Case #" << tcase << ": ";
    int D, N;

    cin >> D >> N;
    vector<horse> horses;
    for (int i = 0; i < N; ++i)
    {
        double k, s;
        cin >> k >> s;
        horses.push_back({k, s});
    }

    sort( horses.begin( ), horses.end( ), [ ]( const horse & lhs, const horse & rhs )
    {
        return lhs.k > rhs.k;
    });

    double ans;
    if (N == 1)
    {
        ans = (horses[0].s * D) / (D - horses[0].k);
        cout << fixed << setprecision(6) << ans << endl;
        return;
    }

    int cual = 0;

    for (int i = 1; i < N; ++i)
    {
        double t = (horses[i - 1].k - horses[i].k) / (horses[i].s - horses[i - 1].s);
        double x = horses[i].k + (horses[i].s * t);
        // cout << endl;
        // cout << t << endl;
        if (t < 0 || isinf(t) || x > D)
        {
            cual = i;
        }
    }

    // cout << endl;
    // cout << horses[cual].k << " " << horses[cual].s << endl;
    ans = (horses[cual].s * D) / (D - horses[cual].k);
    cout << fixed << setprecision(6) << ans << endl;


    // for (int i = 0; i < N; ++i)
    // {
    //     cout << horses[i].k << " " << horses[i].s << endl;
    // }


}

int main () {
    optimezeio(0);
    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i)
    {
        
        _main(i);
    }
}
