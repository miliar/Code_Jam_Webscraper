#include<iostream>
using namespace std;

int main()
{
    int mone;
    cin>>mone;
    for(int j=1;j<=mone;j++)
    {
        int i;
        string str;
        cin>>str;
        int len=str.length();
        int temp=0;
        for(i=len-1;i>0;i--)
        {
            if(str[i]<str[i-1]&&str[i]!=0&&str[i-1]!=0)
                {
                    for(int p=i;p<len;p++)
                        str[p]='9';
                    str[i-1]=str[i-1]-1;
                    if(str[i-1]=='0')
                        i++;
                }
            while(str[i]=='0')
            {
                temp=1;
                i--;
            }
            if(temp)
            {
                str[i]=str[i]-1;
                for(int p=i+1;p<len;p++)
                    str[p]='9';
                if(str[i]=='0')
                    i++;
                temp=0;
            }

        }
        cout<<"Case #"<<j<<": ";
        int temp1=0;
        for(i=0;i<str.length();i++)
         {
             if(str[i]!='0')
             {
                 temp1=1;
             }
             if(temp1==1)
                cout<<str[i];
         }
         cout<<endl;
    }
    return 0;
}