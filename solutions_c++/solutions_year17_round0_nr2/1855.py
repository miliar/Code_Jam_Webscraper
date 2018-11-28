#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solve(string& seq){
    int n = seq.size();
    char last = '9';
    int cur = n;
    for(int i = n-1; i >= 0; --i){
        if(last < seq[i]){
            cur = i+1;
            last = seq[i] - 1;
        }else{
            last = seq[i];
        }
        seq[i] = last;
    }
    for(;cur < n; ++cur){
        seq[cur] = '9';
    }
    if(seq[0] == '0'){
        seq = seq.substr(1);
    }
    return seq;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        string seq;
        cin >> seq;
        cout << "Case #" << t << ": " << solve(seq) << endl;
    }
    return 0;
}

