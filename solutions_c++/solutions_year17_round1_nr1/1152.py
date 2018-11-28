#include <iostream>
#include <fstream>

using namespace std;

char a[26][26];
int db[26]={0};
int n, m;


void feltolt(int sor)
{
    if(db[sor]!=m)
    {
        char vele;
        int akt=1;
        while(a[sor][akt]=='?') akt++;
        vele=a[sor][akt];
        for(int i=1; i<=akt-1; i++) a[sor][i]=vele;
        akt++;
        bool most;
        while(akt<=m)
        {
            most=true;
            while(a[sor][akt]=='?' and akt<=m)
            {
                a[sor][akt]=vele;
                akt++;
                most=false;
            }
            if(most) akt++;
            vele=a[sor][akt-1];
        }
    }
}

void masol(int bol, int ba)
{
    for(int i=1; i<=m; i++)
    {
        a[ba][i]=a[bol][i];
    }
}


int main()
{
    ifstream f("fel1.in");
    ofstream g("fel1.out");

    int t;
    f>>t;

    bool talalt;
    for(int i=1; i<=t; i++)
    {
        f>>n>>m;
        for(int j=1; j<=n; j++)
        {
            db[j]=0;
            for(int k=1; k<=m; k++)
            {
                f>>a[j][k];
                if(a[j][k]!='?') db[j]++;
            }
        }

        talalt=false;
        for(int j=1; j<=n; j++)
        {
            if(!talalt)
            {
                if(db[j]>0)
                {
                    talalt=true;
                    feltolt(j);
                    for(int k=1; k<j; k++) masol(j, k);
                }
            }
            else
            {
                if(db[j]==0) masol(j-1, j);
                else feltolt(j);
            }
        }

        g<<"Case #"<<i<<": "<<endl;
        for(int j=1; j<=n; j++)
        {
            for(int k=1; k<=m; k++)
            {
                g<<a[j][k];
            }
            g<<endl;
        }

    }
    return 0;
}
