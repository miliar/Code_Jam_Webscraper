#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;
struct Horse
{
    long double k;
    long double s;

};
bool lesss(Horse i,Horse j) { return (i.k<j.k);}

int main()
{
    int T;
    long double D, N;
    scanf("%d",&T);
    long double time;
    for(int t=1;t<=T;t++)
    {
        DI(t)
        printf("Case #%d: ",t);
        cin >> D >> N;
        vector<Horse> horses(N);
        time = 0;
        for(auto& h : horses)
        {
            cin >> h.k >> h.s;
            long double tmpTime = (D - h.k) / h.s;
            if(tmpTime > time)
                time = tmpTime;
        }
        //sort(horses.begin(), horses.end(), lesss);


        printf("%.6lf\n",  D / time );
     //   cout << D / time << endl;
    }
    return 0;
}
