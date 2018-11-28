#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
using namespace std;
int main(){
	int T,left,right;
	ifstream input;
	input.open("q2l.in");
	input>>T;
	for(int t=1;t<=T;t++){
		string s,ans="";
		input>>s;
		int l = s.length();
		int current,start=0;
		int startvalue = s[0]-'0';
		int prev = startvalue;
		ans+=s[0];
		for(int i=1;i<l;i++){
			current = s[i]-'0';
			if(current<prev){
				ans[start]=(startvalue-1)+'0';
				if(ans[start]!='0')
				ans.erase(ans.begin()+start+1,ans.begin()+i);
				else
				ans.erase(ans.begin()+start,ans.begin()+i);
				for(int j=start+1;j<l;j++){
					ans+='9';
				}		
				break;
			}
			else if(current > prev){
				ans+=s[i];
				start = i;
				startvalue = current;
				prev = current;
			}
			else{
				ans+=s[i];
				prev = current;	
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	input.close();	
}
