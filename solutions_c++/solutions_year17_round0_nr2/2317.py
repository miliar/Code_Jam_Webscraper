#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e5+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;

bool solve()
{
    char s1[22], s2[22];
    scanf("%s",s1);
    int n = strlen(s1);
    bool flag = false;
    for (int i = 0; i < n; ++i) {
        s2[i] = s1[i];
        if (i && s2[i] < s2[i - 1]) {
            s2[i] = '9';
            if (!flag) {
                flag = true;
                for (int j = i - 1; j >= 0; --j) {
                    s2[j]--;
                    if (j && s2[j] >= s2[j-1])
                        break;
                    else if (j)
                        s2[j] = '9';
                }
            }
        }
    }
    if (s2[0] <= '0')
        for (int i = 1; i < n; ++i)
            printf("9");
    else
        for (int i = 0; i < n; ++i)
            printf("%c", s2[i]);
    puts("");
    return false;
}

int main()
{
        freopen("input.txt","r", stdin);
        freopen("output.txt", "w", stdout);
    int countTests;
    scanf("%d", &countTests);
    for (int curTest = 1; curTest <= countTests; ++curTest) {
        printf("Case #%d: ", curTest);
        solve();
    }
    
    return 0;
}
