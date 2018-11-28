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
        lli ara[1005]= {0};

        string str;
        cin>>str;

        for(lli i=0; i<str.size(); i++)
        {
            if(str[i]=='-') ara[i]=0;
            else ara[i]=1;
        }

        lli k;
        cin>>k;

        lli ans=0;
        bool mark= false;


        for(lli i=0; i<=str.size()-k; i++)
        {
            //cout<<ara[i]<<" before "<<i<<endl;
            if(ara[i]==0)
            {
                //cout<<"in "<<i<<endl;
                for(lli j=i ; j<i+k; j++)
                {
                    //cout<<"j "<<j<<" ara[j] "<<ara[j]<<" i "<<i<<endl;
                    if(ara[j]==0) ara[j]=1;
                    else if(ara[j]==1) ara[j]=0;
                }
                ans++;
            }
//            cout<<ara[i]<<" after "<<i<<endl;
//            cout<<ans<<endl;
//            for(lli j=0; j<str.size(); j++) cout<<ara[j]<<" ";
//            cout<<endl;


        }

        for(lli i=str.size()-k; i<str.size(); i++)
        {
            if(ara[i]==0) mark=true;
        }

        if(mark) printf("Case #%lli: IMPOSSIBLE\n",t );
        else printf("Case #%lli: %lli\n", t, ans);
    }

    return 0;
}
