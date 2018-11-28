#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

fstream f("A-large.in", ios_base::in);
fstream g("output.txt", iostream::out);

int t, k, res=0;
string s;
bool b=false;

int main()
{
    f>>t;
    for(int i=1; i<t+1; ++i)
    {
        f>>s; f>>k;
        int l=s.length();
        for(int j=0; j<l-k+1; ++j)
        {
            if(s[j]!='+')
            {
                ++res;
                for(int n=0; n<k; ++n)
                {
                    if(s[j+n]=='+') s[j+n]='-'; else s[j+n]='+';
                }
            }
        }

        for(int j=l-k+1; j<s.length(); ++j) {if(s[j]=='-') {g<<"Case #"<<i<<": IMPOSSIBLE"<<endl; b=true; break;}}

        if(!b) g<<"Case #"<<i<<": "<<res<<endl;
        res=0;
        b=false;
    }

    return 0;
}
