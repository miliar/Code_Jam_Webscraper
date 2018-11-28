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
        string str;
        cin>>str;

        bool mark=false;

        while(mark==false)
        {
            mark=true;

            for(lli i=0; i<str.size()-1; i++)
            {
                if(str[i]>str[i+1])
                {
                    mark=false;
                    str[i]= str[i]-1;

                    for(lli j=i+1; j<str.size(); j++)
                    {
                        str[j]='9';
                    }
                }
            }
        }

        istringstream iss(str);
        lli ans;
        iss>>ans;

        printf("Case #%lli: %lli\n", t, ans);



    }



    return 0;
}
