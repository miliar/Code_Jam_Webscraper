#include<bits/stdc++.h>

using namespace std;

long long logtwo(long long q)
{
    long long a=1;
    long long r=0;
    while(a<=q)
    {
        r++;
        a=a*2;
    }
    return a/2;
}

int main(void)
{
   freopen("C:\\Users\\user\\Desktop\\input.in","r",stdin);
   freopen("C:\\Users\\user\\Desktop\\output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long n,k;
        cin>>n>>k;
        //cout<<n<<" "<<k<<endl;
        long long exp=logtwo(k);
        //cout<<exp<<endl;
        long long temp=(n+1-exp)/exp;
        if((n+1-exp-exp*(temp))>=k+1-exp)
            temp++;
        cout<<"Case #"<<i<<": "<<temp/2<<" "<<(temp-1)/2<<endl;
    }
}
