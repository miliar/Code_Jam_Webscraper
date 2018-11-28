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
bool isHappy(string s){ 
	forit(c,s){
		if ( c == '-') return false;
	}	
	return true;
}

int main(){
	int t,k;
	cin >> t;
	string s;
	forc(t1,t){
		int ans = 0;
		cin >> s >> k;
		forc(i, s.length()-k+1){
			if( s[i] == '-'){
				for(int j = i;j<i+k;j++){
					if( s[j] == '-') s[j]='+';
					else s[j] ='-';
				}
				ans++;
			}
		} 
		cout << "Case #" << (t1+1) << ": ";
		if ( isHappy(s)) { cout << ans << endl; }
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}