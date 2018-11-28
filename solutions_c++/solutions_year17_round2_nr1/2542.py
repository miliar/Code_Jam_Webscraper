#include<bits/stdc++.h>
using namespace std;
int arr[1234];
int main()
{
    //freopen("input.in","r", stdin);
    freopen("output.out","w", stdout);
    int n, d, t;
    scanf("%d",&t);
    for(int tc = 1; tc <= t; tc++)
    {
        scanf("%d%d",&d,&n);
        priority_queue<double> pq;
        while(n--)
        {
            int cur, s;
            scanf("%d%d",&cur, &s);
            double tym = (double) (d - cur)/s;
            pq.push(tym);
        }
        double tym = pq.top();
        printf("Case #%d: %.10f\n",tc, (double) d/tym);
    }

}
