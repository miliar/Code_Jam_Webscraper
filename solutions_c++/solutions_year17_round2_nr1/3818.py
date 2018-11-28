#include <bits/stdc++.h>
using namespace std;
#define  ll long long int
#define loop(i,n) for(int i =0 ;i<n;i+=1)
#define loop2(i,n) for(int i = 1;i<=n;i+=1)


int main()
{
   ios_base::sync_with_stdio(false);
   cin.tie(0);
    freopen("/Users/ashish/Desktop/A-large.in.txt", "r", stdin);
    freopen("/Users/ashish/Desktop/A-large-practice.out.txt", "w", stdout);
    ll cases;
    cin>>cases;
    loop2(y1, cases)
    {
        cout<<"Case #"<<y1<<": ";
        ll dist,n;
        cin>>dist>>n;
        double ans = 0;
        loop(i,n)
        {
            ll cool,v;
            cin>>cool>>v;
            cool = dist-cool;
            ans = max(ans,(double)cool/v);
        }
        cout<<setprecision(8);
        printf("%.6lf\n",dist/ans);
        
    }
    

    
    return 0;
}
