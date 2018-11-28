#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double rl;

const int MX=1009;
int N, C, M;
int P[MX], B[MX];

int ceil_div(int a, int b)
{
    return (a+b-1)/b;
}

pair<int, int> solve()
{
    vector<int> cnt_place(MX), cnt_customer(MX);

    for(int i=0; i<M; i++)
    {
        cnt_place[P[i]]++;
        cnt_customer[B[i]]++;
    }

    int R=0;
    for(int i=1; i<=C; i++) R=max(R, cnt_customer[i]);

    int sum=0;

    for(int i=1; i<=N; i++)
    {
        sum+=cnt_place[i];
        R=max(R, ceil_div(sum ,i));
    }

    int S=0;
    for(int i=1; i<=N; i++)
    {
        if(cnt_place[i]>R)
        {
            S+=cnt_place[i]-R;
        }
    }

    return pair<int, int> (R, S);

    //map<int, int> M;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        //int N;
        //cin >> N;
        //int result=solve(N);
        cin >> N >> C >> M;
        for(int i=0; i<M; i++) cin >> P[i] >> B[i];
        //pair<int, int> res=solve();
        auto res=solve();
        cout << "Case #" << t << ": " << res.first << ' ' << res.second << endl;
    }
    return 0;
}
