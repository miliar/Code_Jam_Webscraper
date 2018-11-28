/*
********************************
**      Name:Dev Bishnoi      **
**      NIT, Kurukshetra      **
**           INDIA            **
********************************
*/

#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define pie 3.14159265358979323 
#define ll long long 
#define rep(i,a,b) for(i=a ; i<=b ; i++)
#define init(a , val ) memset(a , val , sizeof(a))// val can be possible only 0,1.
#define vi vector< int > 
#define vpii vector< pair< int , int> >
#define pii pair<int , int >
#define pi_ii pair< int , pii >
#define pii_i pair< pii, int >
#define piiii pair< pii, pii >
#define pb push_back
#define mp make_pair 
#define read(x) scanf("%d" , &x)
#define read2(x,y) scanf("%d%d",&x,&y)
#define read3(x,y,z) scanf("%d%d%d", &x, &y , &z)
#define reads(s) scanf("%s",s)
#define print(x) printf("%d\n",x)
#define print2(x,y) printf("%d %d\n",x,y)
#define fin(fname) freopen(fname,"r", stdin)
#define fout(fname) freopen(fname, "w", stdout);
double dp[1001][1001];
struct node {
	int r;
	int h;
};
bool compare(struct node a, struct node b){
	if(a.r == b.r)
		return a.h > b.h;
	return a.r > b.r;
}
double solve(int idx, int count, int n, int k, struct node arr[]){
	if(dp[idx][count] != -1)
		return dp[idx][count];
	if(count == k){
		return 0;
	}
	if(idx >= n ){
		return (-1000000000000000000);
	}
	double ans = 2 * pie * arr[idx].r * arr[idx].h + solve(idx + 1, count + 1, n, k, arr);
	ans = max(ans, solve(idx + 1, count, n, k, arr));
	dp[idx][count] = ans;
	return ans;
}
int main(){
	fin("A-large.in");
	fout("output.out");
	int t = 1, T;
	read(T);
	while(t <= T){
		int n, k, i, j;
		read2(n, k);
		struct node arr[n+1];
		rep(i, 0, n-1){
			read2(arr[i].r, arr[i].h);
		}
		rep(i, 0, 1000){
			rep(j, 0, 1000){
				dp[i][j] = -1;
			}
		}
		double ans = 0;
		sort(arr, arr + n, compare);
		rep(i, 0, n-1){
			ans = max(ans, pie * arr[i].r * arr[i].r + 2 * pie * arr[i].r * arr[i].h  + solve(i + 1, 1, n, k, arr));
		}
		cout << "Case #"<< t << ": " << fixed << setprecision(9) << ans << endl;
		t++;
	}
	return 0;
}
