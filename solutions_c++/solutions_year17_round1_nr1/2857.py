#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
int n,m;
int a[30][30],sum[30][30],used[30][30];
bool all_unknown_except_one(int x0,int y0,int x1,int y1)
{
    return sum[x1][y1]-(sum[x1][y0-1]+sum[x0-1][y1]-sum[x0-1][y0-1])==(x1-x0+1)*(y1-y0+1)-1;
}
typedef pair<pair<pair<pair<int,int>,pair<int,int> >,pair<int,int> >,int> mytuple;
vector<mytuple> table;
mytuple extend(int x,int y)
{
    for (int i=1;i<=x;i++)
        for (int j=1;j<=y;j++)
            if (all_unknown_except_one(i,j,x,y))
                for (int k=n;k>=x;k--)
                    for (int l=m;l>=y;l--)
                        if (all_unknown_except_one(i,j,k,l))
                        {
                            /*for (int kk=i;kk<=k;kk++)
                                for (int ll=j;ll<=l;ll++)
                                {
                                    a[kk][ll]=a[x][y];
                                    used[kk][ll]=1;
                                }*/
                            return make_pair(make_pair(make_pair(make_pair(i,j),make_pair(k,l)),make_pair(x,y)),(k-i+1)*(l-j+1)-1);
                        }
    return make_pair(make_pair(make_pair(make_pair(0,0),make_pair(0,0)),make_pair(x,y)),-1);
}
void fill(pair<pair<pair<int,int>,pair<int,int> >,pair<int,int> > todo)
{
    for (int kk=todo.first.first.first;kk<=todo.first.second.first;kk++)
        for (int ll=todo.first.first.second;ll<=todo.first.second.second;ll++)
        {
            a[kk][ll]=a[todo.second.first][todo.second.second];
            used[kk][ll]=1;
        }
}
int comp(const mytuple &x,const mytuple &y)
{
    return y.second-x.second;
}
int main()
{
    //freopen("a.txt","r",stdin);
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int testcase=1;testcase<=test;testcase++)
    {
        memset(used,0,sizeof(used));
        scanf("%d%d",&n,&m);
        int tot=0;
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
            {
                char ch;
                cin>>ch;
                if (ch=='?')
                {
                    tot++;
                    a[i][j]=-1;
                }
                else a[i][j]=ch-'A';
            }
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
                sum[i][j]=sum[i][j-1]+sum[i-1][j]-sum[i-1][j-1]+(a[i][j]==-1);
        while (tot)
        {
            bool flag=true;
            memset(sum,0,sizeof(sum));
            for (int i=1;i<=n;i++)
                for (int j=1;j<=m;j++)
                    sum[i][j]=sum[i][j-1]+sum[i-1][j]-sum[i-1][j-1]+(a[i][j]==-1);
            table.clear();
            for (int i=1;i<=n && tot && flag;i++)
                for (int j=1;j<=m && tot && flag;j++)
                    if (a[i][j]!=-1 && !used[i][j])
                    {
                        //tot-=extend(i,j);
                        //flag=false;
                        auto ret=extend(i,j);
                        if (ret.second>0) table.push_back(extend(i,j));
                    }
            sort(table.begin(),table.end(),comp);
            fill(table[0].first);
            tot-=table[0].second;
            /*printf("==show==\n");
            for (int i=1;i<=n;i++)
            {
                for (int j=1;j<=m;j++)
                    printf("%c",a[i][j]+'A');
                printf("\n");
            }*/
        }
        printf("Case #%d:\n",testcase);
        for (int i=1;i<=n;i++)
        {
            for (int j=1;j<=m;j++)
                printf("%c",a[i][j]+'A');
            printf("\n");
        }
    }
    return 0;
}
