#include <iostream>
#include <cstring>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	int t;
	cin>>t;
	for (int k=1;k<=t;k++){
		string s;
		int n;
		cin>>s;
		cin>>n;
	//	s="---+-++-";n=3;
		int count=0;
	//	cout<<s.length();
		//if (s[0]=='-') cout<<"lalalala";
		for (int i=0,m=s.length()-n;i<=m;i++){
			if (s[i]=='-'){
				for (int j=i;j<i+n;j++) 
			 	if(s[j]=='-') s[j]='+';
			 	else if (s[j]=='+') s[j]='-';
				count++;
			} 
		}
		int check=1;
		for (int i=0,m=s.length();i<m;i++) if (s[i]=='-'){ 
		check=0; break;
		}
		cout<<"Case #"<<k<<": ";
		if (check==1) cout<<count<<endl;
		else if (check==0)cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
