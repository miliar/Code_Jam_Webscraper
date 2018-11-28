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

int t,T;

ll n,ans,a;

bool isTidy(ll a){
    string s = to_string(a);
    int n = s.length();
    for(int i = 0; i < n-1; i++){
        if(s[i] > s[i+1]){
            return false;
        }
    }
    return true;
}

int main(){
    // freopen(TASKNAME".in", "r", stdin);
    // freopen(TASKNAME".out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> n;
        ans = n;
        // cerr << n << endl;
        // cerr << isTidy(n) << endl;
        a = 1;
        while(!isTidy(ans)){
            a*=10;
            ans = ans - (ans%a) - 1;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}