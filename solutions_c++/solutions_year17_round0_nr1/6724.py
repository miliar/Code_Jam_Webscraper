#include <bits/stdc++.h>
#define int long long int
using namespace std;

#undef int
int main() 
{
#define int long long int

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int t;
    cin>>t;
    for(int tc = 1; tc<=t;tc++)
    {
        string str; int k, a1 = 0, a2 = 0;
        cin>>str>>k;
        int n = str.length();
        string s = str;
        for(int i = 0;i<=n-k;i++)
        {
            if(str[i]=='-')
            {
                a1++;
                for(int j = i;j<i+k;j++)
                    str[j] = (str[j]=='+')?'-':'+';
            }
        }
        bool b1 = true;;
        for(int i = n-k+1;i<n;i++)
            if(str[i]=='-')
                b1 = false;
        str = s;
        for(int i = n-1;i>=k-1;i--)
        {
            if(str[i]=='-')
            {
                a2++;
                for(int j = i;j>i-k;j--)
                    str[j] = (str[j]=='+')?'-':'+';
            }
        }
        bool b2 = true;
        for(int i = 0;i<k-1;i++)
            if(str[i]=='-')
                b2 = false;
        if(!b1&&!b2)cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<tc<<": "<<min(a1, a2)<<endl;
    }
    
    return 0;
}