#include <bits/stdc++.h>
#define loop(i, a, n) for(ll i = a; i < n; i++)
#define cin in
#define cout out
#define right(n) ((n) / 2)
#define left(n) ((n) / 2 - ((n) % 2 == 0))
using namespace std;

ifstream in("in.in");
ofstream out("out.txt");
typedef long long ll;

void prep()
{
    static ll t = 1;
    cout << "Case #" << t++ << ": ";
}

void func()
{
    ll n, k; cin >> n >> k;
    ll sub, a = 1, b = 0;
    k--;
    for (sub = 2; k > 0; k -= sub, sub *= 2, n /= 2) if (n % 2 == 1) a = 2 * a + b; else b = 2 * b + a;
    sub /= 2;
    k += sub;
    if (k > a) n--;
    cout << right(n) << " " << left(n) << endl;
}

int main()
{
    ll t; cin >> t;
    while(t--) prep(), func();
    return 0;
}
