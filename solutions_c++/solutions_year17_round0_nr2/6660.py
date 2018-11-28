#include <iostream>
#include <string>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int c=1;c<=t;c++) {
		string a;
		cin>>a;
		char parent='0',current;
		int i;
		for(i=0;i<a.size();i++) {
			current=a[i];
			if(current>=parent) {
				parent=current;
			} else {
				while(current<parent) {
					i--;
					a.replace(i,1,1,parent-1);
					if(i==0)
						break;
					current=a[i];
					parent=a[i-1];		
				}
				break;
			}
		}
		string ans="";
		for(int j=0;j<=i;j++) {
			if(j==a.size())
				break;			
			if(a[j]!='0')
				ans.push_back(a[j]);
		}
		for(int j=i+1;j<a.size();j++)
			ans.push_back('9');
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}
