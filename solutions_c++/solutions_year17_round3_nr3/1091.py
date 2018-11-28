#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
using namespace std;
#define ull unsigned long long
#define lli long long
#define mod 1000000007
double arr[50];
void solve(int test_case_number){
	 int n,k;
	 cin>>n>>k;
	 double u;
	 cin>>u;
	 double ans=1.0;
	 for(int i=0;i<n;i++){
	 	cin>>arr[i];
	 	ans*=arr[i];
	 }
	 sort(arr,arr+n);
	 for(int i=0;i<n;i++){
	 	double tot=0;
	 	for(int j=0;j<=i;j++){
	 		tot+=arr[j];
		 }
		 tot+=u;
		 if(tot>(i+1)) tot=i+1;
		 double tans=1.0;
		 int pos=1;
		 for(int j=0;j<n;j++){
		 	if(j<=i){
		 		if(tot/(i+1)<arr[j]){
		 			pos=0;
				 }
		 		tans*=(tot/(i+1));
			 }
			 else{
			 	tans*=arr[j];
			 }
		 }
		 if(pos && tans>ans){
		 	ans=tans;
		 }
	 }
	 printf("%.8f\n",ans);
}

int main(){
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++){
		cout<<"Case #"<<tt<<": ";
		solve(tt);
//		cerr<<"solved "<<tt<<endl;
	}
	return 0;
}
