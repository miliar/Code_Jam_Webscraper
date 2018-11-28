#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int i;
        string str;
        cin>>str;
        int len=str.length();
        int flag=0;
        for(i=len-1;i>0;i--)
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
        cout<<"Case #"<<k<<": ";
        int flag1=0;
        for(i=0;i<str.length();i++)
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
