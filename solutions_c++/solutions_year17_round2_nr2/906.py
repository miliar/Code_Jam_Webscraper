#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>

bool check(int t, int o, int &b, int n, std::stringstream &ob, char oc, char bc)
{
    if (o > 0)
    {
        if (o == b)
        {
            if (n == o + b)
            {
                for(int i = 0; i < o; i++)
                    ob << bc << oc;
                printf("Case #%d: %s\n", t, ob.str().c_str());
                return true;
            }
            else
            {
                printf("Case #%d: IMPOSSIBLE\n", t);
                return true;
            }
        }
        else if (o > b)
        {
            printf("Case #%d: IMPOSSIBLE\n", t);
            return true;
        }
        else
        {
            for(int i = 0; i < o; i++)
                ob << bc << oc;
            ob << bc;
            b = b - o;
        }
    }
    return false;
}

void method(std::stringstream &answer, int j, std::stringstream &ob, std::stringstream &gr, std::stringstream &vy, int fl[3]) {
    switch(j)
    {
    case 0:
        if (fl[j] == 0)
        {
            answer << ob.str();
            fl[j] = 1;
        }
        else
            answer << 'B';
        break;
    case 1:
        if (fl[j] == 0)
        {
            answer << gr.str();
            fl[j] = 1;
        }
        else
            answer << 'R';
        break;
    case 2:
        if (fl[j] == 0)
        {
            answer << vy.str();
            fl[j] = 1;
        }
        else
            answer << 'Y';
        break;
    }
}

void solving(int t)
{
    std::stringstream ob;
    std::stringstream gr;
    std::stringstream vy;
    std::stringstream answer;

    int n, r, o, y, g, b, v;
    scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);

    if (check(t, o, b, n, ob, 'O', 'B'))
        return;
    if(check(t, g, r, n, gr, 'G', 'R'))
        return;
    if(check(t, v, y, n, vy, 'V', 'Y'))
        return;

    fflush(stdout);
    if (b + r < y || b + y < r || r + y < b)
    {
        printf("Case #%d: IMPOSSIBLE\n", t);
        return;
    }

    int fl[3] = {0};
    if (ob.str().size() == 0)
        fl[0] = 1;
    if (gr.str().size() == 0)
        fl[1] = 1;
    if (vy.str().size() == 0)
        fl[2] = 1;

    int count[3] = {b, r, y};

    int prev = -2;

    int best = 0;
    int besti = -1;
    for (int i = 0; i < 3; i++)
    {
        if (count[i] > best)
        {
            best = count[i];
            besti = i;
        }
    }
    int in[3];
    in[0] = besti;
    in[1] = (besti + 1) % 3;
    in[2] = (besti + 2) % 3;

    for (int i = 0; i < best; i++)
    {
        method(answer, in[0], ob, gr, vy, fl);
        if (i < count[in[1]]) {
            method(answer, in[1], ob, gr, vy, fl);
        }
        if (i >= best - count[in[2]]) {
            method(answer, in[2], ob, gr, vy, fl);
        }
    }

    printf("Case #%d: %s\n", t, answer.str().c_str());
    fflush(stdout);
}

int main()
{
    int t, T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++)
        solving(t);

    return 0;
}
