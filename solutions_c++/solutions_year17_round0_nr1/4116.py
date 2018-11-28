#include<cstdio>
#include<iostream>
#include<cstring>



int inputSize;

main()
{
    FILE* FileRead = fopen("A-large.in", "r");
    FILE* FileWrite = fopen("ThisIsOutput2.txt", "w");

    int caseCount;
    fscanf(FileRead, "%d", &caseCount);

    for(int currentCase = 1 ; currentCase <= caseCount ; currentCase++)
    {
        fprintf(FileWrite, "Case #%d: ", currentCase);

        char input[1001];
        int flipSize;
        fscanf(FileRead, "%s %d", input, &flipSize);
        inputSize = strlen(input);
        int ans = 0;
        bool isCorrect = true;

        for(int i = 0 ; i <= (inputSize - flipSize) ; i++)
        {
            if(input[i] == '-')
            {
                for(int j = 0 ; j < flipSize ; j++)
                {
                    if(input[i + j] == '-') input[i + j] = '+';
                    else input[i + j] = '-';
                }
                ans += 1;
            }
        }

        for(int i = 0 ; i < inputSize ; i++)
        {
            if(input[i] == '-')
            {
                isCorrect = false;
                break;
            }
        }

        if(isCorrect) fprintf(FileWrite, "%d\n", ans);
        else fprintf(FileWrite, "IMPOSSIBLE\n");

        printf("Case %d Success\n", currentCase);

    }
}
