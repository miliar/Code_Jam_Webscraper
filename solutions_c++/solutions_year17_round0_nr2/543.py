#include <bits/stdc++.h>

#define FO(i,a,b) for (int i=a;i<b;i++)
#define sz(v) int(v.size())

using namespace std;

int main() {
    int t; scanf("%d", &t);
    FO(z,0,t) {
        string s;
        cin >> s;
        long long n = stoll(s);
        FO(i,0,sz(s)) {
            bool gd = true;
            FO(j,i,sz(s)) if (s[j] != s[i]) {
                gd = s[j] > s[i];
                break;
            }

            if (!gd) {
                s[i]--;
                FO(j,i+1,sz(s)) s[j] = '9';
                goto end;
            }
        }
        end:;
        long long x = stoll(s);
        printf("Case #%d: %lld\n", z+1, x);
    }
}

