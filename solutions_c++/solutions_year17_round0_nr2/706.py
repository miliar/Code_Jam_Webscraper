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

int T;
string s;

void solve(int test) {
    cin >> s;
    int k = sz(s);
    FOD(i,end(s),1) {
        if (s[i] < s[i-1]) {
            s[i-1]--; s[i] = '9'; k = i;
        }
    }
    while (sz(s) > 0 && s[0] == '0') {
        s.erase(0,1); k--;
    }
    FOR(i,k,end(s)) s[i] = '9';
    printf("Case #%d: ", test); cout << s << endl;
}

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("output-large.txt", "w", stdout);

    cin >> T;
    FOR(test, 1, T) solve(test);

    return 0;
}







