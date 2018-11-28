#include<bits/stdc++.h>
using namespace std;
char ara[30];
char ans[30];
bool  rec( int i, char val)
{
    if(i==strlen(ara))
    {
        ans[i]='\0';
        return true ;
    }
    else{
        for( char c='9'; c>='0';c--)
        {
            if( c<=ara[i] && c>=val)
            {
                ans[i]=c;
                if( c<ara[i])
                {
                    for( int j=i+1; j<strlen(ara);j++) ans[j]='9';
                    ans[strlen(ara)]='\0';
                    return true;

                }
                else{
                    bool b=rec(i+1,c);
                    if(b==true) return true ;
                }


            }
        }
        return false;
    }
}
int main()
{

    int num,times;
    ofstream fout;
    ifstream fin;
    fout.open("output.txt");
    fin.open("B-large.in");
    fin>>times;
    for( int cas=1;cas<=times;cas++)
    {

        fin>>ara;
        int flag=1;

        fout<<"Case "<<"#"<<cas<<": ";


            rec(0,'0');
            for(int i=0;i<strlen(ans);i++)
            {
                if(ans[i]!='0')
                {
                    flag=0;
                    fout<<ans[i];
                }
                else if(flag=0) fout<<ans[i];

            }
        fout<<endl;

    }

    fout.close();
    return 0;

}
