#include<bits/stdc++.h>
//#include <boost/multiprecision/cpp_int.hpp>
//namespace mp = boost::multiprecision;
using namespace std; 
#define ll long long int
#define dbl double
#define si set<ll>
#define vi vector<int>
#define vii vector<string>
#define mii map<int,int>
#define pii pair<int,int>
#define pff pair<double,double>
#define fr(i,n) for(int i=0;i<n;i++)
#define mxx 101
#define mmm INT_MAX
#define mymod 10000000007
#define pcal 1e-7
#define pi 3.1415926535897932384
int mymin(vi v)
{
    return *min_element(v.begin(),v.end());
}
int main()
{
    clock_t tstart = clock();
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cout<<fixed<<setprecision(10);
    int t;
    cin>>t;
    int case_number = 1;
    while(t--)
    {
        cout<<"Case #"<<case_number++<<": ";
        int n,k;
        cin>>n>>k;
        std::vector<pff> v(n);
        fr(i,n)
        {
            double a,b;
            cin>>a>>b;
            v[i] = make_pair(a,b);
        }
        double ans = 0;
        for(int iiii=1;iiii<pow(2,n);iiii++)
        {
            bitset<10> bt(iiii);
            if(bt.count()!=k)
                continue;
            std::vector<pff> vec;
            fr(i,10)
            {
                if(bt[i])
                    vec.push_back(v[i]);

            }
            sort(vec.begin(),vec.end());
            reverse(vec.begin(),vec.end());
            double temp,r,h;
            r = vec[0].first;
            h = vec[0].second;
            temp = pi*r*r + 2*pi*r*h;
            fr(i,k-1)
            {
                r = vec[i+1].first;
                h = vec[i+1].second;
                temp += 2*pi*r*h; 
            }
            ans  = max(temp,ans);
        }
        cout<<ans<<"\n";
    }
    //cout<<"\n\nTotal Time Taken : "<<(double)(-tstart + clock())/CLOCKS_PER_SEC<<"sec\n\n";
    return 0;
}