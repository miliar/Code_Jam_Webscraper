
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
#include <map>

using namespace std ; 

typedef long long ll ; 

int firstDecLoc(char* str) {
    int ret = 1 ; 
    while(str[ret] >= str[ret-1])
        ret++ ; 
    return ret;
}

void sol(){
    char str[22];
    scanf("%s", str) ; 
    while(true) {
        int l = firstDecLoc(str);
        if(l == strlen(str))
            break ; 
        str[l-1]--;
        if(l-1 == 0 && str[l-1] == '0') {
            char tmp[22];
            strcpy(tmp, str+1);
            strcpy(str, tmp);
            l--;
        }
        int len = strlen(str);
        for(int i = l ; i != len ; i++)
            str[i] = '9' ; 
    }
    puts(str);
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

