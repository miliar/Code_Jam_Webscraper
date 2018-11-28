#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
typedef pair<int, int>          pii;
typedef vector<int>             vi;
#define SYNC		ios_base::sync_with_stdio(0);cin.tie(0); 
ll MOD = 1000000007;
#define rep(i,b)   for (int i=0; i < b; i++)
#define fi           first
#define se           second
#define pb           push_back
#define mp           make_pair
#define dzx 		cerr<<"here";
#define deb(x)		cerr << #x << " here "<< x;
#define debn(x)		cerr << #x << " here " << x << "\n"; 
//START
int main()
{
	SYNC
	int t;
	cin>>t;
	int te = t;
	while(t--){
		int d,n;
		cin>>d>>n;
		ll a,b;
		double max = 0;
		rep(i,n) {
			cin>>a>>b;
			double temp = (double)(d-a)/b;
			if( temp > max){
				max = temp; 
			}
		}
		printf("Case #%d: %.6f\n",te-t,d/max);
		//cout<<"Case #"<<te-t<<": "<<d/max<<endl;
	}	
	return 0;
}