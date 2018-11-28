#include <bits/stdc++.h>
#define F first
#define S second.first
#define T second.second
#define mp make_pair
#define op(a) "Case #"<<a<<": "
#define ll long long
#define PI 3.14159265358979323846264338327950288419
using namespace std;
void output(int test_id,double x){
   cout<<setprecision(9)<<fixed<<"Case #"<<test_id<<": "<<x<<endl;
}
bool com (pair<ll,ll> a,pair<ll,ll> b){
	if(a.first!=b.first)
		return a.first>b.first;
	return a.second<b.second;
}
bool com2(pair<ll,ll> a,pair<ll,ll> b){
	return a.first*a.second>b.first*b.second;
}
int main(int argc, char const *argv[]){
freopen("A-large.in", "r", stdin); 
 freopen("A-small-attempt1.out", "w", stdout); 
 int No_testCase; cin>>No_testCase;  
 for(int test_id=1;test_id<=No_testCase;test_id++){    
       ll n,k; 
       cin>>n>>k;
       pair<ll,ll> v[n];
       ll r=-1,h=-1,ind=-1;
       for(int i=0;i<n;i++){
         cin>>v[i].first>>v[i].second;
        /*if(r<v[i].first*v[i].first + 2*v[i].first*v[i].second){
         	r=v[i].first*v[i].first + 2*v[i].first*v[i].second;
         	ind=i;
         }*/
       }
       long double cur = 0,ans  = 0;
       for(int i = 0; i <n-k+1; i++){
       		sort(v,v+n,com);
       		sort(v+i+1,v+n,com2);
       		cur = v[i].first*v[i].first +2*v[i].first*v[i].second;
       		for(int index = 0; index < k-1; index++){
       			cur += 2*v[i+index+1].first*v[i+index+1].second;
       		}
       		if(cur >ans ) ans = cur;
       }
      
      ans= 1.0*(ans)*PI;
       output(test_id ,ans); 
    } 
    
	return 0;
}