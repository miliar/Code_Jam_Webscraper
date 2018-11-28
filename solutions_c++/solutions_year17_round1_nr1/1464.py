#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<cmath>

#include<algorithm>
#include<bitset>
#include<complex>
#include<deque>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<stack>
#include<string>
#include<set>
#include<vector>
using namespace std;

int r, c;
char str[30][30];

bool isAllEmpty(char s[]){
    for (int i = 0; i < c; i++)
        if(s[i] != '?') return false;
    return true;
}

void sol(char s[]){
    for (int i = 0; i < c; i++) {
        if(s[i] != '?'){
            for (int j = i+1; j < c; j++) {
                if(s[j] == '?')
                    s[j] = s[i];
                else
                    break;
            }
            for (int j = i-1; j >= 0; j--) {
                if(s[j] == '?')
                    s[j] = s[i];
                else
                    break;
            }
        }
    }
}

int main(int argc, const char *argv[])
{
    int tn;
    cin >> tn;
    for(int z = 1; z <= tn; z++){
        cin >> r >> c;
        for (int i = 0; i < r; i++)
            scanf("%s", str[i]);
        for (int i = 0; i < r; i++) {
            if(!isAllEmpty(str[i]))
                sol(str[i]);
        }
        for (int i = 0; i < r; i++) {
            if(!isAllEmpty(str[i])){
                for (int j = i+1; j < r; j++) {
                    if(isAllEmpty(str[j]))
                        strcpy(str[j], str[i]);
                    else
                        break;
                }
                for (int j = i-1; j >= 0; j--) {
                    if(isAllEmpty(str[j]))
                        strcpy(str[j], str[i]);
                    else
                        break;
                }
            }
        }
        printf("Case #%d:\n", z);
        for (int i = 0; i < r; i++) {
            printf("%s\n", str[i]);
        }
    }
    return 0;
}
