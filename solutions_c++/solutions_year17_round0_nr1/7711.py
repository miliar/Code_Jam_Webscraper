#include <cstdio>
#include <cstring>
#include <iostream>
#include<string>

using namespace std;

string processString(string s, int startIndex, int len)
{
    for(int i = startIndex; i<len; i++)
    {
        if(s[i]=='+') s[i] = '-';
        else if(s[i] == '-') s[i] = '+';
    }
    return s;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A_large.out", "w", stdout);
    int t;
    scanf("%d", &t);

    for (int z = 1; z <= t; z++) {
        string s;
        int count = 0;
        int n;
        cin >> s >> n;
        int len = s.size();
        size_t firstIndexOfMinus = s.find("-");
        if(firstIndexOfMinus == std::string::npos)
        {
            printf("Case #%d: %d\n", z, 0);
            continue;
        }
        for(int i=0; i<=len-n; i++)
        {
            if(s[i]=='-')
            {
                s = processString(s, i, i+n);
                count++;
            }
        }
        if(s.find("-") != std::string::npos)
        {
            printf("Case #%d: IMPOSSIBLE\n", z);
        }
        else
        {
            printf("Case #%d: %d\n", z, count);
        }
    }
}

