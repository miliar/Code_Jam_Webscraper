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
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("out-small.txt", "w", stdout);
    int T;
    cin >> T;
    for(int kase = 1; kase <= T; kase++){
        string s;
        cin >> s;
        int flag = 0;
        for(int i = 0; i < s.length() - 1; i++){
            if(s[i] > s[i + 1]){
                if(i == 0 || s[i] != s[i - 1]){
                    s[i]--;
                    for(int m = i + 1; m < s.length(); m++)s[m] = '9';
                }
                else{
                    char c = s[i];
                    for(int j = 0; i - j >= 0; j++){
                        if(s[i - j] != c || i - j == 0){
                            s[i - j]--;
                            for(int m = i - j + 1; m < s.length(); m++){
                                s[m] = '9';
                            }
                            flag = 1;
                            break;
                        }
                    }
                    if(flag)break;
                }
            }
        }
        if(s[0] == '0')s = s.substr(1, s.length());
        printf("Case #%d: ", kase);
        cout << s << endl;
    }
    return 0;
}
