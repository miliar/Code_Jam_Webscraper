#include<iostream>
#include<string>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int itrS = 1; itrS <= t; itrS++){
        string str;
        cin >> str;
        int k;
        cin >> k;
        int cnt = 0;
        for(int i = 0; i <= str.length() - k; i++){
            if(str[i] == '-'){
                cnt++;
                for(int j = 0; j < k; j++)
                    if(str[i + j] == '-')
                        str[i + j] = '+';
                    else
                        str[i + j] = '-';
            }
        }
        bool flag = true;
        for(int i = 0; i <= str.length() && flag; i++)
            if(str[i] == '-')
                flag = false;
        cout << "Case #" << itrS << ": ";
        if(flag)
            cout << cnt << "\n";
        else
            cout << "IMPOSSIBLE\n";
    }
    return 0;
}
