#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt" , "r" ,stdin);
    freopen("out.txt" , "w" ,stdout);
    int t;
    cin >> t;
    string str;
    int k;
    for(int i=1;i<=t;i++){
        cin >> str >> k;
        bool flag = true;
        int ans = 0;
        for(int j=0;j<str.length();j++){
            if(str[j] == '-'){
                if(j+k-1 < str.length()){
                    for(int jj = j;jj<j+k;jj++){
                        str[jj] = (str[jj] == '+' ? '-' : '+');
                    }
                    ans++;
                }
                else{
                    flag = false;
                    break;
                }
            }
        }
        cout << "Case #" << i << ": ";
        if(!flag){
            cout << "IMPOSSIBLE";
            if(i!=t)cout<< "\n";
            continue;
        }
        cout << ans ;
        if(i!=t)cout << "\n";
    }
    return 0;
}
