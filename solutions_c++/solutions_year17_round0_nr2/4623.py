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
    freopen("tidy_large.in", "r", stdin);
    freopen("a74.txt", "w", stdout);
    int t=1, l, i, j, k, n;
    cin>>t;
    string s;
    for(l=1; l<=t; l++)
    {
        cin>>s;
        n=s.size();
        i=n-1;
        while(i>0)
        {
            if(s[i]<s[i-1])
            {
                for(j=i; j<n; j++)
                    s[j]='9';
                s[i-1]--;
            }
            i--;
        }
        while(s[0]=='0')
            s=s.substr(1);
        cout<<"Case #"<<l<<": "<<s<<endl;
    }
    return 0;
}
