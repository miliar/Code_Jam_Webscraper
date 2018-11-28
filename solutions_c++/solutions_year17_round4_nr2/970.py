#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
#define mod 1000000007

int cas=0,t,arr[1005],p,b,n,c,m,i,rides,j,promotions;
std::vector<int>adj[1005];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        cas++;
        scanf("%d %d %d",&n,&c,&m);
  // if(cas == 43) cout << n << " " << c << " " <<m << "\n";
        for(i=0;i<=1000;i++)
            adj[i].clear();
        for(int i=0; i<m; i++)
        {
            scanf("%d %d",&p,&b);
         //   if(cas == 43)
         //    cout << b << " " << p <<"\n";
            b--;
            adj[b].push_back(p);

        }

        rides=0;
        for(i=0; i<c; i++)
            rides=max(rides,(int)adj[i].size());

        for(i=1; i<=n; i++)
            arr[i]=rides;

        for(i=0; i<=c; i++)
            for(j=0; j<adj[i].size(); j++)
                arr[adj[i][j]]-=1;

        // printf("\n");
        //for(i=1;i<=n;i++)
          //  printf("%d ",arr[i]);
        //printf("\n");

        promotions=0;
        while(1)
        {
            int sum=0,add=0;
            for(i=1; i<=n; i++)
            {
                if(arr[i]<0)
                {
                    if(arr[i]*(-1)>sum)
                    {
                        add= (arr[i]*(-1) - sum);
                        rides+= (arr[i]*(-1)-sum);
                        break;
                    }
                    else
                    {
                        promotions += arr[i]*(-1);
                        sum= sum+arr[i];
                    }
                }
                else
                    sum+=arr[i];
            }

            if(i>n)
                break;
            for(i=1;i<=n;i++)
                arr[i]+=add;
            promotions=0;
        }

        printf("Case #%d: %d %d\n",cas,rides,promotions);
    }
    return 0;
}
