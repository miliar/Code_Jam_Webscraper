#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("out.txt","w+",stdout);
    int T;
    scanf("%d",&T);
    for(int caseNum = 1;caseNum <= T;caseNum++)
    {
        cerr << caseNum << endl;
        long long N,K;
        priority_queue<long long> q;

        scanf("%I64d%I64d",&N,&K);


        q.push(N);
        for(int i = 1;i < K;i++)
        {
            int now = q.top();
            q.pop();
            if(now % 2 && now / 2)
            {
                q.push(now / 2);
                q.push(now / 2);
            }
            else if(now % 2 == 0)
            {
                q.push(now / 2);
                if(now / 2 - 1 > 0)
                    q.push(now / 2 -1);
            }
        }
        int now = q.top();
        if(now % 2)
            printf("Case #%d: %d %d\n",caseNum,now / 2,now / 2);
        else
            printf("Case #%d: %d %d\n",caseNum,now / 2,now / 2 - 1);
    }
    return 0;
}
