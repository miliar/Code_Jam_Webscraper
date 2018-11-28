
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned ll
#define db double
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define PII pair<int, int>

const string INPUT_FILE = "input.txt";
const string OUTPUT_FILE = "a.txt";

int t,k;
char buf[1005];

int solve() {
    int ret=0;
    int n=strlen(buf);
    for (int i=0;i+k-1<n;i++) {
        if (buf[i]=='-') {
            for (int j=0;j<k;j++) {
                if (buf[i+j]=='-') buf[i+j]='+';
                else buf[i+j]='-';
            }
            ret++;
        }
    }
    bool flag=false;
    for (int i=n-k;i<n;i++) {
        if (buf[i]=='-') flag=true;
    }
    if (flag) return -1;
    else return ret;
}

int main() {

    freopen(INPUT_FILE.c_str(), "r", stdin);
    freopen(OUTPUT_FILE.c_str(), "w", stdout);

    scanf("%d\n",&t);
    for (int tt=1;tt<=t;tt++) {
        memset(buf,0,sizeof(buf));
        scanf("%s",buf);
        scanf("%d",&k);
        printf("Case #%d: ",tt);
        int ans=solve();
        if (ans==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
}