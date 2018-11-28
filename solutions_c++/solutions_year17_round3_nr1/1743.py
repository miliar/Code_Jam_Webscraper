#include <bits/stdc++.h> 
using namespace std;
#define ll long long int
#define gearchange() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define MOD 1000000007LL
#define SIZE 1001
double pie= 3.1415926535897932;
double inf= -1e18;
pair< double,double > A[SIZE];
map<pair<int,int> ,double> dp;
double  solve(int x, int k){
	if(k==0){return 0; }
	if(k!=0 and x==-1){  return inf; }
	if(dp[make_pair(x,k)]){ return dp[make_pair(x,k)];}

    double a= 2.0*(pie)*(A[x].second)*(A[x].first)+ solve(x-1,k-1);
    double b= solve(x-1,k);
    return dp[make_pair(x,k)]= max(a,b);
}

int main(){
	gearchange();
   int t;
   cin>>t;
   int x=0;
  while(t--){
  	x++;
  	int n,k;
  	cin>>n>>k;
    for (int i = 0; i < n; ++i)
    {
       double a,b;
       cin>>a>>b;
       A[i]= make_pair(a,b);
    }
    sort(A,A+n);
    double maxx=0;
    for (int i = n-1; i>=0; i--)
    {
       double a= pie*(A[i].first)*(A[i].first)+ 2.0*pie*(A[i].first)*(A[i].second);
       if(i!=0){
           a+=solve(i-1,k-1);
           maxx= max(maxx,a);
       }
       else{
       	  if(k-1>0){ a= inf; }
       	  maxx= max(maxx, a);
       }
    }
      
      printf("Case #%d: %.7f\n",x,maxx);
      dp.clear();
   
  }
  return 0;
}