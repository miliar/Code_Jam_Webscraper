#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;

char N[20];

void findTidy() {
    for (int i = 1; N[i]; ++i) {
        if (N[i] < N[i-1]) {
            N[i-1] = N[i-1]-1;
            for (int j = i; N[j]; ++j) N[j] = '9';
            findTidy();
            break;
        }
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T = INPT_INT;
    for (int _case = 1; _case <= T; ++_case) {
        scanf("%s",N);
        findTidy();

        printf("Case #%d: ",_case);
        bool print = false;
        for (int i = 0; N[i]; ++i) {
            if (N[i]!='0') {
                print = true;
            }
            if (print) {
                printf("%c",N[i]);
            }
        }
        puts("");
    }
    return 0;
}
