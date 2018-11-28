#include <bits/stdc++.h>

using namespace std;


double  D, N;


void _main(int TEST)
{
 double maxt=0;
    double ki,si;
    scanf("%lf%lf", &D, &N);

   for(double i=0;i<N; i++)
    {
          scanf("%lf%lf", &ki, &si);
          int dik=D-ki;
         // printf("\n dik %lf\n---",D-ki);
          if(maxt<(dik/si)){
            maxt=dik/si;
          }
    }
 //printf("\n mac %lf\n---",maxt);
    //cout<<"\n res\n"<<(maxt)<<endl;
           printf("%lf\n", (D/maxt));
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        //cerr << i << endl;
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
