#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

pair<double , double> arr[1010] ;
int n ;
double d;

int main(){
    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);
	int t ;
	double a , b ;
	scanf("%d",&t);
	for(int T = 1 ; T<=t ; T++){
		scanf("%lf%d",&d,&n) ;
		double ans = 0 ;
		for(int i=0;i<n;i++){
			scanf("%lf%lf",&a,&b) ;
			ans = max( ans , (d - a) / b );
		}
		printf("Case #%d: %.7lf\n" ,T ,  d/ans) ;
	}
	return 0;
}
