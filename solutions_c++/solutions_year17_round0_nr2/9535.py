#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>

using namespace std;

#define MAXN 20
int digit[MAXN];

int SpiltNum(int n){
    int len = 0;
    while(n){
        digit[len++] = n % 10;
        n /= 10;
    }
    return len;
}

int DP(int n){
    for(int i=n; i>=1; i--){
        int len = SpiltNum(i);
        bool flag = true;
        for(int i=1; i<len; i++){
            if(digit[i-1] < digit[i]){
                flag = false;
                break;
            }
        }
        if(flag){
            return i;
        }
    }
    return -1;
}

int main()
{
//    cout << "Hello world!" << endl;
    freopen("B1.txt", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t;
    int cas = 0;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        cout << "Case #" << ++cas << ": " << DP(n) << endl;
    }
    return 0;
}
