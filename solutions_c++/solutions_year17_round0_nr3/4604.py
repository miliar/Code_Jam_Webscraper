#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

pair<ll, ll> solve(ll N, ll K)
{
    map<ll, ll> M;
    M[N]=1;

    while(true)
    {
        auto it=M.end();
        it--;

        ll len=it->first, cnt=it->second;
        M.erase(it);
        assert(len>0);

        //cout << len << ' ' << M.size() << '\n';
        //cin.get();

        ll len_R=len-(len+1)/2, len_L=(len+1)/2-1;
        assert(len_R>=len_L);

        if(K>cnt)
        {
            M[len_L]+=cnt;
            M[len_R]+=cnt;

            K-=cnt;
        }
        else
        {
            return pair<ll,ll>(len_R, len_L);
        }
    }

    //return pair<ll,ll>(0LL, 0LL);
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        ll N, K;
        cin >> N >> K;
        auto result=solve(N, K);
        cout << "Case #" << t << ": " << result.first << ' ' << result.second << endl;
    }
    return 0;
}
