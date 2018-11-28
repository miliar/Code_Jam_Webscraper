#include<bits/stdc++.h>
using namespace std;
struct data
{
    double speed, position;
}ara[1001];
bool cmp(data a, data b)
{
    if(a.position>b.position)
        return true;
    else return false;
}
int main()
{
    int i, t, cs= 0, n;
    double x, y, tm, d, res;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &t);
    while(t--)
    {
        scanf("%lf %d", &d, &n);

        for(int i=0; i<n; i++)
            scanf("%lf %lf", &ara[i].position, &ara[i].speed);

        sort(ara, ara+n, cmp);

//        for(int i=0; i<n; i++)
//            cout<<ara[i].position<<endl;

        tm= 0.0;
        for(int i=n-1; i>=0; i--)
        {
            x= d-ara[i].position;
            y= x/ara[i].speed;
//            cout<<y<<endl;
            tm= max(tm, y);
        }
        res= d/tm;

        printf("Case #%d: %.6lf\n", ++cs, res);
    }

    return 0;
}
