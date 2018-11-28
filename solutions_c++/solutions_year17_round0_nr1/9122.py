#include <iostream>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <sstream>
#include <queue>
#include <map>
#include <functional>
#include <bitset>

using namespace std;
#define pb push_back
#define mk make_pair
#define ll long long
#define ull unsigned long long
#define pii pair<int, int>
#define fi first
#define se second
#define ALL(A) A.begin(), A.end()
#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define REP1(i, n) for(int (i)=1;(i)<=(int)(n);(i)++)
#define fastio ios::sync_with_stdio(0), cin.tie(0)
#define PI M_PI
const ll mod = 1000000007;
const int INF = 213456789;
const double eps = 1e-7;

template<class T> T gcd(T a, T b){if(!b)return a;return gcd(b,a%b);}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out-large.txt", "w", stdout);
    int T;
    cin >> T;
    for(int kase = 1; kase <= T; kase++){
        string s;
        cin >> s;
        int n;
        cin >> n;
        int i = 0;
        int ans = 0;
        while(i < s.length()){
            if(s[i] == '+'){
                i++;
                continue;
            }
            else if(s[i] == '-'){
                if(i + n <= s.length()){
                    for(int j = 0; j < n; j++){
                        if(s[i + j] == '+')s[i + j] = '-';
                        else s[i + j] = '+';
                    }
                    ans++;
                    i++;
                }
                else i++;
            }
        }
        for(i = 0; i < s.length(); i++){
            if(s[i] == '-')break;
        }
        if(i == s.length())printf("Case #%d: %d\n", kase, ans);
        else printf("Case #%d: IMPOSSIBLE\n", kase);
    }
    return 0;
}
