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

bool f[N];

int main()
{
    //ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("i", "r", stdin);
    freopen("o", "w", stdout);
    int qu; cin >> qu;
    for(int ass = 1 ; ass <= qu ; ass ++)
    {
    int n, vx; cin >> n >> vx;
    f[0] = true;
    f[n+1] = true;
    int l, r, prev, next, idx;
    for(int p = 1 ; p <= vx ; p ++)
    {
        l = 0, r = 0, prev = 0, next = n+1;
        for(int i = 1 ; i <= n ; i ++)
            if(!f[i])
            {
                idx = i;
                break;
            }
        for(int i = 1 ; i <= n ; i ++)
        {
            if(f[i])
            {
                prev = i;
                continue;
            }
            for(int j = i ; j < n+2 ; j ++)
                if(f[j])
                {
                    next = j;
                    break;
                }
            int cur_l = i-prev-1;
            int cur_r = next-i-1;
            if((min(l, r) == min(cur_l, cur_r) && max(l, r) < max(cur_l, cur_r)) || (min(l, r) < min(cur_l, cur_r)))
            {
                idx = i;
                l = cur_l;
                r = cur_r;
            }
        }
        f[idx] = true;
        //cout << p << " humans and max/min: " << max(l, r) << " " << min(l, r) << "\n";
        //for(int i = 0 ; i < n+2 ; i ++)
            //cout << f[i];
        //cout << endl;
    }
    for(int i = 0 ; i <= n+2 ; i ++)
        f[i] = false;
    cout << "Case #" << ass << ": " << max(l, r) << " " << min(l, r) << "\n";
    }
}
