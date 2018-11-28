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
//ifstream fin("B-large.in"); /// modifica cu numele corespunzator
//ofstream fout("B-large.out"); /// modifica cu numele corespunzator

int t;
string s, sol;
bool aux1, aux2, aux3;

int main()
{
    cin >> t;
    for1(nr_t, t)
    {
        cin >> s;
        cout << "Case #" << nr_t << ": ";

        if(s.size() == 1)
        {
            cout << s[0];
            goto SKIP;
        }
        aux1 = aux2 = aux3 = 0;
        for(auto i: s)
            if(i == '0')
                aux1 = 1;
            else if(i == '1')
                aux2 = 1;
            else aux3 = 1;
        if(aux1 && aux2 && !aux3)
        {
            for1(temp, s.size() - 1)
                    cout << '9';
            goto SKIP;
        }
        sol.clear();
        for0(i, s.size() - 1)
            if(s[i] <= s[i + 1])
                sol += s[i];
            else
            {
                s[i]--;
                sol += s[i];
                for(int j = i + 1; j < s.size(); j++)
                    sol += "9";
                for(int temp = sol.size() - 1; temp > 0; temp--)
                    if(sol[temp] < sol[temp - 1])
                        sol[temp - 1]--, sol[temp] = '9';
                if(sol[0] == '0')
                {
                    for1(i, sol.size() - 1)
                        cout << sol[i];
                    goto SKIP;
                }

                cout << sol;
                goto SKIP;
            }
        cout << sol << s[s.size() - 1];
        SKIP: ;
        cout << '\n';

    }


    return 0;
}




