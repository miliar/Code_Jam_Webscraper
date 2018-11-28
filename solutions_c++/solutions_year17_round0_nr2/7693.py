#include<iostream>
using namespace std;

int main()
{
    int tst12;
    cin>>tst12;
    for(int zu=1;zu<=tst12;zu++)
    {
        int xy;
        string str33;
        cin>>str33;
        int len=str33.length();
        int tmp=0;
        for(xy=len-1;xy>0;xy--)
        {
            if(str33[xy]<str33[xy-1]&&str33[xy]!=0&&str33[xy-1]!=0)
                {
                    for(int ph=xy;ph<len;ph++)
                        str33[ph]='9';
                    str33[xy-1]=str33[xy-1]-1;
                    if(str33[xy-1]=='0')
                        xy++;
                }
            while(str33[xy]=='0')
            {
                tmp=1;
                xy--;
            }
            if(tmp)
            {
                str33[xy]=str33[xy]-1;
                for(int ph=xy+1;ph<len;ph++)
                    str33[ph]='9';
                if(str33[xy]=='0')
                    xy++;
                tmp=0;
            }

        }
        cout<<"Case #"<<zu<<": ";
        int tmp1=0;
        for(xy=0;xy<str33.length();xy++)
         {
             if(str33[xy]!='0')
             {
                 tmp1=1;
             }
             if(tmp1==1)
                cout<<str33[xy];
         }
         cout<<endl;
    }
    return 0;
}
