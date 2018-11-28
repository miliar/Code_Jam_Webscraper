#include<bits/stdc++.h>
using namespace std;
#define PI 3.141592654
#define maxn 1005
vector<pair<int,int> >s;
bool stsort(pair<int,int>e1,pair<int,int>e2){
    return e1.first>e2.first;
}
double dp[maxn][maxn];
int main(){
    FILE *fp1 = fopen("C:\\Users\\Hmc1994\\Downloads\\A-large.in","r+");
    FILE *fp2 = fopen("C:\\Users\\Hmc1994\\Downloads\\ans.out","w+");
    int t;
    fscanf(fp1,"%d",&t);
    int ansn=1;
    while(t--){
        int n,k;
        fscanf(fp1,"%d%d",&n,&k);
        int r,h;
        s.clear();
        memset(dp,0,sizeof(dp));
        for(int i=1;i<=n;i++){
            fscanf(fp1,"%d%d",&r,&h);
            s.push_back(make_pair(r,h));
            sort(s.begin(),s.end(),stsort);
        }
        double sz;
        for(int i=0;i<n;i++){
            for(int j=1;j<=k && j<=i+1;j++){
                if(j!=1){
                    sz=(double)s[i].first*PI*2.0*s[i].second;
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+sz);
                }
                if(j==1){
                    sz=(double)s[i].first*PI*2.0*s[i].second+(double)PI*s[i].first*s[i].first;
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+sz);
                }

            }
        }
        fprintf(fp2,"Case #%d: %.8lf\n",ansn++,dp[n-1][k]);
    }
}
