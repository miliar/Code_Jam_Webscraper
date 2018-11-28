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
    freopen("B-small-attempt1.in","rt",stdin);
    freopen("out.txt","wt",stdout);
    int t;
    cin>>t;
    for(int c=1; c<=t; c++)
    {
        int n,r, o, y, g, b, v;
        cin>>n>>r>>o>>y>>g>>b>>v;
        cout<<"Case #"<<c<<": ";
        if(r>y+b || y>r+b || b>r+y)
            cout<<"IMPOSSIBLE\n";
        else
        {
            int l=-1;
            while(n>0)
            {
                if(l!=0 && l!=1)
                {
                    if(r>y)
                    {
                        l=0; r--; n--;cout<<'R';
                    }
                    else
                    {
                        l=1; y--; n--;cout<<'Y';
                    }
                }else if(l!=1 && l!=2)
                {
                    if(b>y)
                    {
                        l=2; b--; n--;cout<<'B';
                    }
                    else
                    {
                        l=1; y--; n--;cout<<'Y';
                    }
                }else{
                    if(b>r)
                    {
                        l=2; b--; n--;cout<<'B';
                    }
                    else
                    {
                        l=0; r--; n--;cout<<'R';
                    }

                }

            }
            cout<<endl;
        }
    }
    return 0;
}
