#include <iostream>
#include <string>

using namespace std;

bool ar[8101];

bool check(string i) {
	long long len=i.length()-1;
	char l=i[len],sl='a';
	bool ans=true;
	len--;
	while(len>=0) {
		sl=l;
		l=i[len];
		if(sl<l)
			ans=false;
		len--;
	}
	return ans;
}

string maken(string s) {
	long long len=s.length(),p1=0,p2=1;
	while(p2<len) {
		if(s[p1]>s[p2])
			break;
		p1++;
		p2++;
	}
	if(p2<len) {
		s[p1]--;
		while(p2<len)
			s[p2++]='9';
	}
	return s;
}

int main() {
	long long t,ans,n;
	string s;
	cin>>t;
	for(long long i=1;i<=t;i++) {
		cout<<"Case #"<<i<<": ";
		cin>>s;
		while(!check(s)) {
			s=maken(s);
		}
		for(long long j=0;j<s.length();j++) {
			if(s[j]!='0')
				cout<<s[j];
		}
		cout<<endl;
	}	
}