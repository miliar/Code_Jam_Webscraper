#include <bits/stdc++.h>

#define db 	cout << "*****" << endl;
#define Max 100009
#define pb push_back
#define pp pop_back
#define ff first
#define ss second
#define mk make_pair
#define MOD 1000000007

using namespace std;

double n;
int k;

int main(){
	
	
	int t=0;
	
	
	freopen("3.in" , "r" , stdin);
	freopen("3.out" , "w" , stdout);
	
	cin >> t;
	for( int i=1;i<=t;i++){
		
		cin >> n >> k;
		
		setprecision(6);
		double h=0.0;
		double a,b;
		while(k--){
			
			cin >> a >> b;
			double H = ( n - a ) / b;
			h = max( H , h );
			
		}
		cout << "Case #" << i << ": " << fixed << n / h << endl;
		
	}
	return 0;
}
