#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define OK puts("OK")
#define EL printf("\n")
#define sz(A) (int) A.size()
#define end(A) (int) A.size()-1
#define FOR(i,l,r) for (auto i=l;i<=r;i++)
#define FOD(i,l,r) for (auto i=l;i>=r;i--)

int T, k;
string s;

void solve(int test) {
    cin >> s >> k;
    FOR(i,0,end(s)) s[i] = (s[i] == '-' ? '0' : '1');
    int ans = 0;
    FOR(i,0, end(s)-k+1) {
        if (s[i] == '0') {
            ans++;
            FOR(j,i,i+k-1) s[j] = (s[j] == '0' ? '1' : '0');
        }
    }
    int flag = 1;
    FOR(i,0,end(s))
        if (s[i] == '0') flag = 0;

    printf("Case #%d: ", test);
    if (flag) printf("%d\n", ans); else puts("IMPOSSIBLE");
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output-large.txt", "w", stdout);

    cin >> T;
    FOR(test, 1, T) solve(test);

    return 0;
}







