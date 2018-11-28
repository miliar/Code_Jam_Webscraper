#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long int ulli;

string exclude_leading_zeroes(string in){
    string ans;
    ulli i = 0;
    for(i = 0; i < in.size() && in[i] == '0'; i++);

    for(; i < in.size(); i++)   ans = ans + in[i];

    if(ans == "")   ans = "0";
    return ans;
}

bool is_tidy(string in){
    bool ans = true;

    for(ulli i = 1; i < in.size(); i++){
        if(in[i] < in[i-1])
            ans = false;
    }

    return ans;
}

int main(){
    ios :: sync_with_stdio(false);
    cin.tie(NULL);
    string a,b;
    ulli t,ans;
    char c;

    cin >> t;

    for(ulli i = 0; i < t; i++){
        cin >> a;
        while(is_tidy(a) == false){
            ulli j;

            for(j = 1; j < a.size(); j++){
                if(a[j-1] > a[j]){
                    a[j-1]--;
                    break;
                }
            }

            for(; j < a.size(); j++){
                a[j] = '9';
            }

            a = exclude_leading_zeroes(a);
        }

        cout << "Case #" << i + 1 << ": " << a << endl;
    }
}
