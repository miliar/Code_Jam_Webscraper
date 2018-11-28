
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned ll
#define db double
#define InF 0x3f3f3f3f
#define mOD 1000000007
#define PII pair<int, int>

const string INPUT_FILE="input.txt";
const string OUTPUT_FILE="b.txt";

int t,n;
char buf[20];
int digits[20];

bool dfs(int idx,int last) {//printf("idx:%d last:%d\n",idx,last);
    if (idx==n) return true;
    if (digits[idx]>=last) {
        if (dfs(idx+1,digits[idx])) return true;
        else {
            digits[idx]--;
            for (int i=idx+1;i<n;i++) digits[i]=9;
            if (digits[idx-1]<=digits[idx]) return true;
            return false;
        }
    }
    return false;
}

ll solve() {
    n=strlen(buf);
    for (int i=0;i<n;i++) digits[i]=buf[i]-'0';
    dfs(0,0);
    ll ans=0;
    for (int i=0;i<n;i++) {
        ans=ans*10+digits[i];
    }
    return ans;
}

int main() {

    freopen(INPUT_FILE.c_str(),"r",stdin);
    freopen(OUTPUT_FILE.c_str(),"w",stdout);

    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++) {
        memset(buf,0,sizeof(buf));
        memset(digits,0,sizeof(digits));
        scanf("%s",buf);
        printf("Case #%d: %lld\n",tt,solve());
    }
}