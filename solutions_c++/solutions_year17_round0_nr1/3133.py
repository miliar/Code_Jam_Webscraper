#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int t;

void solve(int test){
    printf("Case #%d: ", test);
    string s; int k;
    cin >> s >> k;
    int ans = 0;
    for (int i = 0; i < s.size() - k + 1; i++){
        if (s[i] == '-'){
            ans++;
            for (int j = 0; j < k; j++)
                s[i + j] = (s[i + j] == '-' ? '+' : '-');
        }
    }
    bool bad = false;
    for (int i = 0; i < s.size(); i++)
        if (s[i] == '-')
            bad = true;
    if (bad)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << ans << endl;
}
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("ALarge.txt", "w", stdout);
    cin >> t;
    for (int i = 0; i < t; i++)
        solve(i + 1);
    return 0;
}
