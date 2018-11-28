#include <bits/stdc++.h>
#define INF 1000000009
#define mod 1000000007
#define PI 3.14159
#define vi vector<int>
#define ll long long
#define ii pair<int, int>
#define pll pair<ll, ll>
#define vii vector<ii>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define mt make_tuple
#define eb emplace_back
#define CLR(arr) memset(arr, 0, sizeof(arr))
#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int ctr=1; ctr<=T; ++ctr)
    {
        string S;
        int K;
        cin>>S>>K;
        int i=0;
        int ans = 0;
        while(i<S.size())
        {
            if(i+K<=S.size() && S[i]=='-')
            {
                for(int j=i; j<i+K; ++j)
                    S[j] = (S[j]=='+') ? '-' : '+';
                ++ans;
            }
            else if(i+K>S.size() && S[i]=='-')
            {
                ans = -1;
                break;
            }
            ++i;
        }
        cout<<"Case #"<<ctr<<": ";
        if(ans==-1)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<endl;
    }
    return 0;
}
