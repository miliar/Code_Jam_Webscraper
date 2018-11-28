#include <bits/stdc++.h>
 
#define long long long int
using namespace std;
 
#define Max 100005+5
#define cons 1000000000+7
#define mp make_pair
#define pb push_back
#define x first
#define y second


int main()
{
    ios::sync_with_stdio(false);cin.tie(0);

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;cin>>t;
    int case_No=0;

    while(t--)
    {
    	case_No++;   	
    	cout<<"Case #"<<case_No<<": ";

      double d;cin>>d;
      int n;cin>>n;

      double ans = 0;

      for(int i=1;i<=n;i++)
      {
        double pos,speed;cin>>pos>>speed;
        double time1 = (d-pos)/speed;
        ans = max(ans,time1);
      }

      cout<<setprecision(9)<<fixed<<(d/ans)<<"\n";



    }

    	

}





