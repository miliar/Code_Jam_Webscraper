#include <iostream>
#include <vector>
#include <memory.h>
using namespace std;

char a[30][30];
int r,c;
vector<int> vx,vy;

bool checkcol(int u, int d, int y, char ch)
{
    for(int i=d;i<=u;i++)
        if(a[i][y]!='?') return false;
    for(int i=d;i<=u;i++)
        a[i][y]=ch;
    return true;
}

void apnd(int x, int y)
{
    int l,r,u,d;
    d=x-1;
    while(a[d][y]=='?')
    {
        a[d][y]=a[x][y];
        d--;
    }
    d++;
    u=x+1;
    while(a[u][y]=='?')
    {
        a[u][y]=a[x][y];
        u++;
    }
    u--;
    l=y-1;
    while(checkcol(u,d,l,a[x][y])) l--;
    l++;
    r=y+1;
    while(checkcol(u,d,r,a[x][y])) r++;
    r--;
}

void mymain(int t)
{
    int i,j;
    cin>>r>>c;
    memset(a,0,sizeof(a));
    vx.clear();
    vy.clear();
    for(i=1;i<=r;i++)
        for(j=1;j<=c;j++)
        {
            cin>>a[i][j];
            if(a[i][j]>='A' && a[i][j]<='Z')
            {
                vx.push_back(i);
                vy.push_back(j);
            }
        }

    for(i=0;i<vx.size();i++)
        apnd(vx[i],vy[i]);
    cout<<"Case #"<<t<<":"<<endl;
    for(i=1;i<=r;i++)
    {
        for(j=1;j<=c;j++)
            cout<<a[i][j];
        cout<<endl;
    }
}

int main()
{
    int T,t;
    cin>>T;
    for(t=0;t<T;t++) mymain(t+1);
    return 0;
}
