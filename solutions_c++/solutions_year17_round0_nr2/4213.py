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
int arr[mxx];
int sum[mxx];
int dp[mxx][mxx];
int mymin(vi v)
{
    return *min_element(v.begin(),v.end());
}
bool is_tidy(ll n)
{
    string str = to_string(n);
    fr(i,str.length()-1)
    {
        if(str[i]>str[i+1])
            return false;
    }
return true;
}
ll next_tidy(ll n)
{
    string str = to_string(n),sstr,tstr;
    ll temp;
    int l = str.length();
    int i;
    fr(iii,l+1)
    for(i=1;i<l;i++)
    {
      if(str[i]<str[i-1])
      {
        tstr = "";
        for(int k=i;k<l;k++)
            tstr += '9';
        sstr = str.substr(0,i);
        temp = stoll(sstr);
        temp--;
        sstr = to_string(temp);
        str = sstr+tstr;
        l = str.length();
        break;
      }  
    }
    return  stoll(str);
}
int main()
{
    clock_t tstart = clock();
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cout<<fixed<<setprecision(2);
    int t;
    cin>>t;
    int case_number = 1;
    while(t--)
    {
        cout<<"Case #"<<case_number++<<": ";
        ll n;
        cin>>n;
        cout<<next_tidy(n)<<"\n";
    }
    //cout<<"\n\nTotal Time Taken : "<<(double)(-tstart + clock())/CLOCKS_PER_SEC<<"sec\n\n";
    return 0;
}