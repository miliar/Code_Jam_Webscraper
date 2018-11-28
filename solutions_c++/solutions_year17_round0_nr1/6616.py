#include<bits/stdc++.h>

using namespace std;

int main()
{
    int i,t;
    ifstream input;
    ofstream output;
    output.open("A-large.out");
    input.open("A-large.in");
    input>>t;
    for(i=1;i<=t;i++)
    {
        int k,ans=0,l,p=1,j;
        string s;
        input>>s>>k;
        for(j=0;j<=(s.size()-k);j++)
        {

            if(s[j]=='-')
            {
                for(l=j;l<j+k;l++)
                {
                    if(s[l]=='-')
                        s[l]='+';
                    else
                        s[l]='-';
                }
                ans++;
            }
        }
        for(;j<s.size();j++)
        {
            if(s[j]=='-')
            {
                p=0;
                break;
            }
        }
        if(p==1)
            output<<"Case #"<<i<<": "<<ans<<endl;
        else
            output<<"Case #"<<i<<": "<<"IMPOSSIBLE\n";
    }
    return 0;
}
