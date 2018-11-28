#include<bits/stdc++.h>
using namespace std;

bool check(long long n){
    int rem1=n%10;
    while(n>0){
        n/=10;
        int rem2=n%10;
        if(rem2>rem1) return false;
        else
            rem1=rem2;
    }
    return true;
}
int main()
{
    freopen("B.txt","r",stdin);
    freopen("B-out.txt","w",stdout);
    int tc,cnt=1;
    cin>>tc;
    while(tc--){
        long long n;
        cin>>n;
        while(n>0){
        if(check(n))
            {cout<<"Case #"<<cnt++<<": "<<n<<"\n";
              break;}
         --n;
        }

    }
}
