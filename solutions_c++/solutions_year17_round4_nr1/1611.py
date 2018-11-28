#include <cstdio>
#include <vector>

using namespace std;

void testcase()
{
    int groupCount, packSize;
    vector<int> groups;

    scanf("%d %d", &groupCount, &packSize);
    groups.resize(groupCount);
    for (int i = 0; i < groupCount; i++)
    {
        scanf("%d", &groups[i]);
    }

    if (packSize == 2)
    {
        int even = 0, odd = 0;
        for (int i = 0; i < groupCount; i++)
        {
            if (groups[i] % 2 == 0)
            {
                even++;
            }
            else
            {
                odd++;
            }
        }

        printf("%d", even + (odd + 1) / 2);
    }
    else if (packSize == 3)
    {
        int whole = 0, left1 = 0, left2 = 0;
        for (int i = 0; i < groupCount; i++)
        {
            if (groups[i] % 3 == 0)
            {
                whole++;
            }
            else if (groups[i] % 3 == 1)
            {
                left1++;
            }
            else
            {
                left2++;
            }
        }

        int ans = whole;
        if (left1 > left2)
        {
            ans += left2 + (left1 - left2 + 2) / 3;
        }
        else
        {
            ans += left1 + (left2 - left1 + 2) / 3;
        }

        printf("%d", ans);
    }

    printf("\n");
}

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int t = 1; t <= tc; t++)
    {
        printf("Case #%d: ", t);
        testcase();
    }
    return 0;
}