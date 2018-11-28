#include <bits/stdc++.h>

using namespace std;

char color[1005];

int T,R,O,Y,G,B,V;
int N;
int zero = 0;

bool vaild(int i,char c)
{
    return color[((i - 1) % N + N) % N] != c && color[(i + 1) % N] != c;
}
int main()
{
    freopen("out.txt","w+",stdout);
    scanf("%d",&T);
    for(int caseNum = 1;caseNum <= T;caseNum++)
    {
        memset(color,0,sizeof(color));
        scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);

        bool haveAnswer = true;
        for(int i = 0;i < N;i++)
        {
            char maxColor = 0;
            int* maxNum = &zero;

            if(vaild(i,'R') && (R > *maxNum || color[0] == 'R' && R >= *maxNum))
            {
                maxNum = &R;
                maxColor = 'R';
            }
            if(vaild(i,'Y') && (Y > *maxNum || color[0] == 'Y' && Y >= *maxNum))
            {
                maxNum = &Y;
                maxColor = 'Y';
            }
            if(vaild(i,'B') && (B > *maxNum || color[0] == 'B' && B >= *maxNum))
            {
                maxNum = &B;
                maxColor = 'B';
            }

            if(maxColor == 0)
            {
                haveAnswer = false;
                break;
            }

            //cout << maxColor << endl;
            color[i] = maxColor;
            (*maxNum)--;
        }

        if(!haveAnswer)
            printf("Case #%d: IMPOSSIBLE\n",caseNum);
        else
            printf("Case #%d: %s\n",caseNum,color);
    }
    return 0;
}
