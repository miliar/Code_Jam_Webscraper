#include<iostream>
using namespace std;

int main()
{
    int tes;
    cin>>tes;
    for(int v=1;v<=tes;v++)
    {
        int rs;
        string sg;
        cin>>sg;
        int lg=sg.length();
        int tep=0;
        for(rs=lg-1;rs>0;rs--)
        {
             if(sg[rs]<sg[rs-1]&&sg[rs]!=0&&sg[rs-1]!=0)
                {
                    for(int pg=rs;pg<lg;pg++)
                        sg[pg]='9';
                    sg[rs-1]=sg[rs-1]-1;
                    if(sg[rs-1]=='0')
                        rs++;
                }
            while(sg[rs]=='0')
            {
               tep=1;
                rs--;
            }
            if(tep)
            {
                sg[rs]=sg[rs]-1;
                for(int pg=rs+1;pg<lg;pg++)
                    sg[pg]='9';
                if(sg[rs]=='0')
                    rs++;
               tep=0;
            }

        }
        cout<<"Case #"<<v<<": ";
        int tmp1=0;
        for(rs=0;rs<sg.length();rs++)
         {
             if(sg[rs]!='0')
             {
                tmp1=1;
             }
             if(tmp1==1)
                cout<<sg[rs];
         }
         cout<<endl;
    }
    return 0;
}

