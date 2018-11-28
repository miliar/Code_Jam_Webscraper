#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define trace(x)    cerr << #x << ": " << x << endl;
#define bitcount    __builtin_popcountll
#define MOD 1000000007
#define pb push_back
#define pi pair<int,int>
#define pii pair<pi,int>
#define mp make_pair

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("pancakes_large.in", "r", stdin);
    freopen("a71.txt", "w", stdout);
    int t=1, l, i, j, flag, k, n, ans;
    cin>>t;
    string s;
    for(l=1; l<=t; l++)
    {
        cin>>s>>k;
        n=s.size();
        i=ans=flag=0;
        while(i<n)
        {
            while(i<n && s[i]!='-')
                i++;
            if(i==n)
                break;
            for(j=0; j<k; j++)
            {
                if(i+j>=n)
                {
                    flag=1;
                    break;
                }
                if(s[i+j]=='-')
                    s[i+j]='+';
                else
                    s[i+j]='-';
            }
            i++;
            ans++;
        }
        if(flag)
            cout<<"Case #"<<l<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<l<<": "<<ans<<endl;
    }
    return 0;
}
