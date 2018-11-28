#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define mt make_tuple
#define ll long long
#define pii pair<int,int>
#define tii tuple <int,int,int>
#define N 100005
#define mod 2000003
#define X first
#define Y second
#define eps 0.0000000001
#define all(x) x.begin(),x.end()
#define tot(x) x+1,x+n+1
using namespace std;
char s[25];
int T,t,n;
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);

    for(int t=1; t<=T; t++) {
        scanf("%s",&s);
        printf("Case #%d: ",t);
        n=strlen(s);
        int j;

        while(1) {
            for(j=0; j<n-1; j++)
                if(s[j]>s[j+1])
                    break;

            if(j==n-1) {
                if(s[0]=='0')
                    printf("%s\n",s+1);
                else
                    printf("%s\n",s);

                break;
            }
            else {
                s[j]--;

                for(++j; j<n; j++)
                    s[j]='9';
            }
        }
    }

    return 0;
}
