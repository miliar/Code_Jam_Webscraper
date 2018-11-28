#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;

char s[1010];
int k, a[1010], ans;
bool res;

int main() {
    freopen("A-large.in", "rb", stdin);
    freopen("out.txt", "wb", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%s %d", s, &k);
        memset(a, 0, sizeof a);
        int l = strlen(s);
        ans = 0;
        res = true;
        for (int i = 0; i < l; ++ i) {
            if (s[i] == '-') a[i]++;
            if (a[i] % 2 == 1) {
                ans ++;
                if (i + k - 1 >= l) {
                    res = false;
                    break;
                }
                for(int j = 0; j < k ; ++ j) {
                    a[i + j] ++;
                }
            }
        }
        
        for (int i = 0; i < l; ++ i) {
            if (a[i] % 2 == 1) {
                res = false;
                break;
            }
        }
        cout<<"Case #"<<cas<<": ";
        if (res) {
            cout<<ans<<endl;
        } else {
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
