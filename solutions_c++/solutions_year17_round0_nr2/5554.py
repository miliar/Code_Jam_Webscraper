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
		//string s = to_string(t);
		//cout<<t<<' ';
		bool f=1;
		int l=s.length();
		cout<<"Case #"<<t<<": ";
		for(int i=1;i<l;i++){
			if(s[i]<s[i-1]){
				int j=i-1;
				while(s[j]==s[j-1]) j--;
				i=j+1;
				char c=s[i-1]-1;
				for(int j=0;j<i-1;j++) cout<<s[j];
				//cout<<' ';
				if(c!='0') cout<<c;
				for(int j=0;j<l-i;j++) cout<<'9';
				f=0;
				break;
			}
		}
		if(f) for(int i=0;i<l;i++) cout<<s[i];
		cout<<'\n';
	}
	return 0;
}
