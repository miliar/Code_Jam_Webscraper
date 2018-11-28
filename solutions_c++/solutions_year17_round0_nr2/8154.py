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

int Check(string s, int len)
{
    int res = 0;
    for (int i = len - 1; i > 0; i--) {
        if (s[i-1] > s[i]) {
            return i;
        }
    }
    return 0;
}

string Solve(string s, int len, int start)
{
    int k = s[start - 1] - '0';
    k--;
    s[start - 1] = k + '0';
    for (int i = start; i < len; i++)
        s[i] = '9';
    return s;
}

string leadingZero(string s, int len)
{
    string res = "";
    if (s[0] == '0') {
        for (int i = 1; i < len; i++)
            res += s[i];
        return res;
    }
    else return s;
}

int main()
{
//    READ();
//    WRITE();

    int T; sf(T);
    for (int cas = 1; cas <= T; cas++) {
        string s; cin >> s;
        int len = s.size();
        if (len == 1) {
            cout << "Case #" << cas << ": " << s << endl;
            continue;
        }
        while (1) {
            int k = Check(s, len);
            if (k == 0) break;

            s = Solve(s, len, k);
        }
        s = leadingZero(s, len);
        cout << "Case #" << cas << ": " << s << endl;
    }
    return 0;
}
