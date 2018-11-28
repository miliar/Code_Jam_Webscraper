#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<string>
using namespace std;
string str;
int num[100000];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T, k;
    cin >> T;

    for(int f = 1; f <= T; f++){
        cin >> str >> k;
        int ans = 2147483647;
        int now, cnt,flag;

        int L = str.length();

        for(int i = 0; i < L; i++){
            num[i] = 0;
        }
        now = cnt = 0;
        for(int i = 0; i + k - 1 < L; i++){
            now += num[i];
            if((now % 2 == 0 && str[i] == '-') || (now % 2 == 1 && str[i] == '+')){
                ++cnt;
                ++now;
                --num[i + k];
            }
        }
        flag = 1;
        for(int i = L - k + 1; i < L && flag == 1; i++){
            now += num[i];
            if((now % 2 == 0 && str[i] == '-') || (now % 2 == 1 && str[i] == '+')){
                flag = 0;
            }
        }
        if(flag == 1){
            ans = min(ans, cnt);
        }

        reverse(str.begin(), str.end());

        for(int i = 0; i < L; i++){
            num[i] = 0;
        }
        now = cnt = 0;
        for(int i = 0; i + k - 1 < L; i++){
            now += num[i];
            if((now % 2 == 0 && str[i] == '-') || (now % 2 == 1 && str[i] == '+')){
                ++cnt;
                ++now;
                --num[i + k];
            }
        }
        flag = 1;
        for(int i = L - k + 1; i < L && flag == 1; i++){
            now += num[i];
            if((now % 2 == 0 && str[i] == '-') || (now % 2 == 1 && str[i] == '+')){
                flag = 0;
            }
        }
        if(flag == 1){
            ans = min(ans, cnt);
        }

        if(ans != 2147483647){
            cout << "Case #" << f << ": " << ans << endl;
        }else{
            cout << "Case #" << f << ": IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
