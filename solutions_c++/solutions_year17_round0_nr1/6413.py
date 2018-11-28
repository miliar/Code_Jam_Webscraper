#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    int t, k;
    string s;
    cin>>t;
    for(int tt = 1; tt <=t; tt++)
    {
        cin>>s>>k;
        int n = s.length();
        int cnt = 0;
        for(int i = 0; i <= n-k; i++)
        {
            if(s[i] == '+') continue;
            cnt++;
            for(int j = i; j < i+k; j++)
                s[j] = s[j]=='+'?'-':'+';
        }

        bool f = 0;
        for(int i = 0; i < n; i++)
        {
            if(s[i]=='-')
            {
                f = 1;
                break;
            }
        }

        cout<<"Case #"<<tt<<": ";
        if(f) cout<<"IMPOSSIBLE\n";
        else cout<<cnt<<"\n";
    }
    return 0;
}
