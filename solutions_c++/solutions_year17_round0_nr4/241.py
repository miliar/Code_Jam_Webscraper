#include <bits/stdc++.h>
using namespace std;


vector<int> gra[505];
bool vis[505];
int p[505];
bool find(int s)
{
	for(int i=0;i<gra[s].size();i++)
		if(vis[gra[s][i]]==0&&p[gra[s][i]]!=s)
		{
			vis[gra[s][i]]=1;
			if(p[gra[s][i]]==0 || find(p[gra[s][i]]))
			{
				p[gra[s][i]]=s;
				return 1;
			}
		}
	return 0;
}
int max_match(int n)
{
	int ans=0;
	memset(p,0,sizeof(p));
	for(int i=1;i<=n;i++)
	{
		memset(vis,0,sizeof(vis));
		ans+=find(i);
	}
	return ans;
}

int mat[205][205];
int ans[205][205];
bool r[205],c[205];
bool d1[205],d2[205];
vector<pair<int,pair<int,int> > >poi;
int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",ti++);
        int n,m,sum=0;
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                mat[i][j]=ans[i][j]=0;
        for(int i=1;i<=2*n;i++)
        {
            r[i]=c[i]=0;
            d1[i]=d2[i]=0;
        }
        for(int i=0;i<m;i++)
        {
            int x,y;
            char s[5];
            scanf("%s%d%d",s,&x,&y);
            sum++;
            if(s[0]=='+')
            {
                mat[x][y]=1;
                d1[x+y-1]=1;
                d2[x-y+n]=1;
            }
            else if(s[0]=='x')
            {
                mat[x][y]=2;
                r[x]=1;
                c[y]=1;
            }
            else
            {
                mat[x][y]=3;
                d1[x+y-1]=1;
                d2[x-y+n]=1;
                r[x]=1;
                c[y]=1;
                sum++;
            }
        }
        for(int i=1;i<=n;i++)
            gra[i].clear();
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(r[i]==0&&c[j]==0)
                    gra[i].push_back(j);
        sum+=max_match(n);
        for(int i=1;i<=n;i++)
            if(p[i])
                ans[p[i]][i]|=2;
        for(int i=1;i<=2*n;i++)
            gra[i].clear();
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
            {
                int x=i+j-1,y=i-j+n;
                if(d1[x]==0&&d2[y]==0)
                    gra[x].push_back(y);
            }
        sum+=max_match(2*n);
        for(int i=1;i<=2*n;i++)
            if(p[i])
            {
                int x=p[i],y=i;
                ans[(x+y-n+1)/2][(x-y+n+1)/2]|=1;
            }
        printf("%d ",sum);
        poi.clear();
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(ans[i][j])
                {
                    if(ans[i][j]==3||mat[i][j])
                        poi.push_back({3,{i,j}});
                    else
                        poi.push_back({ans[i][j],{i,j}});
                }
        printf("%d\n",(int)poi.size());
        for(int i=0;i<poi.size();i++)
        {
            char s[5];s[1]=0;
            if(poi[i].first==1)
                s[0]='+';
            else if(poi[i].first==2)
                s[0]='x';
            else
                s[0]='o';
            printf("%s %d %d\n",s,poi[i].second.first,poi[i].second.second);
        }
    }
    return 0;
}
