#include <iostream>
using namespace std;

string result(string n, int k){
    int i = 0;
    int flip =  0;
    long len = n.size();
    while (i < len){
        while (n[i] == '+') i++;
        if (i+k-1 < len){
            flip++;
            for (auto j = i; j < i + k; j++){
                n[j] = n[j] == '+' ? '-':'+';
            }
        } else{
            for (auto m = i; m < len; m++){
                if (n[m] == '-')
                    return "IMPOSSIBLE";
            }
        }
    }
    return to_string(flip);
}

int main(){
    int t, k;
    string n;
    cin >> t;
    for (int i=1; i<=t; ++i){
        cin >> n >> k;
        cout << "Case #" << i << ": " << result(n, k) << endl;
    }
    return 0;
}