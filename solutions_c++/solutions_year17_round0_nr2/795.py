#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string s="";

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	
	long long n;
	int caso;
	cin>>caso;
	
	for(int testcases=1;testcases<=caso;testcases++){
		cout<<"Case #"<<testcases<<": ";
		cin>>n;
		/*
		if(n<10){
			cout<<n<<endl;
			continue;
		}
		*/
		
		stringstream st;
		st<<n;
		s=st.str();
		int tam=s.size();
		
		string ans=string(tam-1,'9');
		
		for(int i=0;i+1<s.size();i++){
			if(s[i]>s[i+1]){
				while(i>0 && s[i]==s[i-1]){
					i--;
				}
				
				s[i]--;
				
				for(int j=i+1;j<s.size();j++)
					s[j]='9';
				break;	
			}
		}
		
		while(s[0]=='0'){
			s=s.substr(1);
		}
				
		cout<<s<<endl;
	}
	
	
	
	return 0;
}
