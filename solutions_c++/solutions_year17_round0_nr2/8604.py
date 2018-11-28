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
	int t,ca=0;
	cin>>t;
	while(t--){
		ca++;
		string s;
		cin>>s;
		if(s.length()==1){
			cout<<"Case #"<<ca<<": "<<s<<"\n";
			continue;
		}
		if(s.length()>=2 and s[0]=='1' and s[1]=='0'){
			cout<<"Case #"<<ca<<": ";
			for(int i=0;i<s.length()-1;i++){
				cout<<'9';
			}
			cout<<"\n";
			continue;
		}
		while(!is_sorted(s.begin(),s.end())){
			for(int i=1;i<s.length();i++){
				if(s[i]<s[i-1]){
					int x=s[i-1]-'0';
					x--;
					s[i-1]=(x+'0');
					for(int j=i;j<s.length();j++){
						s[j]='9';
					}
				}
			}
		}
		stringstream ss;
		ll ans=0;
		ss<<s;
		ss>>ans;
		ss.clear();
		cout<<"Case #"<<ca<<": ";
		cout<<ans<<"\n";
	}
	return 0;
}	