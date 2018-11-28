#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	ll t;
	cin>>t;
	ll him=1;
	A:
	while(t--){
		string s;
		ll k;
		cin>>s>>k;
		deque<int> dq;
		int j=-1;
		ll answer=0;
		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){
				j=i;
				break;
			}
		}
		if(j==-1){
			cout<<"Case #"<<him<<": "<<answer<<endl;
			him++;
			continue;
		}
	//	cout<<j<<endl;
		for(int i=j;i<k+j && i<s.length();i++){
			if(s[i]=='+'){
				dq.push_back(i);
				s[i]='-';
			}
			else if(s[i]=='-'){
				dq.push_back(i);
				s[i]='+';
			}
		}
		if(dq.size()==k)	answer++;
		else{
			cout<<"Case #"<<him<<": "<<"IMPOSSIBLE"<<endl;
			him++;
			goto A;
		}
//		cout<<s<<endl;
		for(int i=k+j;i<s.length();i++){
			while(!dq.empty() && s[dq.front()]=='+')	dq.pop_front();
			if(dq.size()==0){
				for(;i<s.length();i++){
					if(s[i]=='-')	break;
				}
				if(i==s.length())	break;
			}
			else{
				int n=dq.size();
				int hmm=0;
				while(hmm<n && dq.empty()==false){
					hmm++;
					int val=dq.front();
					dq.pop_front();
					if(s[val]=='-')	s[val]='+';
					else if(s[val]=='+')	s[val]='-';
					dq.push_back(val);
				}
			}
			bool flag1=true;
			while(dq.size()<k && i<s.length()){
				flag1=false;
				if(s[i]=='+'){
					dq.push_back(i);
					s[i]='-';
				}
				else if(s[i]=='-'){
					dq.push_back(i);
					s[i]='+';
				}
				i++;
			}
			if(dq.size()==k){
				answer++;
				i--;
			}
			else{
				cout<<"Case #"<<him<<": "<<"IMPOSSIBLE"<<endl;
				him++;
				goto A;		
			}
//			cout<<s<<endl;
		}
		bool flag=true;
		for(int i=0;i<s.length();i++)	if(s[i]=='-')	flag=false;
		if(flag)	cout<<"Case #"<<him<<": "<<answer<<endl;
		else	cout<<"Case #"<<him<<": "<<"IMPOSSIBLE"<<endl;
		him++;
	}
}