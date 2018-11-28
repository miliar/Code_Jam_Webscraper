#include<bits/stdc++.h>

using namespace std;

int num[20];
int answer[20];
bool haveAnswer;

void dfs(int pre,bool limited,int pos)
{
    if(pos == 0)
    {
        haveAnswer = true;
        return;
    }
    int bound = limited ? num[pos] : 9;
    for(int i = bound;i >= pre && !haveAnswer;i--)
    {
        answer[pos] = i;
        dfs(i,limited && i == bound,pos - 1);
    }
}
int main()
{
    //freopen("out.txt","w+",stdout);

    int T;
    long long N;
    scanf("%d",&T);
    for(int caseNum = 1;caseNum <= T;caseNum++)
    {
        haveAnswer = false;

        scanf("%I64d",&N);
        int digit = 0;
        while(N)
        {
            num[++digit] = N % 10;
            N /= 10;
        }
        dfs(0,true,digit);

        printf("Case #%d: ",caseNum);
        if(answer[digit])
            printf("%d",answer[digit]);
        for(int i = digit - 1;i > 0;i--)
            printf("%d",answer[i]);
        putchar('\n');
    }
    return 0;
}
