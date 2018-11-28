#include<iostream>
using namespace std;
int main(){
	int T;
	cin>>T;
	string s;
	for(int k=1, n; k<=T; k++){
		cin>>s>>n;
		int len = s.size(), ans = 0;
		bool ok = true;
		for(int i=0; i<len-n+1; i++){
			if(s[i] == '-'){
				for(int j=0; j<n; j++){
					s[i+j] = s[i+j]=='-'?'+':'-';
				}
				ans++;
			}
		}
		for(int i=0; i<len; i++){
			if(s[i] == '-'){
				ok = !ok;
				break;
			}
		}
		cout<<"Case #"<<k<<": ";
		if(ok) cout<<ans<<endl;
		else cout<<"IMPOSSIBLE\n";
	}
}
