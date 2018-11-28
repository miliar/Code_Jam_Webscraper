#include <bits/stdc++.h>
using namespace std;

int solve(string s, int K)
{
    int N=s.size();
    int res=0;

    vector<int> delta(N+1, 0);
    int sum=0;

    for(int i=0; i+K<=N; i++)
    {
        sum+=delta[i];
        int cc=s[i]=='+'?0:1;
        int have=(cc+sum)%2;

        if(have==1)
        {
            delta[i+K]+=-1;
            sum++;
            res++;
        }
    }

    for(int i=N-K+1; i<N; i++)
    {
        sum+=delta[i];
        int cc=s[i]=='+'?0:1;
        int have=(cc+sum)%2;

        if(have==1) return -1;
    }
    return res;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        string s; int K;
        cin >> s >> K;

        int result=solve(s, K);

        cout << "Case #" << t << ": ";

        if(result == -1) cout << "IMPOSSIBLE";
        else cout << result;

        cout << '\n';
    }
    return 0;
}
