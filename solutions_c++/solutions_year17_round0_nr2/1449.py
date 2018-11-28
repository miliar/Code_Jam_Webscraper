#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
#define int long long
using namespace std;

const int nmax = 100010;
int n, k, p, x, y, cnt[nmax], cnt2[nmax];
int dp[30][10][3], u[30][10][3], timer=0;
int v[30], sz=0;

bool check(int x){
    int last = 1000;
    while (x){
        int dig= x%10;
        if (dig>last) return 0;
        last=dig;
        x/=10;
    }
    return 1;
}

int f(int pos, int last, int b){
    for (int j=0; j<=9; j++)
    for (int k=0; k<=2; k++)
    dp[sz][j][k]=1;

    for (int pos=sz-1; pos>=0; pos--)
    for (int last=0; last<=9; last++)
    {
     dp[pos][last][0]=0;
        for (int curr=last; curr<=9; curr++) dp[pos][last][0]+=dp[pos+1][curr][0];
     dp[pos][last][1]=0;
     for (int curr=last; curr<=v[pos]; curr++)
        dp[pos][last][1]+=dp[pos+1][curr][(curr==v[pos] ? 1 : 0)];


    }
    return dp[1][0][1];

    if (pos==sz) return 1;
    if (u[pos][last][b]==timer) return dp[pos][last][b];
    int ans=0;
    u[pos][last][b]=timer;
    if (b==0){
    for (int curr=last; curr<=9; curr++)
        ans+=f(pos+1, curr, 0);
    }
    if (b==1){
        for (int curr=last; curr<=v[pos]; curr++)
        ans+=f(pos+1, curr, (curr==v[pos] ? 1 : 0));
    }
    return dp[pos][last][b]=ans;
}

int calc(int x){
    timer++;
sz=0;
    while (x){
        v[sz++]=x%10;
        x/=10;
    }
    v[sz++]=(0);
    reverse(v, v+sz);
    return f(1, 0, 1)-1;
}

int brute(int x){
    int ans=x;
    while (!check(ans)) ans--;
    return ans;
}

int cool(int x){
    int l=1, r = x;
    while (l+1<r){
        int mid = (l+r) >> 1;
        if (calc(r)-calc(mid-1)>0) l=mid; else r=mid;
    }
    while (!check(r)) r--;
    return r;
}


main(){
//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);
int ans=0;
int t;
    cin >> t;
    int numer=0;
    while (t--){
        numer++;
        cin >> x;
        cout << "Case #" << numer << ": " <<  cool(x) << endl;
    }

}
