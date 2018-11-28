#include <bits/stdc++.h>

using namespace std;

char str[10000];
int st;

void foo(int pos){
    if ( pos == -1 ){
        return;
    }
    int found = pos-1;
    for(int i = pos-1; i >= 0; i-- ){
        if ( str[i] > str[pos] ){
            for( int j = i+1; j < strlen(str); j++ ){
                str[j] = '9';
            }
            found = i;
            str[i]--;
            break;
        }
    }

    if ( found == st && str[st] == '0' ){
        st++;
    }

    foo(found);
}

int main(){
    int t;

    scanf("%d", &t);

    for( int k = 1; k <= t; k++ ){
        st = 0;
        scanf("%s", str);
        foo(strlen(str)-1);

        printf("Case #%d: ", k);
        for( int i = st; i < strlen(str); i++ ){
            printf("%c", str[i]);
        }
        puts("");
    }
}