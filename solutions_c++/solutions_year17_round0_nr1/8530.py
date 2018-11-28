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
	int t,ca=0;;
	cin>>t;
	while(t--){
		ca++;
		bool flag=false;
		string s;
		cin>>s;
		int k;
		cin>>k;
		int count=0;
		for(int i=0;i<=s.length()-k;i++){
			if(s[i]=='-'){
				count++;			//COUNT FLIPS 
				for(int j=i;j<i+k;j++){
					//FLIP ME
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}
		for(int i=0; i< s.length(); i++){
			if(s[i]=='-'){
				cout<<"Case #"<<ca<<": "<<"IMPOSSIBLE\n";
				flag=true;
				break;
			}
		}
		if(!flag){
			cout<<"Case #"<<ca<<": "<<count<<"\n";
		}
	}
	return 0;
}