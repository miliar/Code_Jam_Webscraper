//never sleep.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T>
T input()
{
    T ans = 0, m = 1;
    char c = ' ';
    while (!((c >= '0' && c <= '9') || c == '-'))
        c = getchar();
    if (c == '-')
        m = -1, c = getchar();
    while (c >= '0' && c <= '9')
    {
        ans = ans * 10 + (c - '0'), c = getchar();
    }
    return ans * m;
}
template<typename T>
void read(T& a)
{
    a = input<T>();
}
template<typename T, typename... R>
void read(T& a, R&... r)
{
    read(a);
    read(r...);
}
void ex(string msg = "NO")
{
    cout << msg << "\n";
    exit(0);
}
const int N = 1e5 + 7;

char sw(char a)
{
    if(a == '-')
        return '+';
    return '-';
}

int main()
{
    //ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("i", "r", stdin);
    freopen("o", "w", stdout);
    int a; cin >> a;
    for(int num = 1 ; num <= a ; num ++)
    {
        string s; int k;
        cin >> s >> k;
        int ans = 0, n = s.size();
        for(int i = 0 ; i <= n-k ; i ++)
            if(s[i] == '-')
            {
                for(int j = i ; j < i+k ; j ++)
                    s[j] = sw(s[j]);
                ans++;
            }
        bool ok = true;
        for(int i = n-1 ; i > n-k ; i --)
            if(s[i] == '-')
                ok = false;
        if(!ok)
            cout << "Case #" << num << ": IMPOSSIBLE\n";
        else
            cout << "Case #" << num << ": " << ans << "\n";
    }
}
