#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int N[20] = {0};
bool f(int len) {
    if(len == 1) return true;
    for(int i=1;i<len;i++) {
        if(N[i-1] > N[i]) break;
        else if(i == len-1) return true;
    }

    N[len-1]--;
    for(int i=len-1;i>=1;i--) {
        if(N[i] < 0) {
            N[i] = 9;
            N[i-1]--;
        }
    }
    return false;
}


int main() {
    int T;
    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        string str;
        cin >> str;
        int len = str.length();
        for(int i=0;i<len;i++) {
            N[i] = str[i] - '0';
        }

        while(!f(len));

        printf("Case #%d: ", tc);
        bool isLeading = true;
        for(int i=0;i<len;i++) {
            if(N[i] != 0 && isLeading) {
                isLeading = false;
            }
            if(isLeading && N[i] == 0);
            else printf("%d", N[i]);
        }
        printf("\n");
    }
    return 0;
}
