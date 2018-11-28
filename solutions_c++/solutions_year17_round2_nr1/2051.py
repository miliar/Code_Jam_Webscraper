#include<cstdio>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
    int t, d, n;
    double time, max;
    FILE *input, *output;

    if (argc != 3)
    {
        printf("input을 제대로 넣어주세요.\n");
        return 0;
    }

    input = fopen(argv[1], "r+");
    output = fopen(argv[2], "w+");

    fscanf(input, "%d", &t);

    vector<int> s;
    vector<int> k;

    for (int i = 1; i <= t; i++)
    {
        fscanf(input, "%d %d", &d, &n);

        s.clear();
        s.resize(n);
        k.clear();
        k.resize(n);

        for (int j = 0; j < n; j++)
            fscanf(input, "%d %d", &k[j], &s[j]);

        max = 0;
        for (int j = 0; j < n; j++)
        {
            time = (double) (d - k[j]) / s[j];
            if (time > max)
                max = time;
        }

        fprintf(output, "Case #%d: %.6f\n", i, d / max);
    }

    fclose(input);
    fclose(output);

    return 0;
}
