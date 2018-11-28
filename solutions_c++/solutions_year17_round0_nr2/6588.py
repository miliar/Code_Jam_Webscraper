#include<bits/stdc++.h>

using namespace std;

int main()
{
    int i,t,j;
    ifstream input;
    ofstream output;
    output.open("B-large.out");
    input.open("B-large.in");
    input>>t;
    for(i=1;i<=t;i++)
    {
        string s;
        input>>s;
        if(s.size()==1)
            output<<"Case #"<<i<<": "<<s[0]<<endl;
        else
        {
            int p=(int)s[0];
            int in=0,q=1;
            for(j=1;j<s.size();j++)
            {
                int c=(int)s[j];
                if(c>p)
                {
                    in=j;
                }
                else if(c<p)
                {
                    q=0;
                    break;
                }
                p=c;
            }
            if(q==0){
            if(s[in]=='1')
            {
                s[in]='0';
            }
            else
            {
                s[in]=s[in]-1;
            }
            for(j=in+1;j<s.size();j++)
            {
                s[j]='9';
            }
            if(s[0]=='0')
                j=1;
            else
                j=0;
            }
            else
            {
                j=0;
            }

            output<<"Case #"<<i<<": ";
            for(;j<s.size();j++)
            {
                output<<s[j];
            }
            output<<endl;
        }
    }
    return 0;
}
