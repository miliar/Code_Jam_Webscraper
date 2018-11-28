#include <bits/stdc++.h> 
#define forc(i,j) for(int i=0;i<j;i++)
#define forit(a,b) for(auto a: b)
#define all(a) a.begin(), a.end()
#define fast() ios_base::sync_with_stdio(0); cin.tie(0)
#define printDS(a) forit(itt,a) cout << itt << " "; cout << endl;
// g++ -std=c++11 main.cpp -o main && main.exe < input.txt > output.txt && del main.exe
using namespace std;  
typedef long long ll;
typedef vector<ll> vi;

bool checa( ll l ){ 
	string s;
	stringstream ss;
	ss << l;
	ss >> s; 
	if ( s.length() == 1 ) return true;
	for ( int i=1;i < s.length();i++){
		if ( s[i] < s[i-1]) return false;
	}
	return true;
}

int main(){
	int t;
	ll l;
	cin >> t;
	forc(t1,t){
		cin >> l;
		while( !checa(l) ){
			l--;
		}
		cout << "Case #" << (t1+1) << ": " << l << endl;
	}
	return 0;	
} 