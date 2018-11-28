#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(void){
	freopen("small_input.txt", "r", stdin);
	freopen("small_output.txt", "w", stdout);
	int T; cin>>T;
	for(int t=1;t<=T;t++){
		string s; cin>>s;
		cout<<"Case #"<<t<<": ";
		int k; cin>>k;
		int c=0;
		int l=s.length();
		for(int i=0;i<l-k+1;i++){
			if(s[i]=='-'){
				//cout<<s<<' ';
				c++;
				s[i]='+';
				for(int j=1;j<k;j++)
				if(s[i+j]=='-') s[i+j]='+'; else s[i+j]='-';
				//cout<<i<<' '<<s<<' '<<c;
				//cout<<'\n';
			}
		}
		bool f=0;
		for(int i=l-k;i<l;i++){
			if(s[i]=='-'){
				f=1;
				break;
			}
		}
		if(f) cout<<"IMPOSSIBLE";
		else cout<<c;
		cout<<'\n';
	}
	return 0;
}
