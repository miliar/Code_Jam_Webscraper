/*
ID: notunsh1
LANG: C++
TASK: wormhole
*/
#include <bits/stdc++.h>

using namespace std;

#define rep(i,a,b) for(int i=a;i<=b;i++)
#define pii pair<int,int>
#define pll pair<long long,long long>
#define pb push_back
#define mod 1000000007
#define ll long long
#define mem(a) memset(a,0,sizeof a)
#define memd(a) memset(a,-1,sizeof a)
#define X first
#define Y second
#define ull unsigned long long
#define sc(n) scanf("%d",&n)

ll pow10[19];

void power()
{
    pow10[0]=1;
    ll prod  = 1;
    rep(i,1,18)
    {
        prod*=10;
        pow10[i]=prod;
    }
}

ll dp[20][2][10];
int dig;
char s[25];

ll rec(int pos,int is,int prev)
{
    if(pos == dig)return 0;

    ll &r = dp[pos][is][prev];

    if(r!=-1)return r;
    r = -1000000000000000000;
    if(is)r = 9*pow10[dig-1-pos]+rec(pos+1,1,9);
    else if(pos==0)
    {
        if(s[0]=='1')r = pow10[dig-1]+rec(pos+1,0,1);
        else r = max((s[0]-'0')*pow10[dig-1]+rec(pos+1,0,s[0]-'0'),(s[0]-'0'-1)*pow10[dig-1]+rec(pos+1,1,s[0]-'0'-1));
    }
    else
    {
        rep(i,prev,s[pos]-'0')
        {
            bool yu;
            if(i<s[pos]-'0')yu=1;
            else yu=0;
            r = max(r,i*pow10[dig-1-pos]+rec(pos+1,yu,i));
        }
    }
    return r;
}

int main()
{
    power();
    FILE *fp1 = fopen("B-large.in","r");
    FILE *fp2 = fopen("kochu.txt","w");
    int cases;
    fscanf(fp1,"%d",&cases);
    int u=0;
    while(++u<=cases)
    {
        fscanf(fp1,"%s",s);
        //getchar();
        dig = strlen(s);
        memd(dp);
        ll ans = rec(0,0,0);
        if(ans>0)fprintf(fp2,"Case #%d: %lld\n",u,ans);
        else
        {
            fprintf(fp2,"Case #%d: ",u);
            rep(i,0,dig-2)fprintf(fp2,"9");
            fprintf(fp2,"\n");
        }
    }
    fclose(fp1);
    fclose(fp2);
}
