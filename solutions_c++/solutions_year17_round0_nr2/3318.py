#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef string sg;
typedef long long ll;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for(int i = 1;i <= T;i++){
       string s;
       cin >> s;
       string ans = s;
       int mark;
       for(int j = 0; j < s.length() - 1; j++){
            if(s[j] > s[j+1]){
                mark = j;
                ans[j]--;
                for(int k = j; k > 0 && ans[k-1] > ans[k]; k--){
                    ans[k-1]--;
                    ans[k] = '9';
                }
                while(mark < s.length() - 1){
                    ans[mark+1] = '9';
                    mark++;
                }
                j = s.length();
            }
       }
       printf("Case #%d: ",i);
       for(int j = 0;j < ans.length();j++){
            if(ans[j] > '0') cout << ans[j];
       }
       cout << endl;
    }
    return 0;
}
