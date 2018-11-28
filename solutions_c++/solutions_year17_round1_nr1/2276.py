#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int main()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("aout.txt","w",stdout);
    cin>>T;
    for (int x=1;x<=T;x++)
    {
        int r,c;
        cin>>r>>c;
        string s[r];
        for (int i=0;i<r;i++)
            cin>>s[i];
        int flag=-1, flag1 = -1;
        char a;
        for (int i=0;i<r;i++)
        {
            for (int j=0;j<c;j++)
            {
                if(s[i][j]!='?')
                {
                    flag =1;
                    if(flag1 == -1)
                        flag1 = 1;
                    a=s[i][j];
                    break;
                    //cout<<"if1"<<endl;
                }
            }
            if(flag == 1)
            {
                //cout<<"if2"<<endl;
                for (int j=0;j<c;j++)
                {
                    if(s[i][j]=='?')
                    {
                        s[i][j] = a;
                        //cout<<"if3"<<endl;
                    }
                    else
                    {
                        a=s[i][j];
                        //cout<<"if4"<<endl;
                    }
                }
                if (flag1 == 1)
                {
                    int z=i-1;
                    while(z>=0)
                    {
                        s[z] = s[z+1];
                        //cout<<"if5"<<endl;
                        z--;
                    }
                    flag1 = 0;
                }
            }
            else
            {
                if(i!=0 && flag1 == 0)
                {
                    s[i] = s[i-1];
                    //cout<<"if6"<<endl;
                }

            }
            flag = -1;
        }
        cout<<"Case #"<<x<<":"<<endl;
        for (int i=0;i<r;i++)
            cout<<s[i]<<endl;

    }
    return 0;
}
