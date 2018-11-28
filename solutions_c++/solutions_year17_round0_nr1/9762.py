#include <set>
#include <queue>
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>

bool judge(std::string str)
{
    for(int i = 0; i < str.length(); i++)
        if(str[i] == '-')
            return false;
    return true;
}

std::string filp(std::string str, int pos, int len)
{
    for(int i = 0; i < len; pos++, i++)
        str[pos] = (str[pos] == '+' ? '-' : '+');
    return str;
}

std::queue <std::string> Q;
std::set <std::string> vis;

int bfs(std::string str, int n)
{
    std::string now, next;

    vis.clear();
    while(!Q.empty()) Q.pop();
    Q.push(str); vis.insert(str);
    for(int dis = 0; !Q.empty(); dis++)
    {
        int tot = Q.size();
        while(tot--)
        {
            now = Q.front();
            //std::cout << now << std::endl;
            Q.pop();

            if(judge(now))
                return dis;
            for(int i = 0; i <= now.length()-n; i++)
            {
                next = filp(now, i, n);
                //if(now == "+++++---") std::cout << next << std::endl;
                if(vis.find(next) == vis.end())
                {
                    vis.insert(next);
                    Q.push(next);
                }
            }
        }
    }
    return -1;
}

int main()
{
    int t, n;
    std::string str;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    scanf("%d", &t);
    for(int xt = 0; xt < t; xt++)
    {
        std::cin >> str >> n;
        n = bfs(str, n);
        printf("Case #%d: ", xt+1);
        n == -1 ? puts("IMPOSSIBLE") : printf("%d\n", n);
    }

    return 0;
}