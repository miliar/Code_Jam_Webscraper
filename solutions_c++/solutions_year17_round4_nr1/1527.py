#include<bits/stdc++.h>

using namespace std;

int T;
int N;
int G[105];
int P;

int main()
{
    freopen("out.txt","w+",stdout);
    scanf("%d",&T);
    for(int caseNum = 1;caseNum <= T;caseNum++)
    {
        scanf("%d%d",&N,&P);
        for(int i = 0;i < N;i++)
            scanf("%d",&G[i]),G[i] %= P;

        sort(G,G + N);
        int groupNum = 0;
        int* p = upper_bound(G,G+N,0);
        groupNum += p - G;
        int idx = groupNum;

        if(P == 2)
        {
            groupNum += (G + N - p) / 2;
            if((G + N - p) % 2 == 0)
                groupNum--;
        }

        if(P == 3)
        {
            int oneNum = upper_bound(p,G + N,1) - p;
            int twoNum = N - groupNum - oneNum;
            if(oneNum >= twoNum)
            {
                groupNum += twoNum + (oneNum - twoNum) / 3;
                oneNum -= twoNum;
                if(oneNum % 3 == 0)
                    groupNum--;
            }
            else
            {
                groupNum += oneNum + (twoNum - oneNum) / 3;
                twoNum -= oneNum;
                if(twoNum % 3 == 0)
                    groupNum--;
            }

        }

        if(P == 4)
        {
            int* oneP = upper_bound(p,G + N,1);
            int oneNum = oneP - p;
            int twoNum = upper_bound(oneP,G + N,2) - oneP;
            int threeNum = N - groupNum - oneNum - twoNum;

            if(oneNum >= threeNum)
            {
                groupNum += threeNum;
                oneNum -= threeNum;
                threeNum = 0;
                if(oneNum / 2 >= twoNum)
                {
                    groupNum += twoNum + (oneNum - twoNum * 2) / 4;
                    oneNum -= twoNum * 2;
                    oneNum -= oneNum / 4 * 4;
                    twoNum = 0;
                }

                else
                {
                    groupNum += oneNum / 2 + (twoNum - oneNum / 2) / 2;
                    twoNum -= oneNum / 2;
                    twoNum -= twoNum / 2 * 2;
                    oneNum -= oneNum / 2 * 2;
                }
            }
            else
            {
                groupNum += oneNum;
                threeNum -= oneNum;
                oneNum = 0;
                if(threeNum / 2 >= twoNum)
                {
                    groupNum += twoNum + (threeNum - twoNum * 2) / 4;
                    threeNum -= twoNum * 2;
                    threeNum -= threeNum / 4 * 4;
                    twoNum = 0;
                }

                else
                {
                    groupNum += threeNum / 2 + (twoNum - threeNum / 2) / 2;
                    twoNum -= threeNum / 2;
                    twoNum -= twoNum / 2 * 2;
                    threeNum -= threeNum / 2 * 2;
                }

            }
            if(oneNum == 0 && twoNum == 0 && threeNum == 0)
                groupNum--;
        }
        printf("Case #%d: %d\n",caseNum,groupNum + 1);
    }
    return 0;
}
