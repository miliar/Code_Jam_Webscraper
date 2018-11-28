#include <iostream>


using namespace std;


int main() {
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int r, c;
        cin>>r>>c;
        char cake[33][33]={0};
        for(int i=1;i<=r;i++)
            for(int j=1;j<=c;j++)
                cin>>cake[i][j];


        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                if('A'<=cake[i][j] && cake[i][j]<='Z')
                {
                    for(int jj=j+1;jj<=c;jj++)
                    {
                        if(cake[i][jj] != '?')
                            break;
                        cake[i][jj] = cake[i][j];
                    }
                }
            }
            for(int j=c;j>=1;j--)
            {
                if('A'<=cake[i][j] && cake[i][j]<='Z')
                {
                    for(int jj=j-1;jj>=1;jj--)
                    {
                        if(cake[i][jj] != '?')
                            break;
                        cake[i][jj] = cake[i][j];
                    }
                }
            }
        }

        for(int j=1;j<=c;j++)
        {
            for(int i=1;i<=r;i++)
            {
                if('A'<=cake[i][j] && cake[i][j]<='Z')
                {
                    for(int ii=i+1;ii<=r;ii++)
                    {
                        if(cake[ii][j] != '?')
                            break;
                        cake[ii][j] = cake[i][j];
                    }
                }
            }
            for(int i=r;i>=1;i--)
            {
                if('A'<=cake[i][j] && cake[i][j]<='Z')
                {
                    for(int ii=i-1;ii>=1;ii--)
                    {
                        if(cake[ii][j] != '?')
                            break;
                        cake[ii][j] = cake[i][j];
                    }
                }
            }
        }

        printf("Case #%d:\n", tt);
        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
                cout<<cake[i][j];
            cout<<endl;
        }
    }
    return 0;
}