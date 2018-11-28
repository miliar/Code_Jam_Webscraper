#include<bits/stdc++.h>
using namespace std;
#define double long double
typedef pair<double , double> dd;
ofstream fout("out.txt");
const int N=1e3+10;
const double PI = 3.1415926535897932384626433832795028;
double dp[N][N];
dd a[N];
double area(double r){
	return r*r*PI;
}
double solve(){
	int n , k;
	double ret=0 , sum = 0;
	multiset<int> st;
	cin >> n >> k;
	for(int i=0 ; i<n ; i++)
        for(int j=0 ; j<=k ; j++)
            dp[i][j] = 0;
	for(int i=0 ; i<n ; i++)
		cin >> a[i].first >> a[i].second;
	k --;
	sort(a , a+n);
	dp[0][1] = a[0].second * (a[0].first*2*PI);
	ret = max(ret , a[0].second * (a[0].first*2*PI) + area(a[0].first));
	for(int i=1 ; i<n ; i++){
		double ans=0;
		for(int j=1 ; j<=k ; j++){
			dp[i][j] = max(dp[i-1][j] , dp[i-1][j-1] + a[i].second * (a[i].first*2*PI));
			ans = max(ans , dp[i-1][j]);
		}
		ret = max(ret , ans + a[i].second * (a[i].first*2*PI) + area(a[i].first));
	}
	return ret;
}
int main(){
	int t;
	cin >> t;
	fout << fixed << setprecision(9);
	for(int i=1 ; i<=t ; i++){
		fout << "Case #" << i << ": " << solve() << "\n";
	}
}
