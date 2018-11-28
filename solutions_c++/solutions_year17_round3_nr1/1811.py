/*
    Har Har Mahadev
*/

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vi vector<int>
#define vll vector<long long>
#define vpii vector<pair<int,int> >
#define vpll vector<pair<long long,long long> >
#define pb(x) push_back(x)
#define mk(x,y) make_pair(x,y)
#define fir first
#define sec second
#define all(x) x.begin(),x.end()
#define frp(i,x,y) for(i=x;i<=y;i++)
#define frn(i,x,y) for(i=x;i>=y;i--)
#define mod 1000000007ll
#define FILE freopen("input.in", "rt", stdin),freopen("output.txt", "wt", stdout);
#define ld long double

template <class T>
T expo(T x,T n) { T result=1; while(n>0){ if(n%2==1) result=(result*x)%mod; x=(x*x)%mod; n=n/2; } return result; }

// ------------------------------------------- Potha Ends Here------------------------------------------------ //

long double dp[1001][1001];
int n,k;
vector<pair<long double,long double> > v(1001);
long double pi= 3.1415926535897932;

long double solve(int i,int c){
	if((i==n && c==k) || (c==k)){
		return 0.00000000000;
	}
	if(i==n){
		return -1.1e+16;
	}
	
	if(dp[i][c]!=-1)
	return dp[i][c];
	
	dp[i][c]=2.0000000*pi*v[i].fir*v[i].sec+solve(i+1,c+1);
	dp[i][c]=max(dp[i][c],solve(i+1,c));
	
	return dp[i][c];
}

int main(){
	FILE
	int t,u=0;
	cin>>t;
	while(t--){
		u++;
		int i,j,x,y,z;
		cin>>n>>k;
		
		for(i=0;i<n;i++){
			cin>>v[i].fir>>v[i].sec;
			v[i].fir+=0.000000000000001;
			v[i].sec+=0.000000000000001;
		}
		
		sort(v.begin(),v.begin()+n);
		reverse(v.begin(),v.begin()+n);
		
		for(i=0;i<=n;i++){
			for(j=0;j<=k;j++){
				dp[i][j]=-1;
			}
		}
		
		long double height=0,ans=0;
		for(i=0;i<n;i++){
			height=2*pi*v[i].fir*v[i].sec+solve(i+1,1);
			ans=max(ans,pi*v[i].fir*v[i].fir+height);
		}
		
		printf("Case #%d: %0.7Lf\n",u,ans);
	}
}
