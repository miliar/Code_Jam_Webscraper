#include <bits/stdc++.h>
using namespace std;

//--------------------------------------------------------------------//
#define ll long long int
#define ull unsigned long long int
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define fr(t,i,x) for(int i=t; i<x; ++i) // t = start index
#define mod 1000000007
#define endl "\n"
#define fi first
#define se second
#define output freopen("output.txt","w", stdout)
#define input freopen("input.txt","r", stdin)
//--------------------------------------------------------------------//

struct mycom
{
    bool operator()(pair<int,int> p,pair<int,int> q)
    {
       return (p.second - p.first ) < (q.second - q.first);
    }
};

int main() 
{
    //clock_t tstart = clock();
    //output;
    //input;
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int test, lst;
    cin>>test;
    fr(0,t,test)
    {
        ll n, k, ls=0, rs=0;
        cin>>n>>k;
        if(n==k)
        {
            ls=0;rs=0;
            cout<<"Case #"<<t+1<<": "<<max(ls, rs)<<" "<<min(ls, rs)<<endl;
        } 
        else
        {
            //priority_queue< pair<int, int> > pq;
            priority_queue< pair<int, int> , vector< pair<int, int> >, mycom > pq;
            pq.push(mp(1,n+2));
            int tem, toop, pos, mid;
            fr(0,i,k)
            {
                toop=pq.top().fi;
                pos=pq.top().se;
                //cout<<toop<<" "<<pos<<endl;
                pq.pop();

                mid=toop + (pos - toop)/2;
                pq.push(mp(toop,mid));
                pq.push(mp(mid,pos));
            }
            //cout<<s<<endl;
            cout<<"Case #"<<t+1<<": "<<max(pos - mid-1, mid - toop -1)<<" "<<min(pos - mid-1, mid - toop -1)<<endl;
        }
    }

    //cout<<"\nTotal Time Taken : "<<(double)(-tstart + clock())/CLOCKS_PER_SEC<<"sec\n";
    return 0;
}