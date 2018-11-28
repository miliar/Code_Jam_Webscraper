#include <map>
#include <set>
#include <tuple>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <cstdio>
#include <memory>
#include <cctype>
#include <bitset>
#include <string>
#include <vector>
#include <climits>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <functional>
#define fuck(x) cout<<"["<<x<<"]";
#define FIN freopen("input.txt","r",stdin);
#define FOUT freopen("output.txt","w+",stdout);
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int INF = 0x3f3f3f3f;
const int mod = 1e9 + 7;
const int MX = 1e4 + 5;

char S[MX];
int flip[MX], m;

int main() {
    FIN; FOUT;
    int T, ansk = 0;
    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++ansk);
        scanf("%s%d", S + 1, &m);
        int len = strlen(S + 1);

        int ans = 0, now = 0;
        for(int i = 1; i + m - 1 <= len; i++) {
            int x = S[i] == '+';
            x ^= now;
            if(!x) {
                flip[i] = 1;
                now ^= 1;
                ans++;
            } else flip[i] = 0;
            if(i - m + 1 >= 1) now ^= flip[i - m + 1];
        }

        bool sign = true;
        for(int i = len - m + 2; i <= len; i++) {
            int x = S[i] == '+';
            x ^= now;
            if(!x) {
                sign = false;
                break;
            }
            now ^= flip[i - m + 1];
        }
        if(sign) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}