#include <bits/stdc++.h>
using namespace std;

const int  MAX =2e5+69;
pair<int,int> A[MAX];
int n,d;
typedef long double ld;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("solSEXX.txt", "w", stdout);
    int t;
    cin>>t;

    for(int testnumber = 1;testnumber <= t;++testnumber)
    {
        cin>>d>>n;
        for(int i=0;i<n;++i)
        {
            scanf("%d%d",&A[i].first,&A[i].second);
        }
        long double mx = 0.0;
        for(int i=0;i<n;i++)
        {
            mx = max(mx,((ld)d-A[i].first)/A[i].second);
        }

        printf("Case #%d: ",testnumber);
        cout<<setprecision(6)<<fixed<<1.0*d/mx<<endl;
    }

    return 0;
}
