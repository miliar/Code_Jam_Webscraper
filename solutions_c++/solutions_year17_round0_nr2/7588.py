#include<iostream>
using namespace std;

int main()
{
    int test;
    cin>>test;
    for(int z=1;z<=test;z++)
    {
        int x;
        string str;
        cin>>str;
        int len=str.length();
        int temp=0;
        for(x=len-1;x>0;x--)
        {
            if(str[x]<str[x-1]&&str[x]!=0&&str[x-1]!=0)
                {
                    for(int p=x;p<len;p++)
                        str[p]='9';
                    str[x-1]=str[x-1]-1;
                    if(str[x-1]=='0')
                        x++;
                }
            while(str[x]=='0')
            {
                temp=1;
                x--;
            }
            if(temp)
            {
                str[x]=str[x]-1;
                for(int p=x+1;p<len;p++)
                    str[p]='9';
                if(str[x]=='0')
                    x++;
                temp=0;
            }

        }
        cout<<"Case #"<<z<<": ";
        int temp1=0;
        for(x=0;x<str.length();x++)
         {
             if(str[x]!='0')
             {
                 temp1=1;
             }
             if(temp1==1)
                cout<<str[x];
         }
         cout<<endl;
    }
    return 0;
}
