/*
*	Author: Suparshva Mehta 	Username: suparsh14
*	College: DA-IICT, India
*	GCJ Qualification Round
*	Q-A
*/

#include<bits/stdc++.h>

using namespace std;



int main(){		// O(|S|*K)

	int T;
	cin>>T;

	for(int ca=1;ca<=T;ca++)
	{
		cout<<"Case #"<<ca<<": ";

		//logic starts here

		string s;

		cin>>s;
		//reverse(s.begin(),s.end());
		int K;

		cin>>K;

		int ans=0,len=s.length();

		for(int i=0;i<len-K+1;i++){

			if(s[i]=='+')continue;
			ans++;
			for(int j=0;j<K;j++){
				if(s[i+j]=='+')s[i+j]='-';
				else s[i+j]='+';
			}
		}

		int plus=0;

		for(int i=0;i<len;i++){
			if(s[i]!='+')break;
			plus++;
		}

		if(plus!=len)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;

	}

	return 0;
}