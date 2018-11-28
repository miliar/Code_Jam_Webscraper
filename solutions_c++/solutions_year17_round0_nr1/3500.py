#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

string helper(string &s, int k){
    unordered_map<char, char> hashMap;
    hashMap['+'] = '-';
    hashMap['-'] = '+';

    int len = s.length(), res = 0;
    for(int i = len - 1; i >= k - 1; i --){
        if(s[i] == '+') continue;
        else{
            res ++;
            for(int j = 0; j < k; j ++){
                s[i - j] = hashMap[s[i-j]];
            }
        }
    }
    for(int i = 0; i < len; i ++){
        if(s[i] == '-') return "IMPOSSIBLE";
    }
    return to_string(res);
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int count = 1, n;
    cin >> n;
    while(n--){
        string s;
        int k;
        cin >> s >> k;
        string res = helper(s, k);
        cout << "Case #" << count << ": " << res << endl;
        count ++;
    }
    return 0;
}