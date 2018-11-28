#include <cstdio>
#include <queue>

using namespace std;

struct City
{
    int maxDist;
    int speed;
};

City cities[100];
int routes[100][100];
double dp[100][100];
bool checker[100];
int cityCount;

void testcase()
{
    int questionCount;

    scanf("%d %d", &cityCount, &questionCount);

    for (int i = 0; i < cityCount; i++)
    {
        scanf("%d %d", &cities[i].maxDist, &cities[i].speed);
    }
    for (int i = 0; i < cityCount; i++)
    {
        for (int j = 0; j < cityCount; j++)
        {
            scanf("%d", &routes[i][j]);
            dp[i][j] = -1;
        }
    }

    for (int from = 0; from < cityCount; from++)
    {
        for (int i = 0; i < cityCount; i++)
        {
            checker[i] = false;
        }

        priority_queue<pair<int, int>> q;
        q.push(make_pair(0, from));
        while (!q.empty())
        {
            int totalDist = -q.top().first;
            int to = q.top().second;
            q.pop();

            if (checker[to] == true)
            {
                continue;
            }
            checker[to] = true;

            int maxDist = cities[from].maxDist;
            int curLeftDist = maxDist - totalDist;
            if (curLeftDist < 0)
            {
                break;
            }

            double totalTime = (double)totalDist / cities[from].speed;
            if (dp[from][to] < 0 || dp[from][to] > totalTime)
            {
                dp[from][to] = totalTime;
            }

            for (int i = 0; i < cityCount; i++)
            {
                if (routes[to][i] != -1)
                {
                    q.push(make_pair(-(totalDist + routes[to][i]), i));
                }
            }
        }
    }

    for (int i = 0; i < questionCount; i++)
    {
        if (i > 0)
            printf(" ");

        int from, to;
        scanf("%d %d", &from, &to);
        from--;
        to--;

        for (int j = 0; j < cityCount; j++)
        {
            checker[j] = false;
        }

        priority_queue<pair<double, int>> q;
        q.push(make_pair(0, from));
        while (!q.empty())
        {
            double dist = -q.top().first;
            int currentNode = q.top().second;
            q.pop();

            if (checker[currentNode] == true)
            {
                continue;
            }
            checker[currentNode] = true;

            if (currentNode == to)
            {
                printf("%lf", dist);
                break;
            }

            for (int j = 0; j < cityCount; j++)
            {
                if (dp[currentNode][j] >= 0)
                {
                    q.push(make_pair(-(dist + dp[currentNode][j]), j));
                }
            }
        }
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
        printf("\n");
    }

    return 0;
}
