#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
#define fori(n) for(int i = 0; i < n; i++)
#define forj(m) for(int j = 0; j < m; j++)
#define fork(m) for(int k = 0; k < m; k++)
#define for1(n) for(int i = 1; i < n; i++)

#define mp make_pair
#define pb push_back


int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    ifstream cin("a.in");
    ofstream cout("out.txt");
    ll t;
    cin >> t;
  /*  fork(t){
        string s;
        cin >> s;
        int i = 0;
        char last = '0';
        while (i < s.length()){
            if (s[i] < last){
                //if (s[i-1] == '0') s[i-1] = '9';
                s[i-1]--;
                for(int j = i; j < s.length(); ++j) s[j] = '9';
                i = 0;
                last = '0';
            }
            else {
                last = s[i];
                i++;
            }
        }
        cout << "Case #" << k+1 << ": ";
        if (s[0] == '0') {
            for (int j = 1; j < s.length(); ++j)
            cout << s[j];
        }
        else cout << s;
        cout << endl;
    }*/

    fork(t){
        int cnt = 0;
        string s; int a;
        cin >> s >> a;
        int i = 0;
        for(; i < s.length()- a + 1; ++i){
            if (s[i] == '-'){
                cnt++;
                for(int j = i; j < i + a; j++){
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        bool bo = 0;
        for (; i < s.length(); ++i){
            if (s[i] == '-') {
                cout << "Case #" << k+1 <<": IMPOSSIBLE" << endl;
                bo = 1;
                break;
            }
        }
        if (!bo) {
             cout << "Case #" << k+1 <<": " << cnt << endl;
        }
    }


}

