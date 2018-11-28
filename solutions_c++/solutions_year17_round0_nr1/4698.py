#include<bits/stdc++.h>
#define ll long long int
#define vii vector<int>
#define vll vector<ll>
#define pb push_back
#define LIM 10000000
#define MOD 1000000007
#define MAX 10000000
#define pi acos(-1)
#define segVar int lft = node << 1 , rgt = (node << 1) + 1 , md = (st+ed) >> 1;
#define pii pair<int,int>
#define EPS 1e-9

using namespace std;

int t,n,k;
char str[1510];

int solve(char *s,int k) {
    int len=strlen(s);
    int flip=0;

    for(int i=0; i<len-k+1; i++) {
        if(s[i]=='-') {
            flip++;
            int cnt=0;
            for(int j=i; cnt<k; j++,cnt++) {
                if(s[j]=='-') s[j]='+';
                else s[j]='-';
            }
        }
    }
    ///EIKHANE KI KORSI BUJHI NAI
    int cnt=0;
    int pcnt=0;

    for(int i=len-1; i>=0; i--) {
        if(cnt==k) break;
        if(s[i]=='+') pcnt++;
        cnt++;
    }
    if(pcnt==k) return flip;
    if(pcnt<k) return -1;
}
int main() {
    ///CONFUSED NOW
    ///WHY DOES IT WORK
    freopen("A-large.in","r",stdin);
    freopen("outal.txt","w",stdout);

    scanf("%d",&t);
    for(int x=1; x<=t; x++) {
        scanf("%s",str);
        scanf("%d",&k);
        printf("Case #%d: ",x);
        int ans=solve(str,k);
        if(ans==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
        str[0]=0;
    }
    return 0;
}
