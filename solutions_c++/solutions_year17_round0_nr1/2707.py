#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    string s;
    int n,k,ans=0,err=0;
    ofstream out("output.txt");
    ifstream in("input.in");
    in>>n;
    for(int i=0;i<n;i++)
    {
        ans=0,err=0;
        in>>s>>k;
        for(int l=0;l<s.size();l++)
        {
            if(s[l]!='+')
            {
                if(l+k-1<s.size())
                {
                    ans++;
                    for(int f=l;f<=l+k-1;f++)
                    {
                        if(s[f]=='+')
                            s[f]='-';
                        else if(s[f]=='-')
                                s[f]='+';
                    }
                }
                else if(l+k-1>=s.size())
                {
                    err=1;
                    break;
                }
            }
        }
        if(err==1)
            out<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        else out<<"Case #"<<i+1<<": "<<ans<<endl;
    }
}
