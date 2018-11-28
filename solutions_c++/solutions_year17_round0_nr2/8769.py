
#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string str;
        cin>>str;
        int len = str.size();
        bool flag=0;
        for(int i=len-1;i>0;i--)
        {
            if(str[i]<str[i-1]&&str[i]!=0&&str[i-1]!=0)
                {
                    for(int j=i;j<len;j++)
                        str[j]='9';
                    str[i-1]=str[i-1]-1;
                    if(str[i-1]=='0')
                        i++;
                }
            while(str[i]=='0')
            {
                flag=1;
                i--;
            }
            if(flag)
            {
                str[i]=str[i]-1;
                for(int j=i+1;j<len;j++)
                    str[j]='9';
                if(str[i]=='0')
                    i++;
                flag=0;
            }
 
        }
        printf("Case #%d: ",tt);
        int flag1=0;
        for(int i=0;i<str.length();i++)
         {
             if(str[i]!='0')
             {
                 flag1=1;
             }
             if(flag1==1)
                cout<<str[i];
         }
         printf("\n");
    }
    return 0;
}