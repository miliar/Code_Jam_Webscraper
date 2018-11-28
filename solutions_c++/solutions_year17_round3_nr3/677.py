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


ld val[55];

int main()
{
    sync
    int t,i,j,k,n,l;
    cin>>t;
    ld u;
    for(l=1;l<=t;l++)
    {
        
        cin>>n>>k;
        cin>>u;
        for(i=0;i<n;i++)
        {
            cin>>val[i];
        }
        sort(val,val+n);
        ld cur=0;
        int flag=0;
        ld ans;
        for(i=0;i<n-1;i++)
        {
            if(u>=(val[i+1]-val[i])*(i+1))
            {
                u-=(val[i+1]-val[i])*(i+1);
            }
            else
            {
                cur=u/(i+1);
                flag=1;
                break;
            }
        }
        if(k==n)
        {
            if(flag==1)
            {
                ans=pow(cur+val[i],i+1);
                i++;
                for(;i<n;i++)
                {
                    ans*=val[i];
                }
            }
            else
            {
                cur=u/n;
                ans=pow(cur+val[n-1],n);
            }
            printf("Case #%d: %.8Lf\n",l,ans);
        }
        else
        {
            
        }
        
        
    }
    
}
