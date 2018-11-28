
#include <bits/stdc++.h>
#define for0(i, n) for(int i = 0; i < n; i++)
#define for1(i, n) for(int i = 1; i <= n; i++)
#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()
#define V vector<int>
#define VP vector<pair<int, int> >
#define clr(A, x) memset(A, x, sizeof(A))
#define cpy(A, B) memcpy(A, B, sizeof(B))
#define g(s) getline(cin, s) ///ai grija la fin/cin ///
#define FASTIO ios_base::sync_with_stdio(0)
const long long INFLL = (1LL<<62);
const int INFINT = 2000000000;
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
/*template <typename T>
string to_string(const T& n){
    ostringstream os;
    os << n;
    return os.str();
}
*/
/*void invers_modular(int a, int b, int &d, int &x, int &y)
{
    if(!b)
    {
        d=a;
        x=1;
        y=0;
        return ;
    }
    int x0, y0;
    invers_modular(b, a%b, d, x0, y0);
    x=y0;
    y=x0-a/b*y0;
}*/ // daca x<0 se aduna cu mod pana e mai mare, x fiind rezultatul

/*ull putere(ull baza, ull exponent, ull MOD)
{
    if(exponent == 0) return 1;
    if(exponent % 2 == 0) return putere((baza * baza) % MOD, exponent / 2, MOD) % MOD;
    return ((baza % MOD) * (putere(baza, exponent - 1, MOD) % MOD) % MOD);
}*/
//ifstream fin("C-large.in"); /// modifica cu numele corespunzator
//ofstream fout("C-large.out"); /// modifica cu numele corespunzator

struct number
{
    ll cnt, val;
    number()
    {
        cnt = val = 0;
    }
};

number big, small, c;
number temp[4];
ll mmax = 0;
ll t, n, k;

int main()
{
    cin >> t;
    for1(nr_t, t)
    {
        cin >> n >> k;
        big = small = c;
        for0(i, 4)
            temp[i] = c;
        mmax = 0;
        big.val = n;
        big.cnt = 1;

        cout << "Case #" << nr_t << ": ";
        for(;;)
        {
            mmax = 0;
            k -= big.cnt;
            if(k <= 0)
            {
                if(big.val % 2 == 0)
                    cout << big.val / 2 << ' ' << max(0LL, big.val / 2  - 1) << '\n';
                else cout << big.val / 2 << ' ' << big.val / 2 << '\n';
                break;
            }

            k -= small.cnt;
            if(k <= 0)
            {
                if(small.val % 2 == 0)
                    cout << small.val / 2 << ' ' << max(0LL, small.val / 2  - 1) << '\n';
                else cout << small.val / 2 << ' ' << small.val / 2 << '\n';
                break;
            }
           // cout << big.val << ' ' << big.cnt << ' ' << small.val << ' ' << small.cnt << endl;

            if(big.val % 2 == 0)
            {
                temp[0].val = big.val / 2;
                temp[1].val = max(0LL, big.val / 2 - 1);
                temp[0].cnt = temp[1].cnt = big.cnt;
            }
            else
            {
                temp[0].val = temp[1].val = big.val / 2;
                temp[0].cnt = temp[1].cnt = big.cnt;
            }

            if(small.val % 2 == 0)
            {
                temp[2].val = small.val / 2;
                temp[3].val = max(0LL, small.val / 2 - 1);
                temp[2].cnt = temp[3].cnt = small.cnt;
            }
            else
            {
                temp[2].val = temp[3].val = small.val / 2;
                temp[2].cnt = temp[3].cnt = small.cnt;
            }
            big.cnt = small.cnt = 0;
            for0(i, 4)
                mmax = max(mmax, temp[i].val);
            for0(i, 4)
                if(temp[i].val == mmax)
                {
                    big.cnt += temp[i].cnt;
                    big.val = mmax;

                    temp[i] = c;
                }
                else if(temp[i].val != 0)
                {
                    small.cnt += temp[i].cnt;
                    small.val = temp[i].val;

                    temp[i] = c;
                }
        }
    }



    return 0;
}
