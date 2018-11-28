#include <bits/stdc++.h>

using namespace std;

int t;
string s;

string xuli(string s){
    string x = "";
    int k= s.length(), ok = 1;
    if(s.length() == 1) return s;
    for(int i = 0; i< s.length() - 1; i++)
        if(s[i] > s[i + 1]){
            ok = 0;
            k = i;
            break;
        }
    if(ok == 1) return s;
    for(int i = k; i >= 0; i--)
        if(s[k] == s[i]) k = i;
        else break;
    if(s[k] == '1')
        for(int i = 0; i< s.length() - 1; i++) x+= '9';
    else
        for(int i = 0; i< s.length(); i++)
            if(i < k) x+= s[i];
            else if(i == k) x+= s[i] - 1;
            else x+= '9';
    return x;
}

int main(){
    //ifstream fi("input_file.txt");
    //ofstream fo("output_file.txt");

    cin >> t;
    for(int i = 0; i< t; i++){
        cin >> s;
        cout << "Case #"<< i+1 << ": "<< xuli(s) << endl;
    }

    //fi.close();
    //fo.close();
    return 0;
}
