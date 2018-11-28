#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("blarge.in","r",stdin);
    freopen("blarge.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int tt,k;
    cin>>tt;
    string s;
    for(int t=1; t<=tt; t++)
    {
        cin>>s;
        int n=s.length();
        for(int i=s.length()-1; i>=1; i--)
        {
            if(s[i]<s[i-1])
            {
                if(s[i-1]!='0')
                    s[i-1]--;
                for(int j=i; j<n; j++)
                    s[j]='9';
                //s[i]='9';
            }
        }
        unsigned long long int num=0,power=1;
        for(int i=s.length()-1; i>=0; i--)
        {
            num+=(s[i]-'0')*power;
            power=power*10;
        }
        cout<<"Case #"<<t<<": "<<num<<endl;
        cerr<<"Test Case "<<t<<" Solved"<<endl;
    }
    return 0;
}
