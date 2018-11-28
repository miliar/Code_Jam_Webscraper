#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,n,test,k,i,ans;
    ifstream input;
    input.open("input.cpp");
    ofstream output;
    output.open("output.cpp");
    input>>t;
    for(test=1;test<=t;test++)
    {
        string s;
        input>>s;
        n=s.length();
        ans=0;
        input>>k;
        for(i=0;i<n-k+1;i++)
        {
            if(s[i]=='-')
            {
             for(int j=i;j<k+i;j++)
                {if(s[j]=='-')
                    s[j]='+';
                 else
                    s[j]='-';
                }
                ans++;
            }
        }
        for( i=0;i<n;++i)
        {
            if(s[i]=='-')
                break;
        }
        if(i==n)
        output<<"Case #"<<test<<": "<<ans<<endl;
        else
        output<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}

