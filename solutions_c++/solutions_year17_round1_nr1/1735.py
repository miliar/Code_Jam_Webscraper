#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sci(fd) scanf("%d",&fd)
#define scll(fd) scanf("%lld",&fd)
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define pii pair < int,int > 
#define pll pair < ll,ll >
#define fi first
#define se second
#define LOGN 20
const ll infi=1000000000000000009;
char ar[30][30];
int h[30];
int visited[30][30];
int n,m;
int lol[4][2]={0,1,0,-1,1,0,-1,0};
bool check(int x,int y)
{
    return (x>=0&&x<n&&y>=0&&y<m);
}
int main()
{
    int t,y=0;
    sci(t);
    while(t--)
    {
        sci(n);
        sci(m);
        int i,j,k,l;
        for(i=0;i<n;i++)
        scanf("%s",ar[i]);
        for(i=0;i<27;i++)
        {
            h[i]=0;
            for(j=0;j<27;j++)
            visited[i][j]=0;
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(ar[i][j]!='?')
                {
                    h[ar[i][j]-'A']=1;
                    int lr=i,rr=i,uc=j,lc=j;
                    queue <pii> q;
                    q.push(mp(i,j));
                    while(!q.empty())
                    {
                        int a=q.front().fi,b=q.front().se;
                        q.pop();
                        for(k=0;k<4;k++)
                        {
                            int c=a+lol[k][0],d=b+lol[k][1];
                            if(visited[c][d]==0&&check(c,d)&&ar[c][d]==ar[i][j])
                            {
                                visited[c][d]=1;
                                lr=min(c,lr);
                                rr=max(c,rr);
                                uc=min(uc,d);
                                lc=max(lc,d);
                                q.push(mp(c,d));
                            }
                        }

                    }
                    for(k=lr;k<=rr;k++)
                    {
                        for(l=uc;l<=lc;l++)
                        ar[k][l]=ar[i][j];
                    }
                }
            }
        }
        for(l=0;l<n;l++)
        {
            for(j=0;j<m;j++)
            {
                if(ar[l][j]!='?')
                break;
            }
            if(j!=m)
            break;
        }
        k=l;
        for(i=l;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(ar[i][j]!='?')
                break;
            }
            if(j==m)
            {   
                for(j=0;j<m;j++)
                ar[i][j]=ar[i-1][j];
            }
            else
            {
                for(l=j-1;l>=0;l--)
                {
                    if(ar[i][l]=='?')
                    ar[i][l]=ar[i][l+1];
                }
                for(l=j+1;l<m;l++)
                {
                    if(ar[i][l]=='?')
                    ar[i][l]=ar[i][l-1];
                }
            }
        }

        for(i=k-1;i>=0;i--)
        {
            for(j=0;j<m;j++)
            ar[i][j]=ar[i+1][j];
        }
        y++;
        printf("Case #%d:\n",y);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            printf("%c",ar[i][j]);
            printf("\n");
        }
    }
    return 0;
}