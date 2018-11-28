#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t,cs=0;
    string str;
    cin>>t;
    while(t--)
    {
        cs++;
        cin>>str;
        int len = str.length();
        for(int i=0;i<len-1;i++)
        {
            if(str[i]>str[i+1])
            {
                for(int j=i+1;j<len;j++)
                    str[j]='9';
                for(int j=i;j>=0;j--)
                {
                    if(str[j]=='0')
                    {
                        str[j]='9';
                        continue;
                    }
                    str[j]=str[j]-1;
                    if(j==0) break;
                    if(str[j]>=str[j-1])
                        break;
                    str[j]='9';
                }
                break;
            }
        }
        string ans="";
        int i=0;
        while(i<len && str[i]=='0')
        {
            i++;
        }
        while(i<len)
        {
            ans+=str[i++];
        }
        cout<<"Case #"<<cs<<": "<<ans<<"\n";
    }
    return 0;
}

/*
4
132
129 is str
Case #1:
1000
0999 is str
Case #2:
7
7 is str
Case #3:
111111111111111110
099999999999999999 is str
 once 00641118 is 960051513
 once 00641118 is 960051513
Case # once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
4 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
:  once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513

 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513
 once 00641118 is 960051513

Process returned 0 (0x0)   execution time : 16.175 s
Press any key to continue.
*/
