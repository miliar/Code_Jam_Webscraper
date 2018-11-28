#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, c = 0; cin >> t;
    while(t--){
        cout << "Case #" << ++c << ": ";
        string s; int n;
        cin >> s >> n;
        vector < char > sol(s.size());
        for(int i = 0; i < sol.size(); i++)
            sol[i] = s[i];

        int cnt = 0;
        for(int i = 0; i < s.size(); i++){

            if(sol[i] == '-' && i+n <= s.size()){
                cnt++;
//                cout << i << "\n";
                for(int j = i; j < i+n; j++){
                    char tmp = (sol[j] == '+') ? '-' : '+';
                    sol[j] = tmp;
                }
            }

        }
        bool ok = 1;
        for(int i = 0; i < sol.size(); i++){
            if(sol[i] == '-'){
                ok = 0;
                break;
            }
        }
        if(!ok)
            cout << "IMPOSSIBLE\n";
        else
            cout << cnt << "\n";
    }



    return 0;
}
