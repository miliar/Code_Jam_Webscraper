#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream inp;
    ofstream out;
    inp.open("input.txt");
    out.open("output.txt");
    int t,k,cnt;
    string s;
    inp>>t;
    for(int T=1;T<=t;T++)
    {
        cnt = 0;
        inp>>s>>k;
        for(int i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                cnt++;
                for(int j=0;j<k;j++)
                {
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else
                        s[i+j]='-';
                }
            }
        }
        bool flag = 0;
        for(int i=s.size()-k+1;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                flag =1;
                break;
            }
        }
        out<<"Case #"<<T<<": ";
        if(flag)
            out<<"IMPOSSIBLE"<<endl;
        else
            out<<cnt<<endl;
    }
    return 0;
}
