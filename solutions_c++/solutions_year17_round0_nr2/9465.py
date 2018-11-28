#include <bits/stdc++.h>
using namespace std;
#define LL long long

string ss;
int len;

int main()
{
//    freopen("in.in", "r", stdin);
//    freopen("out.txt", "w", stdout);

    LL t, tc;
    scanf("%lld", &tc);
    for (t = 1; t <= tc; t++)
    {
        cin >> ss;
        len = ss.size();

        beg:

        int p = -1;
        for (int i = 0; i < (len - 1); i++) {
            if (ss[i] > ss[i+1]) {
                p = i;
                break;
            }
        }

        if (p != -1) {
            for (int i = p+1; i < len; i++) ss[i] = '9';
            ss[p]--;

            if (p > 0) {
                if (ss[p] < ss[p-1]) goto beg;
            }
        }

        while(ss[0] == '0') ss.erase(ss.begin());

        printf("Case #%lld: ", t);
        cout << ss << endl;
    }
    return 0;
}
