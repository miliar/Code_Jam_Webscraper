#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
#define inf (1<<30)
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};

char str[10005];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    //ios_base::sync_with_stdio(false);
    int ncase, tcase = 1, k, i;
    scanf("%d", &ncase);
    while(ncase--) {
        scanf("%s %d", str, &k);
        int len = strlen(str);
        int ans = 0;
        for(i = 0; i < len; i++) {
            if(i+k-1 < len) {
                if(str[i] == '-') {
                    ans++;
                    for(int j = i+1; j < i+k; j++) {
                        if(str[j] == '-') str[j] = '+';
                        else str[j] = '-';
                    }
                }
            }
            else if(str[i] == '-') break;
        }
        if(i == len) {
            printf("Case #%d: %d\n", tcase++, ans);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", tcase++);
        }
    }
    return 0;
}



