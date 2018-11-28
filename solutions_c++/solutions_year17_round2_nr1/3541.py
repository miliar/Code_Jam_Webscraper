#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
#define fi first
#define se second
#define ld long double
using namespace std;
struct node{
ld x,y;
}a[10004];
bool check(node a,node b)
{
    return a.x<b.y;
}
ld ans[10004];
int main()
{
    freopen("txtin.txt","r",stdin);
    freopen("txtout.txt","w",stdout);
    ll t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cout<<"Case #"<<test<<": ";
        ld ans1,ans2,m,k,l,temp=0.0;
        int n,i,j;
        cin>>m>>n;
        for(i=1;i<=n;i++)
        {
            cin>>a[i].x>>a[i].y;
            temp=max(temp,(m-a[i].x)/a[i].y);
        }
        //sort(a+1,a+n+1,check);
        ans[n+1]=0.0;
        ld temp2=m/temp;
        printf("%.10Lf\n",temp2);
        //cout<<ans<<"\n";
    }
    return 0;
}
