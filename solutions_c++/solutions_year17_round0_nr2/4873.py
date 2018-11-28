#include<iostream>
using namespace std;
#include<string>
#include<vector>
#include<algorithm>
int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		cout<<"Case #"<<t<<": ";
		string str;
		cin>>str;
			while(!is_sorted(str.begin(), str.end())) {
				int carry=0, diff;
				diff=str[str.size()-1]-'0'-1;
				carry=diff>=0?0:1;
				diff=diff>=0?diff:10+diff;
				str[str.size()-1]=diff+'0';
				for(int i=str.size()-2;i>=0;i--) {
					diff=str[i]-'0'-carry;
					carry=diff>=0?0:1;
					diff=diff>=0?diff:10+diff;
					str[i]=diff+'0';
				}
			}
		int i=0;
		while(str[i]=='0' && i<str.size())
			i++;
		if(i==str.size()) i=0;
		for(int j=i;j<str.size();j++) cout<<str[j];
		cout<<"\n";
	}
}
