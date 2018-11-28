#include<cstdio>
#include<iostream>
using namespace std;
int mm()
{
    double d;
    int n;
    scanf("%lf %d",&d,&n);
    double pos;
    double speed;
    double mx;
    for(int i=0;i<n;i++)
    {
        scanf("%lf %lf",&pos,&speed);
        //cout << pos << speed << endl;
        //printf("%lf %lf",pos,speed);
        if(i == 0)mx = (d-pos)/speed;
        else if((d-pos)/speed > mx)
        {
            mx = (d-pos)/speed;
        }
    }
    printf("%f\n",d/mx);
}
main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        printf("Case #%d: ",i+1);
        mm();
    }
}
