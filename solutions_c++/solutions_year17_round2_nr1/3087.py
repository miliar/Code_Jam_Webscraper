#include<bits/stdc++.h>
#define pi                  acos(-1)
#define READ                freopen("in.txt", "r", stdin)
#define WRITE               freopen("out.txt", "w", stdout)
#define INF                 1000000000000000000
#define dist(ax,ay,bx,by)   sqrt((ax-bx)*(ax-bx)+(ay-by)*(ay-by))
#define M                   1000000
#define gcd(a,b)            __gcd(a,b)
#define lcm(a,b)            (a*b)/__gcd(a,b)
#define m_p(a,b)            make_pair(a,b)
#define pb                  push_back


using namespace std;
typedef unsigned long long llu;
typedef long long lli;
typedef long double ld;


////***four direction***//
//lli fx[]= {+1, -1, +0, +0};
//lli fy[]= {+0, +0, +1, -1};



////***king moves***//
//lli fx[]= {+1, -1, +0, -0, +1, +1, -1, -1};
//lli fy[]= {+0, +0, +1, -1, +1, -1, +1, -1};


////***knight moves***//
//lli fx[]= {-1, -2, +2, +1, -1, -2, +1, +2};
//lli fy[]= {+2, +1, +1, +2, -2, -1, -2, -1};




int main()
{
    READ;
    WRITE;
    lli test;
    cin>>test;

    for(lli t=1; t<=test; t++)
    {
        lli d, n;
        scanf("%lli %lli", &d, &n);

        double maxi=0;

        for(lli i=1; i<=n; i++)
        {
            double k, s;
            scanf("%lf %lf", &k, &s);
            //cout<<k<<"??"<<s<<endl;
            double tem1= (double) (d-k);
            //cout<<".."<<tem1<<endl;
            double temp=tem1/(double)s;

            if(maxi<temp) maxi=temp;
        }

        double ans= (double)d/ (double)maxi;

        printf("Case #%lli: %.6f\n", t, ans);


    }


    return 0;
}
