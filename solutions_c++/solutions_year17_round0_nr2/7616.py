#include<iostream>
using namespace std;

int main()
{
    int test;
    cin>>test;
    for(int i=1;i<=test;i++)
    {
        int a;
        string r;
        cin>>r;
        int len=r.length();
        int temp=0;
        for(a=len-1;a>0;a--)
        {
            if(r[a]<r[a-1]&&r[a]!=0&&r[a-1]!=0)
                {
                    for(int b=a;b<len;b++)
                        r[b]='9';
                    r[a-1]=r[a-1]-1;
                    if(r[a-1]=='0')
                        a++;
                }
            while(r[a]=='0')
            {
                temp=1;
                a--;
            }
            if(temp)
            {
                r[a]=r[a]-1;
                for(int b=a+1;b<len;b++)
                    r[b]='9';
                if(r[a]=='0')
                    a++;
                temp=0;
            }

        }
        cout<<"Case #"<<i<<": ";
        int lap=0;
        for(a=0;a<r.length();a++)
         {
             if(r[a]!='0')
             {
                 lap=1;
             }
             if(lap==1)
                cout<<r[a];
         }
         cout<<endl;
    }
    return 0;
}
