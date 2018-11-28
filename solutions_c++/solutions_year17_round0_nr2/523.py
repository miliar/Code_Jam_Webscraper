#include<bits/stdc++.h>

using namespace std;

string s;

int32_t main(){
    ios_base::sync_with_stdio(0);
    ifstream fin("inputB.txt");
    ofstream fout("outputB.txt");
    #define cin fin
    #define cout fout
    int t;
    cin >> t;
    for(int j = 0; j < t; ++j){
        cout << "Case #" << j+1 << ": ";
        cin >> s;
        int x = -1;
        for(int i = 1; i < s.size(); ++i){
            if(s[i] < s[i-1]){
                x = i-1;
                break;
            }
        }
        if(x == -1){
            cout << s << endl;
        }
        else{
            for(int i = x; i >= 0; --i){
                if(i == 0 && s[i] == '1'){
                    int n = s.size();
                    s = "";
                    for(int z = 0; z < n-1; ++z){
                        s += '9';
                    }
                }
                else if(i == 0 || s[i] - 1 >= s[i-1]){
                    s[i] -= 1;
                    for(int z = i+1; z < s.size(); ++z){
                        s[z] = '9';
                    }
                    break;
                }
            }
            cout << s << endl;
        }
    }
}
