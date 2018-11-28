#include<iostream>
#include<string>
using namespace std;

int solve(string s, int k){
    int f=0;
    for(int i=0;i<s.size();i++){
        if(s[i] == '-'){
            f++;
            for(int j=0;j<k;j++){
                if(i+j >= s.size()){
                    return -1;
                } else {
                    if(s[i+j] == '-'){
                        s[i+j] = '+';
                    } else {
                        s[i+j] = '-';
                    }
                }
            }
        }
    }

    return f;
}

int main(){
    int n;
    cin >> n;
    for(int j=0;j<n;j++){
        string s;
        cin >> s;
        int k;
        cin >> k;

        int res = solve(s, k);
        if(res == -1){
            cout << "Case #" << j+1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << j+1 << ": " << res << endl;
        }
    }
}

