#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("out.txt","w+",stdout);
    int T;
    int D,N;
    scanf("%d",&T);
    for(int caseNum = 1;caseNum <= T;caseNum++)
    {
        scanf("%d%d",&D,&N);
        //cout << D << ' '<< N << endl;
        double maxTime = 0;
        int pos,speed;
        for(int i = 0;i < N;i++)
        {
            scanf("%d%d",&pos,&speed);
            maxTime = max(maxTime,(D - pos) / (double)speed);
        }
        //cout << maxTime << endl;
        printf("Case #%d: %f\n",caseNum,D / maxTime);
    }
    return 0;
}
