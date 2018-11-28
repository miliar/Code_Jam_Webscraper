#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int maxn = 1e5 + 100, inf = 1e9 + 100, mod = 1e9 + 7;

int test;

int main(){
    #ifdef ONPC
    ifstream cin("a.in");
    ofstream cout("a.out");
    #else
    //ifstream cin("a.in");
    //ofstream cout("a.out");
    #endif // ONPC
    ios::sync_with_stdio(0);
    cin >> test;
    for (int iter = 1; iter <= test; iter++){
        string s;
        cin >> s;
        bool ez = 1;
        if (s[0] != '1')
            ez = 0;
        if (ez){
        ez = 0;
        for (int i = 1; i < s.length(); i++)
        if (s[i] == '0')
            ez = 1;
        }
        cout << "Case #" << iter << ": ";
        if (ez){
            for (int i = 1; i < s.length(); i++)
                cout << '9';
        }
        else{
            for (int i = 0; i < s.length(); i++){
                char x = s[i];
                int f = 0;
                for (int j = i + 1; j < s.length(); j++)
                    if (s[j] < x){
                        f = -1;
                        break;
                    }
                    else
                    if (s[j] > x){
                        f = 1;
                        break;
                    }
                if (f == -1){
                    cout << (char)(x - 1);
                    for (int j = i + 1; j < s.length(); j++)
                        cout << '9';
                    break;
                }
                cout << x;
            }
        }
        cout << '\n';
    }
}
