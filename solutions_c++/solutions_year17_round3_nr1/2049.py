#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define null NULL
#define ioS ios::sync_with_stdio(false);
#define mod 1000000007
#define Max 9000000000000000000
#define Min (-1)*9000000000000000000

pair<double,double> arr[10];
double g;
double pi=3.141592;
ll n;
void func(ll i,ll k,bool* vis)
{
    if(k==0)
    {
        double ans=0;
        for(ll j=i-1;j>=0;j--)
        {
            if(vis[j]==1)
            {
                ans+=2*pi*arr[j].ff*arr[j].ss;
                if(j!=i-1)
                {
                    ans-=pi*arr[j].ff*arr[j].ff;
                }
                ans+=pi*arr[j].ff*arr[j].ff;
            }
        }
        if(ans>g)
            g=ans;
        return ;
    }
    if(i==n)
    {
        return ;
    }

    vis[i]=1;
    func(i+1,k-1,vis);
    vis[i]=0;
    func(i+1,k,vis);
}

int main()
{
ioS;
ll i,j,k,l,r,m,o,t;
cin>>t;

for(o=1;o<=t;o++)
{
cin>>n>>k;
for(i=0;i<n;i++)
    cin>>arr[i].ff>>arr[i].ss;
bool vis[10]={0};
sort(arr,arr+n);
g=-1;

func(0,k,vis);



//cout<<"Case #"<<o<<": "<<g<<endl;
printf("Case #%d: %.6f\n",o,g);
}
}
