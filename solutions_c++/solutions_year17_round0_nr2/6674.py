#include <cstdio>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cstring>
using namespace std;


int T;
char str[1001];
char rstr[1001];

char* solve()
{
    int len = strlen(str);
    if( len == 1) { return str;}
    bool flag9 = false;
   
    for (int i=0;i<len; i++) {
        if(flag9) { str[i] = '9'; continue; }
        if(i!=(len-1) && str[i] > str[i+1]) {
            flag9=true;
            char temp = str[i];
            str[i]--;
            
            for(int j=i-1;j>=0;j--) {
                if(str[j] > str[j+1] ) {str[j]--; str[j+1] = '9';}
            }    
        }
    }
    
    
    
    return str;    
}

int main() {
    cin >> T;
    
    for (int t=1;t<=T;t++) {
        cin >> str;
        solve();
        printf("Case #%i: ", t);
        for(int i=0;i<strlen(str);i++) {
            if(str[i] != '0') printf("%c", str[i]);
        }
        cout << endl;
    }

    return 0;
}
