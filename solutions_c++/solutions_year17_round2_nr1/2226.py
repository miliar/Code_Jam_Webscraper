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

vector<pair<double,double> > arr;
int poss(double sp,double dist){
	for(int i=0;i<arr.size();i++){
		double t1=dist/sp;
		double t2=(dist-arr[i].first)/arr[i].second;
	//	cout<<"got "<<t1<<" "<<t2<<endl;
		if(t1<t2){
			return 0;
		}
	}
	return 1;
}
void solve(int test_case_number){

	 int dist,n;
	 cin>>dist>>n;
	 arr.clear();
	 for(int i=0;i<n;i++){
	 	double pos,speed;
	 	cin>>pos>>speed;
	 	arr.push_back(make_pair(pos,speed));
	 }
	 double ans=0;
	 sort(arr.begin(),arr.end());
	 double l=0,u=1000000000000000000.00;
	 for(int i=0;i<1000;i++){
	 	double mid=(l+u)/2.0;
	 	if(poss(mid,dist)){
	 		l=mid;
	 		ans=max(ans,mid);
		 }
		 else{
		 	u=mid;
		 }
	 }
	printf("Case #%d: %.7f\n",test_case_number,ans);
}

int main(){
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++){
//		cout<<"Case #"<<tt<<": ";
		solve(tt);
//		cout<<endl;
//		cerr<<"solved "<<tt<<endl;
	}
	return 0;
}
