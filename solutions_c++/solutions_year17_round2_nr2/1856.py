#include<cstdio>
#include<vector>
#include<utility>
#include<queue>

using namespace std;

char get_char(int num)
{
    if (num == 1)
        return 'R';
    else if (num == 2)
        return 'O';
    else if (num == 3)
        return 'Y';
    else if (num == 4)
        return 'G';
    else if (num == 5)
        return 'B';
    else if (num == 6)
        return 'V';
}

int main(int argc, char** argv)
{
    int t, n, next, v, num, temp;
    FILE *input, *output;

    if (argc != 3)
    {
        printf("input을 제대로 넣어주세요.\n");
        return 0;
    }

    input = fopen(argv[1], "r+");
    output = fopen(argv[2], "w+");

    fscanf(input, "%d", &t);

    priority_queue<pair<int, int> > exist;
    vector<int> ring;

    for (int i = 1; i <= t; i++)
    {
        fscanf(input, "%d", &n);

        ring.clear();
        ring.resize(n);

        for (int j = 1; j <= 6; j++)
        {
            fscanf(input, "%d", &temp);
            if (temp != 0)
                exist.push(make_pair(temp, j));
        }

        temp = exist.top().first;
        if (exist.top().first > n / 2)
        {
            while (!exist.empty())
                exist.pop();
            fprintf(output, "Case #%d: IMPOSSIBLE\n", i);
        }
        else
        {
            num = exist.top().first;
            v = exist.top().second;
            if (num > n / 3)
            {
                for (int j = 0; j < num; j++)
                    ring[j * 2] = v;

                exist.pop();

                if (!exist.empty())
                {
                    num = exist.top().first;
                    v = exist.top().second;
                    for (int j = 0; j < num; j++)
                        ring[n - n % 2 - 1 - j * 2] = v;

                    exist.pop();
                    if (!exist.empty())
                    {
                        num = exist.top().first;
                        v = exist.top().second;
                        for (int j = 0; j < n; j++)
                        {
                            if (ring[j] == 0)
                                ring[j] = v;
                        }
                    }
                }
            }
            else
            {
                next = 0;
                while (!exist.empty())
                {
                    num = exist.top().first;
                    v = exist.top().second;
                    for (int j = 0; j < num; j++)
                        ring[next + j * 3] = v;
                    exist.pop();
                    next++;
                }
            }

            while (!exist.empty())
                exist.pop();

            fprintf(output, "Case #%d: ", i);
            for (int j = 0; j < n; j++)
                fprintf(output, "%c", get_char(ring[j]));
            fprintf(output, "\n");
        }

    }

    fclose(input);
    fclose(output);

    return 0;
}
