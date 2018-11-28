#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<map>

using namespace std;

FILE* FileRead = fopen("C-small-2-attempt0.in", "r");
FILE* FileWrite = fopen("ThisIsOutput2.txt", "w");

main()
{


    int caseCount;
    fscanf(FileRead, "%d", &caseCount);
    int stallCount;
    int peopleCount;

    for(int currentCase = 1 ; currentCase <= caseCount ; currentCase++)
    {
        fprintf(FileWrite, "Case #%d: ", currentCase);
        fscanf(FileRead, "%d %d", &stallCount, &peopleCount);

        map<int,int> M;
        map<int,int>::iterator MIter;
        M[stallCount] = 1;

        int ansMin;
        int ansMax;
        int temp;

        for(int i = 0 ; i < peopleCount ; i++)
        {
            MIter = M.end();
            MIter--;
            temp = (*MIter).first;

            if(temp % 2 == 1)
            {
                ansMin = (temp - 1) / 2;
                ansMax = (temp - 1) / 2;
                if(M.find(ansMin) == M.end()) M[ansMin] = 2;
                else M[ansMin] += 2;
            }
            else
            {
                ansMin = (temp - 1) / 2;
                ansMax = temp / 2;

                if(M.find(ansMin) == M.end()) M[ansMin] = 1;
                else M[ansMin] += 1;

                if(M.find(ansMax) == M.end()) M[ansMax] = 1;
                else M[ansMax] += 1;
            }

            if(M[temp] == 1) M.erase(temp);
            else M[temp]--;

            if(ansMin == 0 && ansMax == 0)
            {
                break;
            }
        }

        fprintf(FileWrite, "%d %d\n", ansMax, ansMin);

        printf("Case %d Success\n", currentCase);
    }
}
