//--------------**************---------------------
/* 
 #        "    ""#    ""#                      #        
 #   m  mmm      #      #     mmm    mmm    mmm#   mmm  
 # m"     #      #      #    #"  "  #" "#  #" "#  #"  # 
 #"#      #      #      #    #      #   #  #   #  #"""" 
 #  "m  mm#mm    "mm    "mm  "#mm"  "#m#"  "#m##  "#mm"  */


#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef pair<int,int> pii;
typedef long long ll;
typedef double ld;
typedef vector<int> vi;
#define fi first
#define se second
#define fe first
#define SZ 666666
#define si(n) scanf("%d",&n);
#define sl(n) scanf("%ld",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%ld\n",n);
#define pf(n) printf("%f\n",n);
#define FILL(a,b) memset(a,0,sizeof(b));
#define rep(i,n) for(int i=0;i<n;i++)
#define reps(i,a,b) for(int i=1;i<=b;i++)
const int INF=1e9+5;
const int MOD=1000000007;

//--------------**************---------------------


int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
	   double d,n;
	   cin>>d>>n;
	   double maxi=-1.0;
	   for(int i=0;i<n;i++)
	   {
         double h,s;
         cin>>h>>s;
         double dis=d-h;
        // cout<<dis<<endl;
         double tim=(double)((double)dis/(double)s);
        // cout<<tim<<endl;
         if(tim>maxi)maxi=tim;
	   }
	   //cout<<maxi<<endl;
	   double ans=(double)((double)d/(double)maxi);
	   cout<<fixed<<setprecision(6)<<"Case #"<<j<<": "<<ans<<endl;
	}
}
