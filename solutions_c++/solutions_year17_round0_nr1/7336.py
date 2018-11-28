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
	int t2 = t;
	while(t--){
		string s;
		cin>>s;
		int k;
		cin>>k;
		int c=0;
		rep(i,s.size()){
			if(s[i]=='-'){
				if(i+k<=s.size()){
					for(int j=0;j<k;j++){
						if(s[i+j] == '+')
							s[i+j] = '-';
						else 
							s[i+j] = '+';
					}
					c++;
				}
			}
		}
		int x=0;
		rep(i,s.size()){
			if(s[i]=='-')
				x++;
		}
		if(x>0)
			cout<<"Case #"<<t2-t<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<t2-t<<": "<<c<<endl;
	}	
	return 0;
}