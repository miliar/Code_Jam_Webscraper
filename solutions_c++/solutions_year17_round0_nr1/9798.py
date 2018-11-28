#include <bits/stdc++.h>
using namespace std;
int n,k;

int call(int i, int counter, string mother)
{
    if(i>=n)
    {
        for(int i = 0; i<n; i++)
        {
            if(mother[i]!='+') return 1000000000;
        }
        return counter;
    }

    string child = "";
    child = mother;
    int res = 1000000000;
    res = min(res, call(i+1, counter, child));
    if(i + k - 1 <= n - 1 )
    {
        for(int j = i; j<= i + k - 1; j++)
        {
            if(child[j]=='+') child[j]='-';
            else child[j] = '+';
        }
        res = min(res, call(i+1, counter + 1, child));
    }
    return res;
}
int main ()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen ("a2.out","w",stdout);
    int t,cs = 0; cin>>t;
    while(t--)
    {
        string s; cin>>s;
        cin>>k;
        n = s.size();

        int ans = call(0,0,s);
        if(ans==1000000000) cout<<"Case #"<<++cs<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<++cs<<": "<<ans<<endl;
    }
    return 0;
}
