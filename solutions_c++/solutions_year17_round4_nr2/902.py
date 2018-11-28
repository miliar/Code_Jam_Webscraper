#include<bits/stdc++.h>
using namespace std;


int mat[1050][50];

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        int n,c,m;
        scanf("%d%d%d",&n,&c,&m);
        memset(mat,0,sizeof(mat));
        for(int i=0;i<m;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            mat[x][y]++;
            if(x>1)
                mat[0][y]++;
        }
        int ans1=0,ans2=0;
        mat[0][2]-=min(mat[1][1],mat[0][2]);
        mat[0][1]-=min(mat[1][2],mat[0][1]);
        ans1+=max(mat[0][1],mat[0][2]);
        if(mat[0][1]>0&&mat[0][2]>0)
        {
            if(mat[0][1]<mat[0][2])
            {
                for(int i=0;i<=n;i++)
                    swap(mat[i][1],mat[i][2]);
            }
            mat[0][1]+=mat[1][2];
            mat[0][2]+=mat[1][1];
            mat[0][1]+=mat[1][1];
            mat[0][2]+=mat[1][2];
            for(int i=2;i<=n;i++)
                ans2+=max(0,mat[i][2]+mat[i][1]-mat[0][1]);
        }
        ans1+=mat[1][1]+mat[1][2];
        printf("Case #%d: %d %d\n",ti++,ans1,ans2);
    }
	return 0;
}

