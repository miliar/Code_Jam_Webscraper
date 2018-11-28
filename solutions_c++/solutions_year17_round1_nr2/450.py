#include <iostream>
#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;
typedef long long Int;

int n,p;
int t;
int req[111];

pair<int,int> seq[111][111];

bool Big(Int a,Int b)
{
    return a*100LL>b*110LL;
}

bool Small(Int a,Int b)
{
    return a*100LL<b*90LL;
}

pair<int,int> GetSeg(int val,int reqval)
{
    int l,r,mid,best=-1;
    pair<int,int> ans;

    l=0;
    r=1500001;

    while(l<=r)
    {
        mid=(l+r)/2;

        if ( Big( (Int)val,(Int)mid*(Int)reqval ) )
        {
            l=mid+1;
        }
        else if ( Small( (Int)val,(Int)mid*(Int)reqval ) )
        {
            r=mid-1;
        }
        else
        {
            best=mid;
            r=mid-1;
        }
    }

    if (best==-1)
    return make_pair(-1,-1);

    ans.first=best;

    l=0;
    r=1500001;
    best=-1;

    while(l<=r)
    {
        mid=(l+r)/2;

        if ( Big( (Int)val,(Int)mid*(Int)reqval ) )
        {
            l=mid+1;
        }
        else if ( Small( (Int)val,(Int)mid*(Int)reqval ) )
        {
            r=mid-1;
        }
        else
        {
            best=mid;
            l=mid+1;
        }
    }

    ans.second=best;

    return ans;
}

vector< pair<int,int> > Added[1500111];
vector< pair<int,int> > Removed[1500111];

bool Taken[111][111];
int RowCtr[111];
bool Active[111][111];
int ans=0;

void Kill(int x,int y)
{
    Taken[x][y]=true;
    RowCtr[x]--;
    Active[x][y]=false;

    return;
}

void Perform()
{
    int i,j;
    int minend,choice;

    for (i=1;i<=n;i++)
    {
        choice=-1;
        for (j=1;j<=p;j++)
        {
            if (Active[i][j])
            {
                if (choice==-1 || seq[i][j].second<minend)
                {
                    minend=seq[i][j].second;
                    choice=j;
                }
            }
        }

        //cout<<"Choosing "<<i<<","<<choice<<endl;
        Kill(i,choice);
    }

    ans++;

    return;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int test;
    int i,j;
    int val;
    bool bad;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        fprintf(stderr,"Solving test %d\n",test);

        for (i=0;i<=1500000;i++)
        {
            if (!Added[i].empty())
            Added[i].clear();
            if (!Removed[i].empty())
            Removed[i].clear();
        }

        memset(Taken,false,sizeof(Taken));
        memset(RowCtr,0,sizeof(RowCtr));
        memset(Active,false,sizeof(Active));
        ans=0;

        scanf("%d %d",&n,&p);

        for (i=1;i<=n;i++)
        {
            scanf("%d",&req[i]);
        }

        for (i=1;i<=n;i++)
        {
            for (j=1;j<=p;j++)
            {
                scanf("%d",&val);

                seq[i][j]=GetSeg(val,req[i]);

                if (seq[i][j].first!=-1)
                {
                    Added[ seq[i][j].first ].push_back(make_pair(i,j));
                    Removed[ seq[i][j].second+1 ].push_back(make_pair(i,j));
                }
            }
        }

        for (i=1;i<=1500000;i++)
        {
            for (j=0;j<Added[i].size();j++)
            {
                //cout<<"Adding "<<Added[i][j].first<<";"<<Added[i][j].second<<" at "<<i<<endl;

                RowCtr[ Added[i][j].first ]++;
                Active[ Added[i][j].first ][ Added[i][j].second ]=true;
            }

            for (j=0;j<Removed[i].size();j++)
            {
                if (!Taken[ Removed[i][j].first ][ Removed[i][j].second ])
                {
                    Active[ Removed[i][j].first ][ Removed[i][j].second ]=false;
                    RowCtr[ Removed[i][j].first ]--;
                }
            }

            if (!Added[i].empty() || !Removed[i].empty())
            {
                while(1)
                {
                    //cout<<"HERE"<<endl;

                    bad=false;
                    for (j=1;j<=n;j++)
                    {
                        if (RowCtr[j]==0)
                        {
                            bad=true;
                            break;
                        }
                    }

                    if (!bad)
                    {
                        //cout<<"Cool shit"<<endl;
                        Perform();
                    }
                    else
                    break;
                }
            }
        }

        printf("Case #%d: %d\n",test,ans);

        //cout<<"t="<<t<<endl;
    }

    return 0;
}
