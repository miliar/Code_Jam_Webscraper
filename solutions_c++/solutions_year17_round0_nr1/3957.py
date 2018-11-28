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
		int k;
		cin>>k;

		int count=0;
		int possible=1;
		for(int i=0; i<s.length();i++) {
			if(s[i]=='-' && (s.length()-i)>=k) {
				for(int j=0;j<k;j++) {
					if(s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-';
				}

				count++;
			}
			if(s[i]=='-') possible=0;
		}

		
		if(possible==0) cout<<"Case #"<<T-t<<": IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<T-t<<": "<<count<<endl;
	}

	return 0;
}