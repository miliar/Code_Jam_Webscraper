
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <set>
using namespace std ; 

typedef long long ll ; 

bool isEmpty(const char* s) {
    for(int i = 0 ; s[i] ; i++)
        if(s[i] != '?')
            return false ; 
    return true ; 
}

void fill(char* s) {
    int len = strlen(s);
    char lastSym = '?';
    for(int i = 0 ; i != len ; i++) {
        if(s[i] != '?')
            lastSym = s[i];
        else
            s[i] = lastSym;
    }
    for(int i = len-1 ; i >= 0 ; i--) {
        if(s[i] != '?')
            lastSym = s[i] ; 
        else
            s[i] = lastSym ; 
    }
}

char map[33][33] ;

void sol(){
    int R, C ; 
    scanf("%d%d", &R, &C) ; 
    for(int i = 0 ; i != R ; i++)
        scanf("%s", map[i]) ; 
    int lastNotEmpty = -1 ;
    int minNonEmpty = 100;
    for(int i = 0 ; i != R ; i++) {
        if(isEmpty(map[i])) {
            if(lastNotEmpty >= 0)
                strcpy(map[i], map[lastNotEmpty]);
            else
                continue;
        }
        else {
            minNonEmpty = min(minNonEmpty, i);
            lastNotEmpty = i;
            fill(map[i]);
        }
    }
    for(int i = 0 ; i != minNonEmpty ; i++) {
        strcpy(map[i], map[minNonEmpty]);
    }
    puts("");
    for(int i = 0 ; i != R ; i++)
        puts(map[i]);
}

int main()
{
    int T ; 
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        fprintf(stderr, "solving case (%d / %d)...\n", time, T) ; 
        printf("Case #%d: ", time) ; 
        sol() ; 
    }
    return 0 ; 
}


