#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

#define F first
#define S second
#define Sz(s) int((s).size())
#define Fill(s,v) memset(s,v,sizeof(s))
#define f(i,n) for (int i=0; i<n; i++)
#define f1(i,n) for (int i=1; i<=n; i++)
#define fI(i,a,b) for (int i=a; i<=b; i++)



int main()
{
    freopen("A-large (1).in","rt",stdin);
    freopen("out.txt","wt",stdout);
    int t;
    cin>>t;
    for(int c=1; c<=t; c++){
    ld mxt=0.0;
    ld d,k,p,s;
    cin>>d>>k;
    for(int i=0; i<k; i++){
        cin>>p>>s;
        mxt=max((d-p)/s,mxt);
    }

    cout<<"Case #"<<c<<": "<<fixed<<setprecision(7)<<d/mxt<<endl;
    }
    return 0;
}
