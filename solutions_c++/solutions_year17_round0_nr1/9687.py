#include <iostream>
#include <cstdio>

using namespace std;

string str;
int k;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, kase = 0;
    cin >> T;
    while(T--) {
        cin >> str >> k;


        int res = 0, len = str.length();
        for(int i = 0; i < len - k + 1; i++) {
            if(str[i] == '-') {
                for(int j = i; j < i + k; j++) {
                    if(str[j] == '-')   str[j] = '+';
                    else if(str[j] == '+')   str[j] = '-';
                }
                res++;

            }
        }
        bool flag = true;
        for(int i = 0; i < str.length(); i++) {
            if(str[i] == '-') {
                flag = false;
                break;
            }
        }
        if(!flag)   printf("Case #%d: IMPOSSIBLE\n", ++kase);
        else    printf("Case #%d: %d\n", ++kase, res);
    }
}
