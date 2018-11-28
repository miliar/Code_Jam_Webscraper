#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

int n[110];
char s[110];

int len;

bool isInc(int endpos){
    int inc = 1;
    for (int i = 1; i < endpos; ++i) {
        if (n[i + 1] < n[i]) {
            inc = 0;
        }
    }
    return inc;
}


void deal(int endpos){
    
    if (endpos <= 1 || isInc(endpos)) {
        return;
    }
    while (!isInc(endpos)) {
        n[endpos] = (n[endpos] + 10 - 1) % 10;
        if (n[endpos] == 9) {
            break;
        }
    }
    if (endpos) {
        n[endpos - 1] = (n[endpos - 1] + 10 - 1) % 10;
        while (n[endpos - 1] == 9) {
            endpos --;
            n[endpos - 1] = (n[endpos - 1] + 10 - 1) % 10;
        }
    }
    
    deal(endpos - 1);
}

int main(){
//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    
    for (int cas = 1; cas <= t; ++cas) {
        scanf("%s", s + 1);
        len = (int)strlen(s + 1);
        for (int i = 1; i <= len; ++i) {
            n[i] = s[i] - '0';
        }
        deal(len);
        int p = 1;
        while (n[p] == 0) {
            p++;
        }
        printf("Case #%d: ", cas);
        for (int i = p; i <= len; ++i) {
            printf("%d", n[i]);
        }
        cout << endl;
        
        
        
        
    }
    
}
