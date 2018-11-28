#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll  long long int
#define X first
#define Y second
using namespace std;
int main()
{
    ll t,k,i,j,c,n,m;
    ofstream out;int pp=1;
    out.open("output.txt");
    cin>>t;
    while(t--)
    {
        cin>>n;
        cout<<"Case #"<<pp<<": ";
        out<<"Case #"<<pp<<": ";pp++;
        vector<ll> v;
        j=0;k=n;m=1;
        while(k>0)
        {
            k/=10;m*=10;
            j++;
        }
        //cout<<m<<" "<<j<<endl;
        ll pre=0;
        v.pb(0);
        for(i=0;i<j;i++)
        {
            m/=10;
            if(n/m>=pre) {v.pb(n/m);pre=n/m;}
            else {break;}
            n%=m;
        }
        if(i!=j)
        {for(k=i;k>0;k--)
            if(v[k]>v[k-1]) {v[k]--;break;}
            else v[k]=9;
        for(;i<j;i++)
            v.pb(9);}
        n=0;
        for(i=0;i<v.size();i++) n=n*10+v[i];
        cout<<n<<endl;
        out<<n<<endl;
    }
    return 0;
}
