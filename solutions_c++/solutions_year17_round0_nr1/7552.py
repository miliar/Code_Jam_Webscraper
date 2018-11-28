//Qualification Round 2017
//Problem A. Oversized Pancake Flipper
#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.txt", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
typedef long long LL;
typedef pair<int,int> pii;
const int MOD = 1e9 + 7;
const int MAX = 1e5 + 5;

bool check(string s){
    REP(i, s.size()) if(s[i] == '-') return 0;
    return 1;
}

int main() {
    fr;fw;
    int T, cases = 1;
    cin >> T;
    while(T--){
        string s;
        int k, n;
        cin >> s >> k;
        n = s.size();
        int ret = 0;
        for(int i=0;i<=n-k;i++){
            if(s[i] == '+') continue;
            ret++;
            for(int j=i;j<i+k;j++){
                if(s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }
        cout << "Case #" << cases++ <<": ";
        if(check(s)) cout << ret <<"\n";
        else cout <<"IMPOSSIBLE\n";
    }
    return 0;
}