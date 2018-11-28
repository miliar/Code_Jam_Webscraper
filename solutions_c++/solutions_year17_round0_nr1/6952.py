#include <bits/stdc++.h>

using namespace std;

int t, k;
string s;

int xuli(string s, int k){
    int d = 0;
    for(int i = 0; i <= s.length() - k; i++)
        if(s[i] == '-'){
            d++;
            for(int j = i; j < i+ k; j++){
                if (s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }
    for(int i = 0; i < s.length(); i++)
        if(s[i] == '-') return -1;
    return d;
}

int main(){
    //ifstream fi("input_file.txt");
    //ofstream fo("output_file.txt");

    cin >> t;
    for(int i = 0; i < t; i++){
        cin >> s >> k;
        int ok = xuli(s, k);
        if(ok == -1)
            cout << "Case #" << i+1 <<": "<<"IMPOSSIBLE"<< endl;
        else cout << "Case #" << i+1 <<": "<<ok << endl;
    }

    //fi.close();
    //fo.close();
    return 0;
}
