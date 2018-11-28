/***************************************************\
*                  بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ                    *
*                    رَّبِّ زِدْنِى عِلْمًا                       *
*               Mir Abdullah yousuf                 *
*    Khulna University of Engineering & Technology  *
*     Electrical and Electronic Engineering, 2k14   *
\***************************************************/
#include <bits/stdc++.h>
#define LL              long long
#define PI              acos(-1.0)
#define PII             pair<int,int>
#define PLL             pair<LL, LL>
#define xx              first
#define yy              second
#define MS(a,b)         memset(a, b, sizeof (a))
#define MP(a,b)         make_pair(a, b)
#define pb              push_back
#define sf(a)           scanf("%d", &a)
#define sff(a, b)       scanf("%d %d", &a, &b)
#define sfff(a, b, c)   scanf("%d %d %d", &a, &b, &c)
#define sfl(a)          scanf("%lld", &a)
#define sfll(a, b)      scanf("%lld %lld", &a, &b)
#define sflll(a, b, c)  scanf("%lld %lld %lld", &a, &b, &c)
#define READ()          freopen("input.txt", "r", stdin)
#define WRITE()         freopen("output.txt", "w", stdout)
#define GCD(a, b)       __gcd(a, b)
#define LCM(a, b)       (a * b) / GCD(a, b)
#define sqr(a)          (a) * (a)
#define MOD             10000007
#define MAX             100
using namespace std;

///***********-8-direction*************/
//int fx[] = {1, -1, 0, 0, 1, -1, -1, 1};
//int fy[] = {0, 0, 1, -1, 1, 1, -1, -1};

///***********-4-direction*************/
//int fx[] = {1, -1, 0, 0};
//int fy[] = {0, 0, 1, -1};

///link : https://www.codechef.com/APRIL17/problems/SEABIL

int Check(string s, int len)
{
    for (int i = 0; i < len; i++) {
        if (s[i] == '-') return i;
    }
    return -1;
}

int main()
{
//    READ();
//    WRITE();

    int T; sf(T);
    for (int cas = 1; cas <= T; cas++) {
        string s; int k, cnt = 0, len;
        cin >> s >> k;
        len = s.size();
        while (1) {
            int x = Check(s, len);
            if (x == -1) {
                printf("Case #%d: %d\n", cas, cnt);
                break;
            }
            else {
                if (x+k > len) {
                    printf("Case #%d: IMPOSSIBLE\n", cas);
                    break;
                }
                else {
                    for (int i = x; i < x+k; i++) {
                        if (s[i] == '+') s[i] = '-';
                        else s[i] = '+';
                    }
                }
            }
//            cout << s << endl;
            cnt++;
        }
    }
    return 0;
}
