#include <iostream>
#include <cstdio>

using namespace std;

int T, K, ans;
string S;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    cin>>T;
    for(int T1 = 1; T1 <= T; ++T1)
    {
        ans = 0;
        cin>>S>>K;
        for (int i = 0; i < (int)S.size() - K + 1; ++i)
            if (S[i] == '-')
            {
                for (int j = i; j < i + K; ++j)
                    S[j] = (S[j] == '+' ? '-' : '+');
                ++ans;
            }
        for (int i = 0; i < (int)S.size(); ++i)
            if(S[i] == '-')
            {
                ans = - 1;
                break;
            }
        if (ans == -1) cout<<"Case #"<<T1<<": IMPOSSIBLE\n";
            else cout<<"Case #"<<T1<<": "<<ans<<"\n";
    }
}
