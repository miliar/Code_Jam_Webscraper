#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
double dp[1003][1003];
int memmory[1003][1003];
int n,k;
double so(int idx, int total);
vector<pair<double,double> > array;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,tt=0; cin>>t;
	while(t--){
		tt++;
		cin>>n>>k;
		array.clear();
		for(int i=0;i<n+2;i++) 
		for(int j=0;j<n+2;j++) {
			dp[i][j] = memmory[i][j] = -1;
		}
		for(int i=0;i<n;i++) {
		double x,y;
			cin>>x>>y;array.push_back(make_pair(x,y));}
		sort(array.begin(), array.end());reverse(array.begin(), array.end());
		printf("Case #%d: %0.9lf\n",tt,so(0,0));
	}
return 0;
}
double so(int idx,int total){
	if(total == k) return 0.0; if(idx >= n) return -1e18; if(memmory[idx][total] != -1)  return dp[idx][total];
	memmory[idx][total] = 1;
	if(total == 0) return dp[idx][total] = max(so(idx+1,total), 3.14159265358979323846*array[idx].first*array[idx].first + 2.0*3.14159265358979323846*array[idx].first*array[idx].second + so(idx+1,total+1));
	else return dp[idx][total] = max(so(idx+1,total), 2.0*3.14159265358979323846*array[idx].first*array[idx].second + so(idx+1,total+1));
}