#include <bits/stdc++.h>


using namespace std;


int main()
{
	int T;
	cin>>T;
	int t=T;
	while(t--) {
		string s;
		cin>>s;

		for(int i=s.length()-1;i>0;i--) {
			if(s[i]>=s[i-1]) continue;
			else {
				s[i-1]--;
				for(int j=i; j<s.length();j++) {
					s[j]='9';
				}
			}
		}

		int j=0, count=0;

		while(s[j--]=='0') {
			count++;
		}

		s.erase(0,count);

	

		
		cout<<"Case #"<<T-t<<": "<<s<<endl;
	}

	return 0;
}