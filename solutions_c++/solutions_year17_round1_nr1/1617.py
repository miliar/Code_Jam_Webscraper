#include<bits/stdc++.h>
using namespace std;
#define loop(i,L,R) for(int i=(L);i<=(R);i++)
#define rept(i,L,R) for(int i=(L);i<(R);i++)
#define isc(n) scanf("%d",&n)
#define llsc(n) scanf("%lld",&n)
#define dsc(n) scanf("%lf",&n)
#define enl cout<<endl
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define xx first
#define yy second
typedef long long ll;
typedef pair<int,int>PI;
typedef pair<pair<int,int>,int>PII;


char grid[100][100];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=0;
    isc(t);
    while(t--)
    {
        int r,c;
        isc(r);
        isc(c);
        rept(i,1,r+1)
        {
            rept(j,1,c+1)
            {
                cin>>grid[i][j];
            }
        }


        rept(i,1,r+1)
        {
            rept(j,1,c+1)
            {
                if(grid[i][j]!='?')
                {
                    int k=j+1;
                    while(k<=c && grid[i][k]=='?')grid[i][k++]=grid[i][j];
                }
            }
        }

        rept(i,1,r+1)
        {
            if(grid[i][1]=='?')
            {
                int k=1;
                while(k<=c && grid[i][k]=='?')k++;
                if(k<=c)
                {
                    for(int j=1;j<k;j++)grid[i][j]=grid[i][k];
                }
                else if(i>1)
                {
                    for(int j=1;j<=c;j++)grid[i][j]=grid[i-1][j];
                }
            }
        }

        for(int i=r-1;i>=1;i--)
        {
            if(grid[i][1]=='?')
            {

                for(int j=1;j<=c;j++)grid[i][j]=grid[i+1][j];
            }
        }
        cout<<"Case #"<<++cas<<":"<<endl;
        rept(i,1,r+1)
        {
            rept(j,1,c+1)
            {
                cout<<grid[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}
