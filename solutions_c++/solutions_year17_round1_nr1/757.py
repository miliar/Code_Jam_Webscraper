#include <iostream>
#include <cstdio>
using namespace std;
int q,n,m,t;
char Mat[30][30],Lin[30];
string cuv;
bool flg;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for (int q=1;q<=t;q++)
    {
        cout<<"Case #"<<q<<":\n";
        cin>>n>>m;
        for (int i=0;i<n;i++)
        {
            cin>>cuv;
           // cout<<cuv<<'\n';
            Lin[i]=NULL;
            for (int j=0;j<m;j++)
            {
                if (cuv[j]!='?')
                {
                    Mat[i][j]=cuv[j];
                    Lin[i]=cuv[j];
                }
                else
                    Mat[i][j]=NULL;
            }
            if (Lin[i]==NULL)
                Lin[i]='c';
        }
        if (Lin[0]=='c')
            flg = true;
        for (int i=0;i<n;i++)
        {
            if (Lin[i]!='c') flg = false;
            if (Lin[i]!='c')
            {
                for (int j=1;j<m;j++)
                {
                    if (Lin[i]!='c')
                    {   if (Mat[i][j]==NULL)
                        if (Mat[i][j-1]!=NULL)
                            Mat[i][j]=Mat[i][j-1];
                    }
                }
                for (int j=m-1;j>=0;j--)
                {
                    if (Lin[i]!='c')
                    {
                         if (Mat[i][j]==NULL)
                            if (Mat[i][j+1]!=NULL)
                                Mat[i][j]=Mat[i][j+1];
                    }
                }
            }
            if ( Lin[i]=='c'&&flg == false&&i>0)
            {

                for (int j=0;j<m;j++)
                    if (Mat[i][j]==NULL)
                        Mat[i][j]=Mat[i-1][j];
            }
        }
        if (Lin[n-1]=='c')
            flg = true;
        for (int i=n-1;i>=0;i--)
        {
            if (Lin[i]!='c') flg = false;
            if (Lin[i]!='c')
            {
                for (int j=1;j<m;j++)
                {
                    if (Lin[i]!='c')
                    {
                        if (Mat[i][j]==NULL)
                            if (Mat[i][j-1]!=NULL)
                                Mat[i][j]=Mat[i][j-1];
                    }
                }
                for (int j=m-1;j>=0;j--)
                {
                    if (Lin[i]!='c')
                    {
                        if (Mat[i][j]==NULL)
                            if (Mat[i][j+1]!=NULL)
                                Mat[i][j]=Mat[i][j+1];
                    }
                }
            }
            if ( Lin[i]=='c'&&flg == false&&i<n-1)
            {
                for (int j=0;j<m;j++)
                    Mat[i][j]=Mat[i+1][j];
            }
        }
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
                cout<<Mat[i][j];
            cout<<'\n';
        }
    }
}
