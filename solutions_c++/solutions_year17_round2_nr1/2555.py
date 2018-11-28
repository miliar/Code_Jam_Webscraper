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

int main(){
	fin("A-large.in");
	fout("output.out");
	int t = 1, T;
	read(T);
	while(t <= T){
		int n;
		double d;
		cin >> d;
		cin >> n;
		double tm = 0;
		int i;
		rep(i, 0, n-1){
			double a, b;
			cin >> a >> b;
			tm = max( (d - a) / b, tm);
		}
		double ans = d / tm;
		cout << "Case #"<< t << ": " <<fixed << setprecision(6) << ans <<endl ;
		t++;
	}
	return 0;
}
