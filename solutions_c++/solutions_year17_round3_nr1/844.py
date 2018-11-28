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
pa val[1003];

bool compare(pa lhs,pa rhs)
{
    if(lhs.f==rhs.f)
        return lhs.s>rhs.s;
    return lhs.f>rhs.f;
}

int main()
{
    sync
    int t,i,j,k,n,l;
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>n>>k;
        for(i=1;i<=n;i++)
        {
            cin>>val[i].f>>val[i].s;
        }
        
        sort(val+1,val+1+n,compare);
        
        
        for(i=0;i<=n;i++)
        {
            a[0][i]=0;
            a[i][0]=0;
        }
        double va;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                va=2*pi*val[i].f*val[i].s;
                if(pre[i-1][j-1]==0)
                {
                    va+=pi*(val[i].f*val[i].f);
                }
                
                if(va+a[i-1][j-1]>a[i-1][j])
                {
                    a[i][j]=va+a[i-1][j-1];
                    pre[i][j]=-1;
                }
                else
                {
                    a[i][j]=a[i-1][j];
                    pre[i][j]=-1;
                }
            }
        }
        
        
        va=a[n][k];
        
        printf("Case #%d: %.8lf\n",l,va);
    }
}



