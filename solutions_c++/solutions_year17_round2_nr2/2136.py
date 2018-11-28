#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define x first
#define y second
void solve (int x){
	ll n,r,o,y,g,b,v;
	cin >> n >> r >> o >> y >> g >> b >> v;
	if( r > n/2 || y > n/2 || b > n/2){
		cout <<"Case #"<<x<<":  "<<"IMPOSSIBLE";
		return ;
	}
	char ans [1005];
	int i= 1;
	while(r!=0){
		if ( i%2==1){
			ans [i]='R';
			r--;
		}
		else{
			if(y>b){
				ans[i] ='Y'; 
				y--;
			}
			else{
				ans [i]='B';
				b--;
			}
		}
		i ++;
	}
	if ( y == 0 || b == 0){
		if(y==0){
			ans [i] ='B';
		}
		else{
			ans [i] = 'Y';
		}
	}
	else{
	
	while(i<=n){
		if (b>y){
		
		if (i%2==0){
			ans [i] ='B';
		}
		else{
			ans [i] ='Y';
		}
		i ++;
	}
	else{
		if (i%2==1){
			ans [i] ='B';
		}
		else{
			ans [i] ='Y';
		}
		i ++;
	}
	}
	}
	cout <<"Case #"<<x<<":  ";
	for ( i = 1 ; i <= n ; i ++){
		cout << ans[i] ;
	}
}
int main()
{
	//ios::sync_with_stdio(false);
	//cin.tie(0);
	//fflush(stdout);
	assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
  int t,x=0;
  cin >> t;
  while ( t-- ){
  	x++ ;
  	solve(x);
  	cout << '\n';
  }
	return 0;
}
