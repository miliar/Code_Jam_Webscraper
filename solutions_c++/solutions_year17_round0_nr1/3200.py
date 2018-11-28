
#include <iostream>
#include <string>
using namespace std;

int no_cases;

int main(){
	cin>>no_cases;
	for (int caseID=1; caseID<=no_cases; caseID++){
		string s;
		int n;
		cin>>s>>n;

		int ans=0;
		//n>s.size() case
		if (n>s.size()){
			//all +
			int all_plus=true;
			for (int i=0; i<n; i++){
				if (s[i]=='-')
					all_plus=false;
			}
			if (all_plus)
				cout<<"Case #"<<caseID<<": "<<0<<endl;
			else
				cout<<"Case #"<<caseID<<": "<<"IMPOSSIBLE"<<endl;
			continue;
		}
		for (int i=0; i+n<=s.size(); i++){
			if (s[i]=='-'){
				for (int j=0; j<n; j++){
					if (s[i+j]=='-')
						s[i+j]='+';
					else
						s[i+j]='-';
				}
				ans++;
			}
		}
		bool flag=true;
		for (int i=0; i<n; i++){
			if (s[s.size()-1-i]=='-')
				flag=false;
		}
		if (flag){
			cout<<"Case #"<<caseID<<": "<<ans<<endl;
		}
		else
			cout<<"Case #"<<caseID<<": "<<"IMPOSSIBLE"<<endl;
	}
}