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
	int t2=t;
	while(t--){
		string s;
		cin>>s;
		int last = 0;
		rep(i,s.size()-1){
			if(s[i]<s[i+1]){
				last = i + 1;
			} else if (s[i] == s[i+1]){

			} else {
				s[last] = s[last]-1;
				for(int j = last+1;j<s.size();j++){
					s[j] = '9';
				}
			}
		}
		int val=0;
		string ans;
		rep(i,s.size()){
			if(s[i]!='0'){
				val = i;
				break;
			}
		}
		for(int i=val;i<s.size();i++){
			ans +=s[i];
		}
		cout<<"Case #"<<t2-t<<": "<<ans<<endl;
	}	
	return 0;
}