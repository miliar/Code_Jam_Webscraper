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

void transform(const string& s, vector<int>& v)
{
    for(int i = 0 ; i < s.size() ; i ++)
        v[i] = s[i]-'0';
}

int main()
{
    freopen("i", "r", stdin);
    freopen("o", "w", stdout);
    //ios_base::sync_with_stdio(false); cin.tie(0);
    int q; cin >> q;
    for(int num = 1 ; num <= q ; num ++)
    {
        string s; cin >> s;
        int n = s.size();
        vector<int> ar(n); transform(s, ar);
        int idx = n;
        for(int i = n-1 ; i > 0 ; i --)
        {
            if(ar[i] < ar[i-1])
            {
                idx = i;
                ar[i-1]--;
            }
        }
        cout << "Case #" << num << ": ";
        if(ar.size() == 1 || ar[0] > 0)
            for(int i = 0 ; i < n ; i ++)
                if(i >= idx)
                    cout << 9;
                else
                    cout << ar[i];
        else
            for(int i = 1 ; i < n ; i ++)
                if(i >= idx)
                    cout << 9;
                else
                    cout << ar[i];
        cout << "\n";
    }
}
