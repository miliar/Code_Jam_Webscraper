#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define MOD 1000000007
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
int main()
{
        freopen("A-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                string s;
                int k, ans = 0;
                cin >> s >> k;
                for(int i = 0; i <= (int) s.size() - k; i++){
                        if(s[i] == '-') {
                                for(int j = i; j < i + k; j++) {
                                        if(s[j] == '-')s[j] = '+';
                                        else    s[j] = '-';
                                }
                                ans++;
                        }
                }
                bool done = 1;
                for(int i = 0; i < (int) s.size(); i++) {
                        done &= (s[i] != '-');
                }
                cout << "Case #" << c << ": ";
                if(!done)
                        cout << "IMPOSSIBLE\n";
                else    cout << ans << "\n";
        }
        return 0;
}
