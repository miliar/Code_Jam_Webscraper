#include<bits/stdc++.h>

using namespace std;

int32_t main(){
    ios_base::sync_with_stdio(0);
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    #define cin fin
    #define cout fout
    int t;
    cin >> t;
    for(int j = 0; j < t; ++j){
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ans = 0;
        vector<int> v(s.size()+1, 0);
        int x = 0;
        for(int i = 0; i < s.size(); ++i){
            x^=v[i];
            if((!x && s[i] == '-') || (x && s[i] == '+')){
                if(i + k < v.size()){
                    x^=1;
                    ++ans;
                    v[i+k] = 1;
                }
                else{
                    ans = -1;
                    break;
                }
            }
        }
        cout << "Case #" << j+1 << ": ";
        if(ans == -1){
            cout << "IMPOSSIBLE" << endl;
        }
        else{
            cout << ans <<endl;
        }
    }
}
