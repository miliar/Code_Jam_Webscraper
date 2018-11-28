//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;


char a[30][30],z;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream cin ("input.in");
    ofstream cout("output.txt");

    int T,r,c,l;
    cin>>T;


    for(int t1=1;t1<=T;t1++)
    {
        cout<<"Case #"<<t1<<":\n";

        cin>>r>>c;
        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                cin>>a[i][j];
            }
        }

        for(int j=1;j<=c;j++)
        {
            l=0;

            for(int i=1;i<=r;i++)
            {
                if(a[i][j]!='?'){z=a[i][j];l=1;break;}
            }
            if(l==0)continue;

            for(int i=1;i<=r;i++)
            {
                if(a[i][j]=='?')a[i][j]=z;
                else z=a[i][j];
            }
        }




        for(int j=2;j<=c;j++)
        {
            l=0;

            for(int i=1;i<=r;i++)
            {
                if(a[i][j]!='?'){z=a[i][j];l=1;break;}
            }
            if(l==1)continue;

            for(int i=1;i<=r;i++)a[i][j]=a[i][j-1];
        }

        for(int j=c-1;j>=1;j--)
        {
            l=0;

            for(int i=1;i<=r;i++)
            {
                if(a[i][j]!='?'){z=a[i][j];l=1;break;}
            }
            if(l==1)continue;

            for(int i=1;i<=r;i++)a[i][j]=a[i][j+1];
        }

        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                cout<<a[i][j];
            }
            cout<<"\n";
        }

    }

    return 0;
}

