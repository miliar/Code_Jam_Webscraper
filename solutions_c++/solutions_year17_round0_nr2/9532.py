#include<iostream>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out1234.txt", "w", stdout);
	int t,i,j,k,l;
	string s;
	cin>>t;
	for(k=1;k<=t;k++) {
		cin>>s;
		l=-1;
		for(i=0;i<s.length()-1;i++) {
			if(s[i]>s[i+1]) {
				l=(l==-1)?i:l;
				s[l]--;
				for(l=l+1;l<s.length();l++) {
					s[l] = '9';
				}
				break;
			}
			else if(s[i] == s[i+1]) {
				if(l==-1) l=i;
			}
			else
				l=-1;
		}
		cout<<"Case #"<<k<<": ";
		for(i=0;i<s.length();i++) {
			if(i==0 && s[i]=='0') {
				continue;
			}
			cout<<s[i];
		}
		cout<<"\n";
	}
}
