#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int R, O, Y, G, B, V;
int N;
char ans[1001];

int tried = 0;

inline int max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    return b;
}

inline bool isEligible(int before, char current)
{
    return before != current;
}

bool calc(int pos)
{
    if (pos == N)
    {
        if (isEligible(ans[pos - 1], ans[0]))
        {
            ans[pos] = '\0';
            printf("%s\n", ans);
            return true;
        }
        else
        {
            return false;
        }
    }
    tried++;
    if (tried > 100000)
    {
        return false;
    }

    vector<pair<int, pair<char, int *>>> sorter;

    sorter.push_back(make_pair(-R, make_pair('R', &R)));
    sorter.push_back(make_pair(-Y, make_pair('Y', &Y)));
    sorter.push_back(make_pair(-B, make_pair('B', &B)));

    sort(sorter.begin(), sorter.end());

    for (int i = 0; i < sorter.size(); i++)
    {
        if (sorter[i].first == 0)
        {
            continue;
        }

        char chr = sorter[i].second.first;
        if (pos == 0 || isEligible(chr, ans[pos - 1]))
        {
            ans[pos] = chr;
            (*(sorter[i].second.second))--;
            if (calc(pos + 1))
            {
                return true;
            }
            (*(sorter[i].second.second))++;
        }
    }

    return false;
}

void testcase()
{
    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
    tried = 0;
    if (calc(0) == false)
    {
        printf("IMPOSSIBLE\n");
    }
}

int main()
{
    int tc, t;

    scanf("%d", &tc);
    for (t = 1; t <= tc; t++)
    {
        printf("Case #%d: ", t);
        testcase();
    }

    return 0;
}
