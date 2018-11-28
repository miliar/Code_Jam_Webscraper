#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>

using namespace std;

#define MAXSIZE 1005

char s[MAXSIZE];

void Solve(int k){
    int start = 0, last = 0;
    int len = strlen(s);
    bool flag = true;
    int cnt = 0;
    for(int i=0; i<len; i++){
        if(i < last && i >= start){
            if(s[i] == '+'){
                start = i;
                last = i + k;
                cnt++;
            }
        }
        else{
            if(s[i] == '-'){
                start = i;
                last = start + k;
                cnt++;
            }
        }
    }

    //check the last k-1 character
    if(last > len){
        flag = false;
    }

    if(flag){
        cout << cnt << endl;
    }
    else{
        cout << "IMPOSSIBLE" << endl;
    }
}

void BruteForce(int k){
    int cnt = 0;
    int len = strlen(s);
    for(int i=0; i<len-k+1; i++){
        if(s[i] == '-'){
            for(int j = i; j<i+k; j++){
                (s[j] == '+') ? (s[j] = '-') : (s[j] = '+');
            }
            cnt++;
        }
    }
    for(int i=len-k+1; i<len; i++){
        if(s[i] == '-'){
            cout << "IMPOSSIBLE " << endl;
            return;
        }

    }
    cout << cnt << endl;
}

int main()
{
    int k;
    freopen("A3.txt", "r", stdin);
    freopen("out3.txt", "w", stdout);
    int cas = 0;
    int t;
    cin >> t;
    while(t--){
        cin >> s >> k;
        cout << "Case #" << ++cas << ": ";
//        Solve(k);
        BruteForce(k);
    }
    return 0;
}
