/*
 ____    _____      _      _               _____ 
/ ___|  | ____|    / \    | |             |___  |
\___ \  |  _|     / _ \   | |      _____     / / 
 ___) | | |___   / ___ \  | |___  |_____|   / /  
|____/  |_____| /_/   \_\ |_____|          /_/   
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define modulo(a, b) (a%b<0 ? a%b+b : a%b)

int main(){
	int t,c=1;
	cin>>t;
	while(t--){
		double maxt=0;
 		double d,n;
 		cin>>d>>n;
 		for(int i=0;i<n;i++){
 			double hd,hs;
 			cin>>hd>>hs;
 			maxt=max(maxt,(d-hd)/hs);
 		}
 		cout<<"Case #"<<c<<": ";
 		cout<<setprecision(10)<<fixed<<d/maxt<<"\n";
 		c++;
	}
	return 0;
}