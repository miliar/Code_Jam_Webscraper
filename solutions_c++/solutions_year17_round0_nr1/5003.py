#include <iostream>
#include <cstring>
#include <bitset>

using namespace std;

#define MAX 10010

char S[MAX];
bitset<MAX> st;

int moves(int k, int size)
{
    int i, count = 0;

    for (i = 0; i <= size - k; ++i)
        if (not st[i])
        {
            ++count;
            for (int j = 0; j < k; ++j)
                st.flip(i + j);
        }

    while (i < size)
        if (not st[i++])
            return -1;

    return count;
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; ++test)
    {
        int k;
        scanf("%s %d", S, &k);

        int size = strlen(S);

        for (int i = 0; i < size; ++i)
            st[i] = (S[i] == '-' ? 0 : 1);

        int count = moves(k, size);

        if (count == -1)
            printf("Case #%d: IMPOSSIBLE\n", test);
        else 
            printf("Case #%d: %d\n", test, count);
    }

    return 0;
}
