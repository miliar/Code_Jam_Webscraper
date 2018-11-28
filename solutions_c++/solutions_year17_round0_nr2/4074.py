#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>

bool isCorrect(char input[]);
void printInput(char input[]);

int inputLen;

FILE* FileRead = fopen("B-large.in", "r");
FILE* FileWrite = fopen("ThisIsOutput2.txt", "w");

main()
{


    int caseCount;
    fscanf(FileRead, "%d", &caseCount);

    for(int currentCase = 1 ; currentCase <= caseCount ; currentCase++)
    {
        fprintf(FileWrite, "Case #%d: ", currentCase);

        char input[21];
        fscanf(FileRead, "%s", input);
        inputLen = strlen(input);
        int currentPosition = inputLen - 1;

        while(!isCorrect(input))
        {
            input[currentPosition] = '9';
            int temp = currentPosition - 1;
            while(temp >= 0)
            {
                if(input[temp] == '0')
                {
                    input[temp] = '9';
                    temp--;
                }
                else
                {
                    input[temp]--;
                    break;
                }
            }

            currentPosition--;
        }

        printInput(input);
        printf("Case %d Success\n", currentCase);
    }
}

bool isCorrect(char input[])
{
    bool frontZero = true;

    for(int i = 0 ; i < (inputLen - 1) ; i++)
    {
        if(frontZero)
        {
            if(input[i] != '0')
            {
                frontZero = false;
                if(input[i] > input[i + 1])
                {
                    return false;
                }
            }
        }
        else
        {
            if(input[i] > input[i + 1])
            {
                return false;
            }
        }
    }

    return true;
}

void printInput(char input[])
{
    bool frontZero = true;
    for(int i = 0 ; i < inputLen ; i++)
    {
        if(frontZero)
        {
            if(input[i] != '0')
            {
                frontZero = false;
                fprintf(FileWrite, "%c", input[i]);
            }
        }
        else
        {
            fprintf(FileWrite, "%c", input[i]);
        }
    }

    fprintf(FileWrite, "\n");
}
