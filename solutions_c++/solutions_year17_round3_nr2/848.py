//Aditya Agrawal
// DTU


#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <list>
#include <utility>
#include <iterator>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <bitset>
#include <complex>
//#include <unordered_set>
//#include <unordered_map>


#define mod 1000000007
#define ima 1000000004
#define imi -1000000004
#define llma 1000000000000000004
#define llmi -1000000000000000004
#define lp(i,n) for(i=0;i<n;i++)
#define li(i,n) for(i=n-1;i>=0;i--)
#define tree vector<list<int > >
#define ll long long int
#define ld long double
#define f first
#define s second
#define pa pair<ll,ll>
#define pad pair<double ,double>
#define pai pair<int,int>
#define mp make_pair
#define nn 100005
#define pi 3.1415926535898
#define inf 1e15
#define diff 1e-7
#define md 359999
#define it ::iterator
#define pb push_back
#define sync ios::sync_with_stdio(false);cout.tie(0);cin.tie(0);
#define lc(a) 2*a+1
#define rc(a) 2*a+2


using namespace std;

typedef complex<double> base;

double a[1003][1003];
int pre[1003][1003];
pair<pai, int> val[200];

bool compare(pair<pai,int> lhs,pair<pai,int> rhs)
{
    return lhs.f<rhs.f;
}

int main()
{
    sync
    int t,i,j,k,n,l;
    cin>>t;
    int tima,timb;
    for(l=1;l<=t;l++)
    {
        cin>>n>>k;
        tima=0;
        timb=0;
        for(i=0;i<n;i++)
        {
            cin>>val[i].f.f;
            cin>>val[i].f.s;
            tima+=val[i].f.s-val[i].f.f;
            val[i].s=1;
        }
        
        for(i=0;i<k;i++)
        {
            cin>>val[i+n].f.f;
            cin>>val[i+n].f.s;
            timb+=val[i+n].f.s-val[i+n].f.f;
            val[i].s=2;
        }
        
        sort(val,val+n+k,compare);
        
        if(n+k<=2)
        {
            if(n==2 || k==2)
            {
                if(val[1].f.s-val[0].f.f>720 && 1440-val[1].f.f+val[0].f.s>720)
                    printf("Case #%d: 4\n",l);
                else
                    printf("Case #%d: 2\n",l);
            }
            else
            {
                printf("Case #%d: 2\n",l);
            }
        }
        else
        {
            
            int prei=-1,prev=0;
            
            for(i=0;i<n+k;i++)
            {
                
            }
            
            printf("Case #%d: \n",l);
        }
    }
}

