#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

ifstream in("data.in");
ofstream out("data.out");

string s;
int sol=0;

int main()
{
    int tests;
    in>>tests;
    for(int i=1; i<=tests; i++)
    {
        in>>s;
        int k;
        int l=s.size();
        in>>k;
        for(int j=0; j<=l-k+1; j++)
        {
            if(s[j]=='-')
            {
                s[j]='+';
                sol++;
                for(int p=j+1; p<=j+k-1; p++)
                {
                    if(s[p]=='-')
                    {
                        s[p]='+';
                    }
                    else
                    {
                        s[p]='-';
                    }

                }
            }
        }
        out<<"Case #"<<i<<": ";
        int flag=1;
        for(int p=l-k+2;p<=l;p++)
        {
            if(s[p]=='-')
                flag=0;
        }
        if(flag==1)
        {
        out<<sol<<'\n';
        }
        else
        {
            out<<"IMPOSSIBLE"<<'\n';
        }
        sol=0;
    }
}
