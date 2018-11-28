#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	string s, ans;
	for(int tc = 1; tc<=t; tc++){
		cin>>s;
		int n = s.length(), j = -1;
		for(int i = 1; i<n; i++){
			if(s[i]<s[i-1]){
				j = i;
				break;
			}
		}
		if(j!=-1){
			for(int i = n-1; i>=j && i>=1; i--){
				s[i] = '9';
			}
			int k = j-1;
			s[k] = s[k]-1;
			while(k>=1 && s[k]<s[k-1]){
				s[k] = '9';
				s[k-1] = s[k-1]-1;
				k--;
			}
		}
		if(s[0]=='0')
			s = s.substr(1, n-1);
		cout<<"Case #"<<tc<<": "<<s<<endl;
	}
	return 0;
}
