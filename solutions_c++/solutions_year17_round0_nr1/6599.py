#include <bits/stdc++.h>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define INF (1<<30)
#define ll long long
#define ld long double
#define pii pair<int,int> 
#define endl '\n'

#define TASKNAME ""

using namespace std;

const int MAXN = 1e3;

int T, ans, k, n;
string s;

int main(){
    // freopen(TASKNAME".in", "r", stdin);
    // freopen(TASKNAME".out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("a.err", "w", stderr);
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> s >> k;
        n = s.length();
        ans = 0;
        bool imp = false;
        int reverses[MAXN + 10] = {0};

        for(int i = 0; i < n; i++){
            if((s[i] == '-' && reverses[i] % 2 == 0) || (s[i]=='+' && reverses[i] % 2 == 1)){
                if(n - i < k){
                    imp = true;
                    break;
                }
                for(int j = 0; j < k; j++){
                    reverses[i+j]++;
                }
                ans++;
            }
        }
        for(int i = 0; i < n; i++){
            cerr << reverses[i] << ' ';
        }
        cerr << endl;
        if(imp){
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
            continue;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}