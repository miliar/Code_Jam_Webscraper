#include <bits/stdc++.h>

#define mod 1000000007
#define inf 1000000000000LL
#define root2 1.41421
#define root3 1.73205
#define pi 3.14159
#define MAX 100001
#define cntbit __builtin_popcountll
#define ll long long int
#define PII pair<int, int>
#define f first
#define s second
#define mk make_pair
#define PLL pair<ll, ll>
#define gc getchar
#define pb push_back

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, ca=1, i, j, n;
    string s;
    cin>>t;
    while(ca<=t)
    {
        cout<<"Case #"<<ca<<": ";
        cin>>s;
        n=s.size();
        i=0;
        for(j=1;j<n;j++)
        {
            if(s[j]>s[i])
            {
                i=j;
                continue;
            }
            if(s[j]==s[i]) continue;
            if(s[j]<s[i])
            {
                int x=s[i];
                x--;
                s[i]=(char)x;
                i++;
                while(i<n)
                {
                    s[i]='9';
                    i++;
                }
            }
        }
        i=0;
        if(s[0]=='0')i=1;
        for(;i<n;i++)
        cout<<s[i];
        cout<<endl;
        ca++;
    }
}
