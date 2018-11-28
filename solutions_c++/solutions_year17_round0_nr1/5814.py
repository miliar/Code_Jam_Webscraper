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

vector<int>par[1001];
map<string,int>ma;

int main()
{
    FILE *fp1 = fopen("A-large.in","r");
    FILE *fp2 = fopen("kochu.txt","w");
    int cases;
    fscanf(fp1,"%d",&cases);
    int u=0;
    while(++u<=cases)
    {
        char s[1005];
        int k;
        fscanf(fp1,"%s %d",&s,&k);
        bool is = 1;
        int ans = 0;
        int ln = strlen(s);
        rep(i,0,ln-k)
        {
            if(s[i]=='+');
            else
            {
                rep(j,i,i+k-1)
                {
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
                }
                ans++;
            }
        }
        rep(i,0,ln-1)
        {
            if(s[i]=='-')
            {
                is=0;
                break;
            }
        }
        if(is)fprintf(fp2,"Case #%d: %d\n",u,ans);
        else fprintf(fp2,"Case #%d: IMPOSSIBLE\n",u);
    }
    fclose(fp1);
    fclose(fp2);
}
