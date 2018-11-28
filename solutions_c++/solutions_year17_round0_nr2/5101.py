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

bool test(char s[], int len){
    for (int i = 0; i < len - 1; i++)
        if(s[i] > s[i+1]) return false;
    return true;
}

void ans(char s[], int len){
    /* printf("ans \n", n); */
    /* long long gclbcotal = 0; */
    /* string s = to_string(n); */
    while(!test(s, len)){
        for (int i = 0; i < len - 1; i++){
            if(s[i] > s[i+1]){
                s[i]--;
                for (int j = i+1; j < len ; j++) {
                    s[j] = '9';
                }
                break;
            }
        }
    }
}

int main(int argc, const char *argv[])
{
    int tn;
    long long n;
    char str[40];

    cin >> tn;
    for (int i = 1; i <= tn; i++) {
        cin >> n;
        sprintf(str, "%lld", n);
        ans(str, strlen(str));
        printf("Case #%d: %lld\n", i, stoll(string(str)));
    }
    return 0;
}
