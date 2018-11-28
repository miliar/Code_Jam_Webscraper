#include <cstdio>
#include <map>

using namespace std;

inline long long maxll(long long a, long long b)
{
    return a > b ? a : b;
}

inline long long minll(long long a, long long b)
{
    return a < b ? a : b;
}

void tcase()
{
    long long startingSize, count;
    scanf("%lld %lld", &startingSize, &count);

    map<long long, long long> countMap;

    countMap[-startingSize] = 1;

    while (countMap.size() > 0)
    {
        auto firstElem = countMap.begin();
        long long curSize = -(firstElem->first);
        long long curCount = firstElem->second;
        long long leftSize = (curSize - 1) / 2;
        long long rightSize = curSize / 2;

        if (count <= curCount)
        {
            printf("%lld %lld\n", maxll(leftSize, rightSize), minll(leftSize, rightSize));
            return;
        }

        count -= curCount;

        countMap.erase(firstElem);

        countMap[-leftSize] += curCount;
        countMap[-rightSize] += curCount;
    }

    printf("ERROR\n");
}

int main()
{
    int tNo;

    scanf("%d", &tNo);

    for (int t = 1; t <= tNo; t++)
    {
        printf("Case #%d: ", t);
        tcase();
    }
}
