#include <cstdio>
#include <ios>
#include <iostream>
#include <string>

bool can(char col, char test)
{
    if (col == 'R')
        return (test != 'R' && test != 'O' && test != 'V');
    else if (col == 'Y')
        return (test != 'Y' && test != 'O' && test != 'G');
    else //B
        return (test != 'B' && test != 'G' && test != 'V');
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc, n, r, ry, y, yb, b, rb;
    std::cin >> tc;
    for (int t = 0; t < tc; t++)
    {
        std::cin >> n >> r >> ry >> y >> yb >> b >> rb;
        std::cout << "Case #" << t+1 << ": ";
        int color_total = (r > 0) + (b > 0) + (y > 0) + (rb > 0) + (ry > 0) + (yb > 0);
        if (color_total == 1)
            std::cout << "IMPOSSIBLE\n";
        else if (color_total == 2)
        {
            if (r && b)
            {
                if (r == b)
                {
                    for (int i = 0; i < r; i++)
                        std::cout << "RB";
                    std::cout << '\n';
                }
                else
                    std::cout << "IMPOSSIBLE\n";
            }
            else if (r && y)
            {
                if (r == y)
                {
                    for (int i = 0; i < r; i++)
                        std::cout << "RY";
                    std::cout << '\n';
                }
                else
                    std::cout << "IMPOSSIBLE\n";
            }
            else if (r && yb)
            {
                if (r == yb)
                {
                    for (int i = 0; i < r; i++)
                        std::cout << "RG";
                    std::cout << '\n';
                }
                else
                    std::cout << "IMPOSSIBLE\n";
            }
            else if (y && b)
            {
                if (y == b)
                {
                    for (int i = 0; i < y; i++)
                        std::cout << "YB";
                    std::cout << '\n';
                }
                else
                    std::cout << "IMPOSSIBLE\n";
            }
            else if (y && rb)
            {
                if (y == rb)
                {
                    for (int i = 0; i < y; i++)
                        std::cout << "YV";
                    std::cout << '\n';
                }
                else
                    std::cout << "IMPOSSIBLE\n";
            }
            else if (b && ry)
            {
                if (b == ry)
                {
                    for (int i = 0; i < b; i++)
                        std::cout << "BO";
                    std::cout << '\n';
                }
                else
                    std::cout << "IMPOSSIBLE\n";
            }
            else
                std::cout << "IMPOSSIBLE\n";
        }
        else if (color_total >= 3)
        {
            std::string ans = "";
            if (ry)
            {
                while (ry)
                {
                    ans += 'B';
                    b--;
                    ans += 'O'; //ry
                    ry--;
                }
                ans += 'B';
                b--;
            }
            if (yb)
            {
                while (yb)
                {
                    ans += 'R';
                    r--;
                    ans += 'G'; //yb
                    yb--;
                }
                ans += 'R';
                r--;
            }
            if (rb)
            {
                while (rb)
                {
                    ans += 'Y';
                    y--;
                    ans += 'V'; //yb
                    rb--;
                }
                ans += 'Y';
                y--;
            }
            if (r < 0 || b < 0 || y < 0)
                std::cout << "IMPOSSIBLE\n";
            else
            {
                bool fail = false;
                if (ans.length() == 0)
                {
                    //there are at least three because of the guarantee 3 <= N
                    if (r == 0 || y == 0 || b == 0)
                    {
                        std::cout << "IMPOSSIBLE\n";
                        fail = true;
                    }
                    else
                    {
                        ans += "RBY";
                        r--; b--; y--;
                    }
                }
                if (!fail) //length will always be at least 3 now
                {
                    bool found = true;
                    while ((r || y || b) && found)
                    {
                        found = false;
                        for (int i = 0; i < ans.length(); i++)
                        {
                            if (i == 0)
                            {
                                if (r && can('R', ans.at(i)) && can('R', ans.at(ans.length()-1)))
                                {
                                    ans.insert(0, "R");
                                    found = true;
                                    r--;
                                }
                                if (y && can('Y', ans.at(i)) && can('Y', ans.at(ans.length()-1)))
                                {
                                    ans.insert(0, "Y");
                                    found = true;
                                    y--;
                                }
                                if (b && can('B', ans.at(i)) && can('B', ans.at(ans.length()-1)))
                                {
                                    ans.insert(0, "B");
                                    found = true;
                                    b--;
                                }
                            }
                            else
                            {
                                if (r && can('R', ans.at(i)) && can('R', ans.at(i-1)))
                                {
                                    ans.insert(i, "R");
                                    found = true;
                                    r--;
                                }
                                if (y && can('Y', ans.at(i)) && can('Y', ans.at(i-1)))
                                {
                                    ans.insert(i, "Y");
                                    found = true;
                                    y--;
                                }
                                if (b && can('B', ans.at(i)) && can('B', ans.at(i-1)))
                                {
                                    ans.insert(i, "B");
                                    found = true;
                                    b--;
                                }
                            }
                        }
                    }
                    if (ans.length() == n)
                        std::cout << ans << '\n';
                    else
                        std::cout << "IMPOSSIBLE\n";
                }
            }
        }
    }
}
