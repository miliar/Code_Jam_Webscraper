#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define MOD 1000000007
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
ll ans = -1;
string n;
void calc(int i, ll cur, bool les) {
        if(i == n.size()) {
                ans = max(ans, cur);
                return;
        }
        int x = cur % 10LL, y = n[i] - '0';
        if(!les) {
                if(y >= x)
                        calc(i + 1, cur * 10LL + y, les);
                if(y - 1 >= 0 && y - 1 >= x)
                        calc(i + 1, cur * 10LL + y - 1, 1);
        }
        else    {
                calc(i + 1, cur * 10LL + 9, 1);
        }
}
int main()
{
        freopen("B-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                cin >> n;
                cout << "Case #" << c << ": ";
                calc(0, 0, 0);
                if(ans == -1) {
                        for(int i = 0; i < (int) n.size() - 1; i++)
                                cout << 9;
                }else   cout << ans;
                cout << "\n";
                ans = -1;
        }
        return 0;
}
