#include <bits/stdc++.h> 
using namespace std;
#define ll long long int
#define gearchange() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define MOD 1000000007LL

int main(){
  // gearchange();
   int t;
   cin>>t;
   int x=0;
   while(t--){
   	  x++;
   	  double n,d;
    	 cin>>d>>n;
   	     double maxx=0;
   	 for (int i = 0; i < n; ++i)
   	 {
   	 	double a,b;
   	 	cin>>a>>b;
   	 	//cout<<(d-a)/b<<endl;
   	 	maxx= max((d-a)/b,maxx);
   	 }
   	   double v= d/maxx;
   	   printf("Case #%d: %.8f\n",x,v);
   }
  return 0;
}