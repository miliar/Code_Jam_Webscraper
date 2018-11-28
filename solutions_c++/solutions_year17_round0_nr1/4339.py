#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <map>
#include <string.h>
#include <utility>
using namespace std;
int t;
int k;
int flag=1;
char s[1010];
ifstream infile("file.in");
ofstream outfile("file.out");
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            infile>>s;infile>>k;
            outfile<<"Case #"<<i+1<<": ";
            flag=1;
            int len=strlen(s);
            int ans=0;
            for(int i=0;i<len;++i)
            {
                if(s[i]=='+')continue;
                else
                {
                    if(len-i<k)
                    {
                        flag=0;
                        break;
                    }
                    else
                    {
                        ++ans;
                        for(int j=i;j<=i+k-1;++j)
                        {
                            if(s[j]=='+')s[j]='-';
                            else s[j]='+';
                        }
                    }
                }
            }
            if(flag)
            {
                outfile<<ans<<endl;
            }
            else outfile<<"IMPOSSIBLE"<<endl;
        }
    }
}
