#include <bits/stdc++.h>
using namespace std;

int t, r;
string s;

string change(string t){
    for(int i = 0 ; i < t.size()-1 ; i++)
        if(t[i+1] < t[i]){
            t[i]--;
            for(int j = i+1 ; j < t.size() ; j++) t[j] = '9';
            break;
        }
    return t;
}
bool is(string t){
    for(int i = 0 ; i < t.size()-1 ; i++) if(s[i] > s[i+1]) return 0;
    return 1;
}
int main()
{
    freopen("B-large.in" , "r" , stdin);
    freopen("o.txt" , "w" , stdout);
    cin >> t;
    while(t-- && cin >> s){
        cout << "Case #" << ++r << ": ";
        while(!is(s)) s = change(s);
        int i = 0;
        while(s[i++]=='0');i--;
        for(;i < s.size() ; i++) cout << s[i];
        cout << endl;
    }
    fclose (stdout);
    return 0;
}
