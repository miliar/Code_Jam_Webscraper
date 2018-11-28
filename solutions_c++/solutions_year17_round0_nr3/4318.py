#include<bits/stdc++.h>
#define pi                  acos(-1)
#define READ                freopen("in.txt", "r", stdin)
#define WRITE               freopen("out.txt", "w", stdout)
#define INF                 1000000000
#define dist(ax,ay,bx,by)   sqrt((ax-bx)*(ax-bx)+(ay-by)*(ay-by))
#define M                   1000000
#define gcd(a,b)            __gcd(a,b)
#define lcm(a,b)            (a*b)/__gcd(a,b)
#define m_p(a,b)            make_pair(a,b)
#define pb                  push_back


using namespace std;
typedef unsigned long long llu;
typedef long long lli;


//***four direction***//
lli fx[]= {+1, -1, +0, +0};
lli fy[]= {+0, +0, +1, -1};



////***king moves***//
//lli fx[]= {+1, -1, +0, -0, +1, +1, -1, -1};
//lli fy[]= {+0, +0, +1, -1, +1, -1, +1, -1};


////***knight moves***//
//lli fx[]= {-1, -2, +2, +1, -1, -2, +1, +2};
//lli fy[]= {+2, +1, +1, +2, -2, -1, -2, -1};
//

int main()
{
    READ;
    WRITE;

    lli test;
    scanf("%lli", &test);

    for(lli t=1; t<=test; t++)
    {
        lli n, k;
        scanf("%lli %lli", &n, &k);

        priority_queue<lli>pq;

        lli a, b;
        pq.push(n);

        while(k)
        {
            k--;
            lli temp= pq.top();
            pq.pop();

            if(temp%2==0)
            {
                a= temp/2;
                b=temp/2-1;
            }

            else
            {
                a= temp/2;
                b=temp/2;
            }

            pq.push(a);
            pq.push(b);

        }

        printf("Case #%lli: %lli %lli\n", t, a,b);
    }


    return 0;
}
