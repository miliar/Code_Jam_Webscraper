#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

int n , mod , arr[110] ;

int main(){
    freopen("A_small.in","r",stdin);
    freopen("A_small.out","w",stdout);
	int t , a;
	scanf("%d",&t) ;
	for(int T = 1; T<=t;T++){
		scanf("%d%d",&n,&mod);
		memset(arr, 0 ,sizeof arr) ;
		for(int i=0;i<n;i++) {
			scanf("%d",&a) ;
			arr[a%mod]++ ;
		}
		int res = 0   ;
		if(mod == 2) res += ( arr[0] + (arr[1]+1)/2 ) ;
		else if(mod == 3){
			res+=arr[0] ;
			int tmp = min(arr[1] , arr[2]) ;
			res+=tmp;
			arr[1] -= tmp ;
			arr[2] -= tmp ;
			res+=(arr[1] +2)/3 ;
			res+=(arr[2] + 2) /3 ;
		}
		else{
			res+=arr[0] ;
			res+=(arr[2]/2) ;
			arr[2] -= 2*(arr[2]/2) ;
			int tmp = min(arr[1],arr[3]) ;
			res+=tmp ;
			arr[1] -= tmp ; arr[3] -= tmp ;
			if(arr[2] > 0){
				if(arr[1] >= 2) res++ , arr[1]-=2 ;
				else if(arr[3] >= 2) res++ , arr[3]-=2 ;
			}
			res+=( (arr[3] + 3)/4 + ( arr[1] + 3 )/4 ) ;
		}
		printf("Case #%d: %d\n", T,res) ;
	}
	return 0;
}
