#include <bits/stdc++.h>
using namespace std;
int t,n,xam;
string s;
int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        cin >> s;
        printf("Case #%d: ", i);
        xam = s[s.size()-1];
        for (int i = s.size()-2; i >= 0; i--){
            if (s[i] > xam){
                s[i]--;
                for (int j = i+1; j < s.size(); j++) s[j] = '9';
            }
            xam = s[i];
        }
        int awal = 0;
        for (awal; awal < s.size()-1; awal++){
            if (s[awal] != '0') break;
        }
        for (int i = awal; i < s.size(); i++){
            cout << s[i];
        }
        cout<<endl;
    }
}
