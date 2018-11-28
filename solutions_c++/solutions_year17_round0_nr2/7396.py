/*input
4
132
1000
7
111111111111111110
*/
#include<bits/stdc++.h>
 
using namespace std;
 
#define ll long long int
 
// string check(string a){
// 	if(a[0]<=a[1])
// 		return a;
// 	else{
// 		if(a == "10")
// 			return "09";
// 		a[1] = '9';
// 		int i = atoi(a.c_str());
// 		i -= 10;
// 		a = to_string(i);
// 		return a;
// 	}
// }
 
// vector<ll> v(20);
// void initiate(){
// 	v[0] = 1;
// 	for(int i = 1; i <= 18; ++i){
// 		v[i] = 10*v[i-1];
// 	}
// }
 
// bool poweroften(ll n){
// 	auto it = find (v.begin(), v.end(), n);
// 	if(it != v.end())
// 		return true;
// 	return false;
// }
 
bool lastcheck(ll n){
	string a = to_string(n);
	for(int i = 0; i < a.size()-1; ++i){
		if(a[i]>a[i+1])
			return false;
	}
	return true;
}
 
void solve(ll n, int q){
	// if(n < 10)
 //  		cout << "Case #" << q << ": " << n << endl;
 //  	else if(poweroften(n)){
 //  		cout << "Case #" << q << ": " << n-1 << endl;
 //  	}
 //  	else{
   		while(!lastcheck(n)){
   		int flag = 0;
		string a = to_string(n);
		for(int i = 0; i < a.size()-1; ++i){
			if(a[i] == '9' and flag){
				for(int j = i; j < a.size(); ++j){
					a[j] = '9';		
				}
				break;
			}
			if(a[i]>a[i+1]){
				a[i] = (((a[i] - '0') - 1) + '0');
				a[i+1] = '9';
				flag = 1;
			}
			// cout<< a<<" ";
		}
		ll ans = 0;
   		for(int i = 0; i < a.size(); ++i){
   			ans = 10*ans + (a[i] - '0');
   		}
   		n = ans;
   		}
		cout << "Case #" << q << ": " << n << endl;
   	// }
  	// if(n < 10)
  	// 	cout << "Case #" << q << ": " << n << endl;
  	// else if(poweroften(n)){
  	// 	cout << "Case #" << q << ": " << n-1 << endl;
  	// }
  	// else{
  	// 	while(!lastcheck(n)){
	  //		string a = to_string(n);
	  //		for(int i = a.size()-1; i >= 1; i--){
	  //			string f;
	  //			f.push_back(a[i-1]);	f.push_back(a[i]);
	  //			f = check(f);
	  //			a[i] = f[1];	a[i-1] = f[0];
	  //		}
	  //		ll ans = 0;
	  //		for(int i = 0; i < a.size(); ++i){
	  //			ans = 10*ans + (a[i] - '0');
	  //		}
	  //		n = ans;
  	// 	}
  	// 	cout << "Case #" << q << ": " << n <<endl;
  	// }
}

int main(){
	freopen("source.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
	int t;
	cin >> t;
	// initiate();
	for(int q = 1; q <= t; q++){
		ll n;
		cin >> n;
		solve(n, q);
	}
return 0;
}