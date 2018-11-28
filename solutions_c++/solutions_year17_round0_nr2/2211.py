#include<iostream>
#include<string>

using namespace std;
#define LL long long

int main(){

    int t;
    cin >> t;
    string s;

    for(int i = 0; i < t; i++){
        cin >> s;
        int k = 1;
        while(k < s.length() && s[k - 1] <= s[k])
            k++;
        if(k < s.length()){
            k--;
            while(k > 0 && s[k - 1] == s[k])
                k--;
            s[k]--;
            for(int j = k + 1 ; j < s.length(); j++)
                s[j] = '9';
        }
        long long x = 0;
        for(int i = 0; i < s.length(); i++){
            x = x * 10ll + (LL)(s[i] - '0');
        }
        cout << "Case #" << i + 1 << ": " << x << endl;
    }
    return 0;
}
