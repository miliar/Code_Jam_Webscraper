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
#define pqi priority_queue<int>
#define fr(i,n) for(int i=0;i<n;i++)
#define mxx 101
#define mmm INT_MAX
#define mymod 10000000007
#define pcal 1e-7
int main()
{
    clock_t tstart = clock();
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    //cout<<fixed<<setprecision(2);
    int tst;
    cin>>tst;
    int case_number = 1;
    //brute force for checking answer
    while(tst--)
    {
        cout<<"Case #"<<case_number++<<": ";
        ll n,k;
        cin>>n>>k;
        if(n==k)
        {
            cout<<"0 0\n";
            continue;
        }
        pqi pq;
        pq.push(n);
        ll num1,num2,num;
        fr(i,k)
        {
            ll num = pq.top();
            pq.pop();
            num1 = num/2;
            num2 = num1;
            if(num%2==0)
                num2--;
            pq.push(num1);
            pq.push(num2);

        }
        cout<<num1<<" "<<num2<<"\n";
    }
    //cout<<"\n\nTotal Time Taken : "<<(double)(-tstart + clock())/CLOCKS_PER_SEC<<"sec\n\n";
    return 0;
}