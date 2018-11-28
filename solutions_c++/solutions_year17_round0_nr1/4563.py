#include<bits/stdc++.h>
using namespace std;

int main()
{
    fstream input("oversized.txt",std::ios_base::in);
    ofstream output;
    output.open("output1.txt");
    int T; input>>T;
    for(int t=1;t<=T;t++)
    {
        string s ;input>>s;
        int k,n=0;input>>k;
        for(int i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                for(int j=0;j<k;j++)
                {
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else if(s[i+j]=='+')
                        s[i+j]='-';
                }
                n++;
            }
        }
        int flag=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
                flag=1;
        }
        if(flag==1)
            output<<"Case #"<<t<<": IMPOSSIBLE\n";
        else
            output<<"Case #"<<t<<": "<<n<<"\n";
    }
}
