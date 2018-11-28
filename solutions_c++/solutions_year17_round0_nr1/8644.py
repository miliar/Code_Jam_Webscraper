#include<bits/stdc++.h>
using namespace std;
int main()
{
    char ara[1000];
    int num,times;
    ofstream fout;
    fout.open("output.txt");
    cin>>times;
    for( int cas=1;cas<=times;cas++)
    {

        cin>> ara>>num;
        int temp=0,time=0;
        for( int i=0;i<strlen(ara);i++)
        {
            if(ara[i]=='-')
            {
                if(strlen(ara)-i<num)
                {
                    time=-1;
                    break;
                }
                else
                {
                    time++;
                    cout<<ara<<endl;
                    for( int j=0;j<num;j++)
                    {
                        ara[j+i]=ara[j+i]=='-'? '+' :'-';
                    }
                    cout<<ara<<endl;

                }

            }

        }
        fout<<"Case "<<"#"<<cas<<": ";
        if(time==-1) fout<<"IMPOSSIBLE\n";
        else fout<<time<<"\n";
    }

    fout.close();
    return 0;

}
