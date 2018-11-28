#include <bits/stdc++.h>
#define lli long long int
using namespace std;
int main()
{
    lli T,i=1;
    cin>>T;
    while(i<=T)
    {
        string s;lli n,z=0,moves=0;
        cin>>s>>n;
        lli l=s.length();
        while(z+n-1<l)
        {
            if(s.substr(z,1)=="-")
            {
                lli j=z;
                while(j<z+n)
                {
                    if(s.substr(j,1)=="-")
                    s[j]='+';
                    else
                    s[j]='-';
                    j++;
                }
                moves++;
            }
            z++;
        }
        lli k=0;
        while(s.substr(k,1)=="+")
        {
            k++;
        }
        if(k==l)
        cout<<"Case #"<<i<<": "<<moves<<endl;
        else
        cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
        i++;
    }
}
