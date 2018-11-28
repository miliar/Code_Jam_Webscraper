#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N,len,ans,c=1;
    string s;
    cin>>N;
    while(N--)
    {
        cin>>s>>len;
        ans=0;
        for(int i=0;i+len<=s.size();++i)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=0;j<len;++j)
                    s[i+j]= s[i+j]=='+'?'-':'+';
            }
        }
        for(auto a:s)
            if(a=='-')
                ans=-1;
        cout<<"Case #"<<c++<<": ";
        if( ans== -1 )cout<<"IMPOSSIBLE\n";
        else cout<<ans<<"\n";
    }

}

