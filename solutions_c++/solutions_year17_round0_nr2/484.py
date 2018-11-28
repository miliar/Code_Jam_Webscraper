#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
using namespace std;

fstream f("B-large.in", ios_base::in);
fstream g("output.txt", iostream::out);
int t;
unsigned long long n, n2;
string s;

int main()
{
    f>>t;
    for(int i=1; i<t+1; ++i)
    {
        f>>n;
        if(n<=9) g<<"Case #"<<i<<": "<<n<<endl;
         else
         {
            n2=n;
            while(n>0) {s=char('0'+n%10)+s; n/=10;}
            int j;
            for(j=0; j<s.length()-1 && s[j]<=s[j+1]; ++j);
            if(j==s.length()-1) g<<"Case #"<<i<<": "<<n2<<endl;
            else
            {
                if(s[j]=='1') {g<<"Case #"<<i<<": "; for(int q=0; q<s.length()-1; ++q) g<<'9'; g<<endl;}
                else
                {
                    int q;
                    for(q=1; j-q>=0 && s[j-q]==s[j]; ++q);
                    --q;
                    s[j-q]-=1;
                    for(int p=1; j-q+p<s.length(); ++p) s[j-q+p]='9';
                    g<<"Case #"<<i<<": "<<s<<endl;
                }
            }
         }
        s.clear();
    }

    return 0;
}
