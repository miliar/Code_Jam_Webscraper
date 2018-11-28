#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int c[6];

bool solve(int N)
{
    c[0] -= c[3];
    c[2] -= c[5];
    c[4] -= c[1];
    if (c[0] < 0 || c[2] < 0 || c[4] < 0)
        return false;
    string ret;
    if (c[0] > c[2] && c[0] > c[4])
    {
        int loop = c[2] + c[4] - c[0];
        if (loop < 0)
            return false;
        c[0] -= loop;
        c[2] -= loop;
        c[4] -= loop;
        if (c[0] < 0 || c[2] < 0 || c[4] < 0)
            return false;
        for (int i = 0; i < c[2]; ++i)
            ret += "RY";
        for (int i = 0; i < c[4]; ++i)
            ret += "RB";
        for (int i = 0; i < loop; ++i)
            ret += "RYB";
    }
    else if (c[2] >= c[0] && c[2] > c[4])
    {
        int loop = c[0] + c[4] - c[2];
        if (loop < 0)
            return false;
        c[0] -= loop;
        c[2] -= loop;
        c[4] -= loop;
        if (c[0] < 0 || c[2] < 0 || c[4] < 0)
            return false;
        for (int i = 0; i < c[0]; ++i)
            ret += "YR";
        for (int i = 0; i < c[4]; ++i)
            ret += "YB";
        for (int i = 0; i < loop; ++i)
            ret += "YRB";
    }
    else
    {
        int loop = c[0] + c[2] - c[4];
        if (loop < 0)
            return false;
        c[0] -= loop;
        c[2] -= loop;
        c[4] -= loop;
        if (c[0] < 0 || c[2] < 0 || c[4] < 0)
            return false;
        for (int i = 0; i < c[0]; ++i)
            ret += "BR";
        for (int i = 0; i < c[2]; ++i)
            ret += "BY";
        for (int i = 0; i < loop; ++i)
            ret += "BRY";
    }
    if (ret.empty())
    {
        if (c[1] > 0)
        {
            if (c[3] != 0 || c[5] != 0)
                return false;
            for (int i = 0; i < c[1]; ++i)
                ret += "OB";
        }
        else if (c[3] > 0)
        {
            if (c[1] != 0 || c[5] != 0)
                return false;
            for (int i = 0; i < c[3]; ++i)
                ret += "GR";
        }
        else if (c[5] > 0)
        {
            if (c[1] != 0 || c[3] != 0)
                return false;
            for (int i = 0; i < c[5]; ++i)
                ret += "VY";
        }
    }
    else
    {
        if (c[1] > 0)
        {
            int pos = 0;
            while (pos < (int)ret.size() && ret[pos] != 'B')
                ++pos;
            if (pos >= (int)ret.size())
                return false;
            string tmp;
            for (int i = 0; i < c[1]; ++i)
                tmp += "OB";
            ret = ret.substr(0, pos + 1) + tmp + ret.substr(pos + 1);
        }
        if (c[3] > 0)
        {
            int pos = 0;
            while (pos < (int)ret.size() && ret[pos] != 'R')
                ++pos;
            if (pos >= (int)ret.size())
                return false;
            string tmp;
            for (int i = 0; i < c[3]; ++i)
                tmp += "GR";
            ret = ret.substr(0, pos + 1) + tmp + ret.substr(pos + 1);
        }
        if (c[5] > 0)
        {
            int pos = 0;
            while (pos < (int)ret.size() && ret[pos] != 'Y')
                ++pos;
            if (pos >= (int)ret.size())
                return false;
            string tmp;
            for (int i = 0; i < c[5]; ++i)
                tmp += "VY";
            ret = ret.substr(0, pos + 1) + tmp + ret.substr(pos + 1);
        }
    }
    printf("%s\n", ret.c_str());
    return true;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase)
    {
        int N;
        scanf("%d", &N);
        for (int i = 0; i < 6; ++i)
            scanf("%d", &c[i]);
        printf("Case #%d: ", kase);
        if (!solve(N))
            puts("IMPOSSIBLE");
    }
    return 0;
}