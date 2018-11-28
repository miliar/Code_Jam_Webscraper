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
	for( int k=1;k<=t;k++){
		
		cin >> n;
		
		int arr[7];
		
		for( int j=1;j<= 6;j++)
			cin >> arr[j];
			
		string s = "";
		int last = 0;
		int inti = 0;
		// RYB
		if( arr[1] >= arr[3] && arr[1] >= arr[5] ){
			last = inti = 1 ;
			s = s + 'R';
			arr[1]--;
		}
		else if( arr[3] >= arr[1] && arr[3] >= arr[5] ){
			last = inti = 3 ;
			s = s + 'Y';
			arr[3]--;
		}
		else if( arr[5] >= arr[1] && arr[5] >= arr[3] ){
			last = inti = 5 ;
			s = s + 'B';
			arr[5]--;
		}
		for( int i = 2 ;i<=n;i++){
			if( last == 1 ){
				if( arr[3] > arr[5] ){
					last = 3 ;
					s = s + 'Y';
					arr[3]--;
				}else if( arr[3] < arr[5] ){
					last = 5 ;
					s = s + 'B';
					arr[5]--;
				}else if( arr[3] == arr[5] ){
					if( 3 == inti ){
						last = 3 ;
						s = s + 'Y';
						arr[3]--;
					}else{
						last = 5 ;
						s = s + 'B';
						arr[5]--;
					}	
				}
			}
			else if( last == 3 ){
				if( arr[1] > arr[5] ){
					last = 1 ;
					s = s + 'R';
					arr[1]--;
				}else if( arr[1] < arr[5] ){
					last = 5 ;
					s = s + 'B';
					arr[5]--;
				}else if( arr[1] == arr[5] ){
					if( 1 == inti ){
						last = 1 ;
						s = s + 'R';
						arr[1]--;
					}else{
						last = 5 ;
						s = s + 'B';
						arr[5]--;
					}	
				}
			}
			else if( last == 5 ){
				if( arr[3] > arr[1] ){
					last = 3 ;
					s = s + 'Y';
					arr[3]--;
				}else if( arr[3] < arr[1] ){
					last = 1 ;
					s = s + 'R';
					arr[1]--;
				}else if( arr[3] == arr[1] ){
					if( 3 == inti ){
						last = 3 ;
						s = s + 'Y';
						arr[3]--;
					}else{
						last = 1 ;
						s = s + 'R';
						arr[1]--;
					}	
				}
			}
		}
		if( arr[1] == 0 && arr[3] == 0 && arr[5] == 0 && s[0] != s[n-1] )
			cout << "Case #" << k << ": " << s << endl;			
		else
			cout << "Case #" << k << ": " << "IMPOSSIBLE" << endl;			
	}
	return 0;
}
