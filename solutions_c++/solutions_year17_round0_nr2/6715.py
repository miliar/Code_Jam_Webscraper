#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
using namespace std;
typedef long long ll;
const int inf = 1e9;
const ll infLL = 1e18;

int i, t, T, len;
char a[20];

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    scanf("%d",&T);
    for (t = 1; t <= T; t++) {
        scanf (" %s",a);
        len = strlen (a);
        for (i=0; i<len; i++) a[i] = a[i]-'0';
        while (true) {
            for (i = 1; i < len; i++) {
                if(a[i-1]>a[i]) break;
            }
            if(i < len) {
                a[i-1]--;
                for (;i<len;i++)
                    a[i] = 9;
            } else break;
        }
        i = 0; while(a[i]==0) i++;
        printf("Case #%d: ",t);
        for (;i<len; i++) printf("%d",a[i]);
        printf("\n");
    }
    return 0;
}
