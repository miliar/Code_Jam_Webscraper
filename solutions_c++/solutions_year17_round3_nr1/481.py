#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double rl;

int N, K;
struct pancake
{
    ll R, H;
};

bool operator <(const pancake& A, const pancake& B)
{
    return A.R*A.H<B.R*B.H;
}

const int MX=1000+99;
pancake P[MX];

rl solve()
{
    sort(P, P+N);
    reverse(P, P+N);

    ll best_ans=0;
    for(int lo=0; lo<N; lo++)
    {
        ll curr_ans=P[lo].R*P[lo].R+2*P[lo].R*P[lo].H;;

        int used=0;
        for(int i=0; used<K-1; i++)
        {
            if(i==lo) continue;
            used++;
            curr_ans+=2*P[i].R*P[i].H;
        }

        best_ans=max(best_ans, curr_ans);
    }

    //cerr << acos(-1.0) << endl;
    return best_ans*acos(-1.0);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cout << setprecision(20);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        //int N;
        //cin >> N;
        //int result=solve(N);
        cin >> N >> K;
        for(int i=0; i<N; i++) cin >> P[i].R >> P[i].H;

        rl ans=solve();
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
