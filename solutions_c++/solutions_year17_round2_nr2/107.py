#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

int n , arr[10] ;
string ans , s[10] ;
char col[] = {0 , 'R' , 'Y' , 'O' , 'B' , 'V' , 'G' };

int main(){
    freopen("B_large.in","r",stdin);
    freopen("B_large.out","w",stdout);
	int t ;
	scanf("%d",&t) ;
	for(int T = 1 ; T<=t;T++){
		scanf( "%d%d%d%d%d%d%d" , &n  , arr + 1 , arr +3 , arr+2 , arr+6 , arr+4 , arr+ 5) ;
		int chk = 0 ;
		ans.clear() ;
		for(int i=0;i<10;i++) s[i].clear() ;
		printf("Case #%d: ",T) ;
		for(int i=4;i>0;i>>=1){
			if(arr[i] < arr[7-i])  chk = 1 ;
			else if( (arr[i] == arr[7-i]) && ( arr[i] + arr[7-i] )!=n && (arr[i] > 0) ) chk = 1 ;
			else if( ( arr[i] == arr[7-i] ) && ( arr[i] > 0 ) ){
				chk = 2 ;
				for(int j=0;j<n;j++){
					if(j%2) ans.push_back(col[i]) ;
					else ans.push_back(col[7-i]) ;
				}
				break ;
			}
			else if(arr[i] > 0){
				for(int j=0;j<=2*arr[7-i];j++){
					if(j%2) s[i].push_back(col[7-i]) ;
					else s[i].push_back(col[i]) ;
				}
				arr[i] = arr[i] - arr[7-i] ;
			}
		}
		if(chk == 2){
//			printf("1n") ;
			cout << ans << endl ;
			continue ;
		}
		if(arr[4]>arr[2]+arr[1] || arr[2]>arr[4]+arr[1] || arr[1]>arr[2]+arr[4]) chk = 1 ;
		ii srt[] = {{arr[4],4} , {arr[2],2} , {arr[1],1}} ;
		int used = 0 ;
		sort(srt , srt+3) ;
		for(int i=0;i<s[srt[2].se].size();i++) ans.push_back(s[srt[2].se][i]); arr[srt[2].se]-- ;
		for(int i=0;i<s[srt[1].se].size();i++) ans.push_back(s[srt[1].se][i]); arr[srt[1].se]-- ;
		if(arr[srt[2].se] < arr[srt[1].se]+arr[srt[0].se] ){ for(int i=0;i<s[srt[0].se].size();i++) ans.push_back(s[srt[0].se][i]); arr[srt[0].se]-- ; used = 1 ;}
		while(arr[srt[2].se]){
			if( arr[srt[2].se] < arr[srt[1].se]+arr[srt[0].se] ){
				for(int i=2;i>=0;i--){
					ans.push_back(col[srt[i].se]) ;
					arr[srt[i].se]-- ;
				}
			}
			else if(arr[srt[1].se] > 0){
				for(int i=2;i>0;i--){
					ans.push_back(col[srt[i].se]) ;
					arr[srt[i].se]-- ;
				}
			}
			else if(used){
				ans.push_back(col[srt[2].se]) ;
				arr[srt[2].se]-- ;
				ans.push_back(col[srt[0].se]) ;
				arr[srt[0].se]-- ;
			}
			else {
				ans.push_back(col[srt[2].se]) ;
				arr[srt[2].se]-- ;
				for(int i=0;i<s[srt[0].se].size();i++) ans.push_back(s[srt[0].se][i]);
				arr[srt[0].se]-- ;
			}
		}
//		printf("2n") ;
		if(chk) printf("IMPOSSIBLE\n") ;
		else cout << ans << endl;
	}
	return 0;
}
