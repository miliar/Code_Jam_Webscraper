#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int casenum, len;
int d[1010];
long long bi[18];
int main()
{
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    bi[0] = 1;
    for(int i = 1;i <= 18;i ++) {
        bi[i] = bi[i - 1] * 10;
        // cout << bi[i] << endl;
    }
    cin >> casenum;
    for(int cs = 1; cs <= casenum; cs ++) {
        long long n; cin >> n;
        long long ans = 0;
        len = 0;
        while(n) {
            d[len] = n % 10;
            len ++;
            n /= 10;
        }
        for(int i = len - 1;i >= 0;i --) {
            int a = d[i];
            bool ok = true;
            for(int j = i - 1;j >= 0;j --) {
                if(d[j] < a) {
                    ok = false;
                    break;
                }
            }
            if(ok) {
                ans += a * bi[i];
            } else {
                if(d[i - 1] > a) {
                    ans += a * bi[i];
                    ans += (d[i - 1] - 1) * bi[i - 1];
                    for(int j = i - 2;j >= 0;j --) {
                        ans += 9 * bi[j];
                    }
                } else {
                    ans += (a - 1) * bi[i];
                    for(int j = i - 1;j >= 0;j --) {
                        ans += 9 * bi[j];
                    }
                }
                break;
            }
        }
        cout << "Case #" << cs << ": ";
        cout << ans << endl;
    }
    return 0;
}
