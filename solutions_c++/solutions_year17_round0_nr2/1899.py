#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("B-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    int w, v;
    string s, g;
    cin >> t;
    for (int i = 1; i <= t; ++i){
        s.clear(); g.clear();
        /*
        cin >> w;
        v = w;
        while (w){
            s = (char)(w%10 + '0') + s;
            w/=10;
        }
        */
        cin >> s;
        cout << "Case #" << i << ": ";
        //cout << s << ' ';
        g = g + s[0];
        bool check = false;
        for (int j = 1; j < s.size(); ++j){
            if (check){
                g += '9';
                continue;
            }
            if (s[j] < g[j-1]){
                int k = j-1;
                while (k > 0 && (g[k]-1 < g[k-1])){
                    g[k] = '9';
                    k--;
                }
                if (k >= 0) g[k]--;
                check = true;
            }
            if (!check) g = g + s[j];
            else g = g + '9';
            //cout << g << '\n';
        }
        /*
        for (int j = v; j >= 1; --j){
            check = true;
            int f = 10, a = j;
            while (a){
                if (a%10 > f){
                    check = false;
                    break;
                }
                f = a%10;
                a/=10;
            }
            if (check){
                w = j;
                cout << j << ' ';
                break;
            }
        }
        */
        for (int j = 0; j < g.size(); ++j){
            if (g[j] == '0') continue;
            else cout << g[j];
        }
        cout << "\n";
    }
}
