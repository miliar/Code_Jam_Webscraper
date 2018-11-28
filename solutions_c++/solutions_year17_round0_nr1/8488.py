#include <cstdio>
#include <cstring>

using namespace std;

int ans;
int length;

void solve(char *S, int index, int k, int happyCount, int flipCount, int length)
{
    if (index > length)
        return;

    char ori[k];
    memcpy(ori, S + (index - k), k);

    int newHappyCount = happyCount;

    for (int i = index - k; i < index; i++)
    {
        if (S[i] == '+')
        {
            newHappyCount--;
            S[i] = '-';
        }
        else
        {
            newHappyCount++;
            S[i] = '+';
        }
    }

    if (newHappyCount == length)
    {
       if (flipCount < ans)
            ans = flipCount;
    }

    solve(S, index + 1, k, newHappyCount, flipCount + 1, length);

    memcpy(S + (index - k), ori, k);

    solve(S, index + 1, k, happyCount, flipCount, length);
}

int main()
{
    int T;
    scanf("%d", &T);

    const int INT_MAX = (1 << 31) - 1;
    char S[2000];
    int K;
    for (int t = 1; t <= T; t++)
    {
        scanf("%s", S);
        scanf("%d", &K);

        ans = INT_MAX;
        length = 0;
        int happyCount = 0;
        while (S[length] != '\0')
        {
            if (S[length] == '+')
                happyCount++;
            length++;
        }

        printf("Case #%d: ", t);
        if (happyCount == length)
            printf("0\n");
        else
        {
            solve(S, K, K, happyCount, 1, length);
            if (ans == INT_MAX)
                printf("IMPOSSIBLE\n");
            else
                printf("%d\n", ans);
        }
    }
    return 0;
}
