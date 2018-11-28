#include <bits/stdc++.h>
#define int long long
#define pii pair <int,int>
#define piii pair < pair<int,int> ,int>
#define f first
#define s second
#define pb push_back
#define N 1005
#define mod 1000000007
#define inf 100000000000000000
#define frew freopen ("C:/Users/Sachin/Desktop/out1.txt","w",stdout);
#define frer freopen ("C:/Users/Sachin/Desktop/A-large.in","r",stdin);
#define pi 3.1415926535897932384626

using namespace std;

pii a[N];


main()
{
    frer;
    frew;
    int t;
    cin>>t;
    for(int w=1;w<=t;w++)
    {
        int i,j,n,k,ans=-inf;
        cin>>n>>k;
        for(i=0;i<n;i++)
            cin>>a[i].f>>a[i].s;
        sort(a,a+n);
        int temp[N];
        for(i=k-1;i<n;i++)
        {
            int x=a[i].f*a[i].f+2*a[i].f*a[i].s;
            for(j=0;j<i;j++)
            {
                temp[j]=2*a[j].f*a[j].s;
            }
            sort(temp,temp+i);
            for(j=i-1;j>=i-k+1;j--)
            {
                x+=temp[j];
            }
            ans=max(ans,x);
        }
        double anss=ans*pi;
        cout<<"Case #"<<w<<": ";
        printf("%.15f\n",anss);

    }
}
