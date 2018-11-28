#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ",t);
        double d; int n;
        scanf("%Lf", &d);
        scanf(" %d", &n);
        double pos, sp;
        double q = 0;
        for(int i=1; i<=n; i++)
        {
        	scanf(" %Lf %Lf", &pos, &sp);
        	q = max(q, (d-pos)/sp );
        }
        printf("%Lf\n", d/q);
    }
    return 0;
}
