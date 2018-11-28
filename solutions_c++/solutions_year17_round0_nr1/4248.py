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
    //cout<<fixed<<setprecision(2);
    int t;
    cin>>t;
    int case_number = 1;
    while(t--)
    {
        cout<<"Case #"<<case_number++<<": ";
        string str;
        cin>>str;
        int k;
        cin>>k;
        int ans = 0;
        int n = str.length();
        for(int i=0;i<=n-k;i++)
        {
            if(str[i]=='-')
            {
                ans++;
                for(int j=i;j<i+k;j++)
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
            }
        }
        bool flag = true;
        fr(i,n)
        if(str[i]=='-')
            flag = false;
        if(flag)
            cout<<ans<<"\n";
        else
            cout<<"IMPOSSIBLE\n";
    }
    //cout<<"\n\nTotal Time Taken : "<<(double)(-tstart + clock())/CLOCKS_PER_SEC<<"sec\n\n";
    return 0;
}