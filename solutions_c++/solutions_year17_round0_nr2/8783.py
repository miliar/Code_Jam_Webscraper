#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long t,x,l,flag,i,flag1,j;
    cin>>t;
    for(x=1;x<=t;x++)
    {
        string str;
        cin>>str;
        l=str.size();
        flag=0;
        for(i=l-1;i>0;i--)
        {
            if(str[i]<str[i-1] && str[i]!=0 && str[i-1]!=0)
                {
                    for(j=i;j<l;j++)
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
            if(flag==1)
            {
                str[i]=str[i]-1;
                for(j=i+1;j<l;j++)
                    str[j]='9';
                if(str[i]=='0')
                    i++;
                flag=0;
            }
 
        }
        cout<<"Case #"<<x<<": ";
        flag1=0;
        for(i=0;i<l;i++)
         {
             if(str[i]!='0')
             {
                 flag1=1;
             }
             if(flag1==1)
                cout<<str[i];
         }
         cout<<endl;
    }
    return 0;
}

