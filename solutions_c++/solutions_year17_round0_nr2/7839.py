#include<iostream>
using namespace std;

int main()
{
    int m;
    cin>>m;
    for(int r=1;r<=m;r++)
    {
        int p;
        string str;
        cin>>str;
        int len=str.length();
        int tem=0;
        for(p=len-1;p>0;p--)
        {
            if(str[p]<str[p-1]&&str[p]!=0&&str[p-1]!=0)
                {
                    for(int a=p;a<len;a++)
                        str[a]='9';
                    str[p-1]=str[p-1]-1;
                    if(str[p-1]=='0')
                        p++;
                }
            while(str[p]=='0')
            {
                tem=1;
                p--;
            }
            if(tem)
            {
                str[p]=str[p]-1;
                for(int a=p+1;a<len;a++)
                    str[a]='9';
                if(str[p]=='0')
                    p++;
                tem=0;
            }
         }
        cout<<"Case #"<<r<<": ";
        int tem1=0;
        for(p=0;p<str.length();p++)
         {
             if(str[p]!='0')
             {
                 tem1=1;
             }
             if(tem1==1)
                cout<<str[p];
         }
         cout<<endl;
    }
    return 0;
}