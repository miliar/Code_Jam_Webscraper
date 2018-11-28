#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<int,pii>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define SIZE 10000002
#define MOD 1000000007LL
#define ld long double
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(; c<'0'||c>'9'; c=getchar())if(c=='-')sign=-1;
    for(num=0; c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

priority_queue<double,vector<double>,greater<double>> PQ;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests;
    cin>>tests;

    for(int cases=1;cases<=tests;cases++)
    {
        int n,k;
        double tot;
        cin>>n>>k;
        cin>>tot;
        double req=0;

        for(int i=1;i<=n;i++)
        {
            double x;
            cin>>x;

            req+=1.0-x;

            PQ.push(x);
        }

        double ans=1;

        PQ.push(1.0);

        while(tot>0.0&&PQ.top()<1.0)
        {
            double f=PQ.top();

            int cnt=0;

            while(PQ.top()==f)
            {
                cnt++;
                PQ.pop();
            }

            double s=PQ.top();

            if(tot>(s-f)*cnt)
            {
                tot-=(s-f)*cnt;
                while(cnt--)
                {
                    PQ.push(s);
                }
            }
            else
            {
                double x=cnt;
                while(cnt--)
                {
                    PQ.push(f+tot/x);
                }
                tot=0;
            }
        }

        while(PQ.size())
        {
            ans=ans*PQ.top();
            PQ.pop();
        }

        printf("Case #%d: %0.12f\n",cases,ans);
        cerr<<cases<<endl;
    }
}
