#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <fstream>
#include <map>
using namespace std;
const int N = 2120;

char n[N];
int t;
string f[33];

void init()
{
    f[1] = "9";
    for(int i=2; i<=29; i++)
    {
        f[i] = f[i-1] + "9";
    }
}

string get_tidy(char key, int now, int len, char *s)
{
    if(now == len) return "";
    if(s[now] < key) return "-1";
    string ret = get_tidy(s[now], now+1, len, s);

    if(ret == "-1")
    {
        if(s[now] <= key) return "-1";
        char add = (s[now]-1);
        //cout<<add<<" * "<<f[len-now-1]<<" * "<<add+f[len-now-1]<<endl;
        return  add + f[len-now-1];
    }
    char add = (s[now]);
    //cout<<add<<" # "<<ret<<" # "<<add+ret<<endl;
    return add + ret;
}

int main()
{
    init();
    freopen("B-large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
        scanf("%s", n);
        int len = strlen(n);
        string ans = "";
        ans = get_tidy('0', 0, len, n);
        char ret[32];
        bool flag = true;
        int idx = 0;
        for(int j=0; j<ans.length(); j++)
        {
            if(flag && ans[j] == '0')
                continue;
            flag = false;
            ret[idx++] = ans[j];
        }
        ret[idx++] = '\0';

        printf("Case #%d: %s\n", i, ret);
    }
    return 0;
}

