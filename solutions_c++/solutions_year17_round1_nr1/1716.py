#include<iostream>
#include<algorithm>
#include<memory.h>
#include<stdio.h>
#include<string>
#include<vector>
#include<bitset>
#include<climits>
#include<list>
#include<set>
#include<fstream>

using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int t,r,c,nonzero;

    ofstream aout("a.txt");
    cin>>t;

    for(int tc=1;tc<=t;tc++)
    {
        cin>>r>>c;

        char a[r][c];


        for(int i=0;i<r;i++)
        {

            nonzero=0;
            for(int j=0;j<c;j++)
            {

                cin>>a[i][j];
                if(nonzero==0)
                {
                    if(a[i][j]!='?')
                    {
                        nonzero=1;
                        for(int k=j;k>=0;k--)
                        {
                            a[i][k]=a[i][j];
                        }
                    }
                }
                else
                {
                    if(a[i][j]=='?')
                    {
                        a[i][j]=a[i][j-1];
                    }
                }


            }

        }


        for(int i=0;i<c;i++)
        {

            nonzero=0;
            for(int j=0;j<r;j++)
            {


                if(nonzero==0)
                {
                    if(a[j][i]!='?')
                    {
                        nonzero=1;
                        for(int k=j;k>=0;k--)
                        {
                            a[k][i]=a[j][i];
                        }
                    }
                }
                else
                {
                    if(a[j][i]=='?')
                    {
                        a[j][i]=a[j-1][i];
                    }
                }


            }

        }

        cout<<"Case #"<<tc<<": "<<endl;
        aout<<"Case #"<<tc<<": "<<endl;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cout<<a[i][j];
                aout<<a[i][j];
            }
            cout<<endl;
            aout<<endl;
        }







    }

    return 0;
}

/*
6
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
3 4
CO?E
????
JA?M
3 3
???
?MA
???
4 4
????
????
??J?
????
*/


