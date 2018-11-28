#include <bits/stdc++.h>
#define FILE_IN freopen("in", "r", stdin);
#define FILE_OUT freopen("out", "w", stdout);
#define endl "\n"
#define mk make_pair
#define pb push_back
#define fi first
#define se second
#define ii pair<int,int>
#define ll long long
#define For(i,x,y) for(int i=x; i<y; i++)
#define popcount(x) __builtin_popcount(x)
#define popcountll(x) __builtin_popcountll(x)
#define MOD 1000000007
#define PI acos(-1.0)
using namespace std;
const double eps = 1e-9;
#define N 100100



int main () {

    int T;

    int k;
    cin >> T;
    
    int test = 1;
    while(T--) {

        string s;

        cin >> s;
        cin >> k;

        int cnt = 0;

       // printf("sz %d\n", (int)s.size());
        for(int i=0;i<=s.size()-k;i++) {
           // printf("%d: ", i);
            if(s[i] == '-') {
                cnt++;
                for(int j=0;j<k;j++) {
                    if(s[i+j] == '-') {
                        s[i+j] = '+';
                    } else s[i+j] = '-';
                }
            }

     //       cout << s << endl;
        }

        printf("Case #%d: ", test++);
        bool res = 1;
        for(int i=0;i<s.size();i++) {
            if(s[i] == '-') {
                printf("IMPOSSIBLE\n");
                res = 0;
                break;
            }   
        }

        if(res) {
            printf("%d\n", cnt);
        }

    }   

}



