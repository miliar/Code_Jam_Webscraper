/*************************************************************************
	> File Name: A.cpp
	> Author: tyxxzjpdez
	> Mail: tyxxzjpdez@163.com
	> Created Time: 2017年04月30日 星期日 16时59分46秒
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

const double pi=acos(-1.0);
const int maxn=1000+10;
int n,k;
double dp[maxn][maxn];

struct Node{
    int R,H;
    bool operator<(const Node& rhs)const{
        return R>rhs.R;
    }
};

Node arr[maxn];

int main(){
    //ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;scanf("%d",&T);;
    for(int kase=1;kase<=T;kase++){
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++)
            scanf("%d%d",&arr[i].R,&arr[i].H);
        sort(arr+1,arr+n+1);
        memset(dp,0,sizeof(dp));
        dp[1][1]=2.0*arr[1].R*arr[1].H+1.0*arr[1].R*arr[1].R;
        for(int i=2;i<=n;i++){
            for(int j=1;j<=i;j++)
                if(j==1)
                    dp[i][j]=max(dp[i-1][j],2.0*arr[i].R*arr[i].H+1.0*arr[i].R*arr[i].R);
                else
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2.0*arr[i].R*arr[i].H);    
        }
        double ans=-1.0;
        printf("Case #%d: %.9f\n",kase,dp[n][k]*pi);
    }
    return 0;
}
