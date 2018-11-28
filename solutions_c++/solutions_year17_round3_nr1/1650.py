#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;
bool cmp(const pair<int,int> &a, const pair<int,int> &b) {
       return (a.first > b.first);
}
int main() {
	ifstream fin;
	ofstream fout;
	vector < pair<long long int, long long int> > v;
	vector <long long int> r, h;
	fin.open("sample.txt");
	fout.open("answers.txt");
	long long int t, i, T, n, k, x, y, j;
	fin>>t;
	for(T=1;T<=t;T++) {
		fout<<"Case #"<<T<<": ";
		fin>>n>>k;
		long long unsigned int dp[n+1][k+1];
		for(i=0;i<n;i++) {
			fin>>x>>y;
			v.push_back(make_pair(x,y));
		}
		sort(v.begin(), v.end(), cmp);
		for(i=0;i<n;i++) {
			r.push_back(v[i].first);
			h.push_back(v[i].second);
		}
		for(i=0;i<=n;i++)
			for(j=0;j<=k;j++)
				dp[i][j]=0;

		for(i=1;i<=n;i++) {
			dp[i][1]=((r[i-1]*r[i-1])+(2*h[i-1]*r[i-1]) > dp[i-1][1] ? (r[i-1]*r[i-1])+(2*h[i-1]*r[i-1]) : dp[i-1][1]);
			cout<<(r[i-1]*r[i-1])<<" ";
		}
		
		for(i=2;i<=n;i++) {
			for(j=2;j<=i&&j<=k;j++) {
				if(j==3)
					cout<<dp[i][j]<<" "<<dp[i-1][j-1]+(2*h[i-1]*r[i-1])<<endl;
				dp[i][j]= (dp[i-1][j] > dp[i-1][j-1]+(2*h[i-1]*r[i-1]) ? dp[i-1][j] : dp[i-1][j-1]+(2*h[i-1]*r[i-1]));
			}
		}
		
		fout<<fixed<<setprecision(10)<<((double)(dp[n][k])*3.141592653589793238462643383279)<<endl;
		
		for(i=0;i<=n;i++) {
			for(j=0;j<=k;j++)
				cout<<dp[i][j]<<"     ";
			cout<<endl;
		}
		r.clear();
		v.clear();
		h.clear();
	}
	return 0;
}