#include <bits/stdc++.h>
using namespace std;
string leastTidy(string s)
{
    string r="";
    int i=0;
    bool leading = true;
    for(;i<s.size()-1;i++)
    {
        if(leading && s[i]=='0') continue;
        if(s[i]!='0') leading = false;
        if(s[i]<=s[i+1]) r.push_back(s[i]);
        else
        {
            r.push_back(s[i]-1);
            i++;
            while(i<s.size())
            {
                r.push_back('9');
                i++;
            }
            break;
        }
    }

    if(i!=s.size())r.push_back(s[s.size()-1]);
    //cout<<r<<"\n";
    return r;
}
int main()
{
    ifstream in("B-large.in");
    ofstream out("out.out");
    int T;
    in>>T;
    for(int t=1;t<=T;t++)
    {
        out<<"Case #"<<t<<": ";

        string s;
        in>>s;
        string r = s;
        do
        {
            s = r;
            r = leastTidy(s);
        }while(!(r==s));
        out<<r<<"\n";
    }
}
