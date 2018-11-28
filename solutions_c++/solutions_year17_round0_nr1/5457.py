#include<bits/stdc++.h>

using namespace std;

int main(){
	int t ,a,cnt;
	cin>>t;
	string s;
	for(int k=1;k<=t;k++){
		cnt=0;
		cin>>s>>a;
		
		for(int i=0;i<s.length()-a+1;i++){
		    if(s[i]=='-'){
		        cnt++;
		        for(int j=i;j<i+a;j++)
		            if(s[j]=='-')
		                s[j]='+';
		            else
		                s[j]='-';
		    }
		//cout<<s<<endl;
		    //cout<<cnt;
		}
		
		int c = count(s.begin(),s.end(),'-');
		if(c>0)
		cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<k<<": "<<cnt<<endl;
	}
	//cout << "Input ok";
	
	
	return 0;
}