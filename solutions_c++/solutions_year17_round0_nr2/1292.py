#include <iostream>
#include <string>
using namespace std;
 
int main() {
	int t;
	cin>>t;
	for(int T = 1; T<=t; T++){
		string s;
		cin>>s;
		int n = s.size();
		
		//if number is less than 111111... make it 99999...
		string cmp="";
		for(int i = 0; i<n; i++)    cmp+="1";
		if(s<cmp){
		    s="";
		    for(int i = 1; i<n; i++)    s+="9";
		    n--;
		}
		
		
		for(int i = 1; i<n; i++){
			if(s[i]>=s[i-1])	continue;
			else{
			    int j = i-2;
			    while(s[j]==s[i-1] && j>=0){
			        j--;
			    }
				s[j+1]=s[i-1]-1;
				for(int k = j+2; k<n; k++)  s[k]='9';
				break;
			}
		}
		cout<<"Case #"<<T<<": "<<s<<endl;
	}
	return 0;
}