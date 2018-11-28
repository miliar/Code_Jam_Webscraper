#include <bits/stdc++.h>
#define ff first
#define ss second
#define pi 3.14159265359
using namespace std;
typedef long long ll;
int dp[1441][1441][3][2];
int a1[1441];
int a2[1441];


int solve(int idx , int dtime , int f ,int z){
    if(dtime > 720)return 1e8;
    if(idx == 1440){
        if(dtime == 720)return z != f;
        return 1e8;
    }
    int &ret = dp[idx][dtime][f][z];
    if(ret != -1)
        return ret;
    ret = 1e8;
    if(!a1[idx]){
        ret = min(ret , solve(idx+1,dtime+1,0,(idx == 0)? 0 : z) + (f != 0) );
    }
    if(!a2[idx]){
        ret = min(ret , solve(idx+1,dtime,1,(idx == 0)? 1 : z) + (f != 1) );
    }
    return ret;
}



int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b-large-out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int I = 1 ; I <= t ; I ++){
        int n,k;
        memset(a1 , 0 , sizeof a1);
        memset(a2 , 0 , sizeof a2);
        memset(dp , -1 , sizeof dp);
        cin >> n >> k;
        for(int i = 0 ; i < n ; i++){
            int l,r;
            cin >> l >> r;
            for(int j = l ; j < r ; j++)
                a1[j] = 1;
        }
        for(int i = 0 ; i < k ; i++){
            int l,r;
            cin >> l >> r;
            for(int j = l ; j < r ; j++)
                a2[j] = 1;
        }
        printf("Case #%d: %d\n",I,solve(0,0,2,0)-1);
    }
    return 0;
}
