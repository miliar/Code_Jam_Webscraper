#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	ifstream fin("in.txt");
	fin>>t;
	ofstream fout("out.txt");
	
	int cnt=1;

	while(t--){
		string s;
		int k;
		fin>>s>>k;
		int cur=0;
		int i;
		int ans=0;
		while(1){
			while(s[cur]=='+'&& i<s.length())
				cur++;
			//	cout<<"s : "<<cur<<endl;
			if(cur+k>s.length())break;
			ans++;
			int flip_size=k;
			bool stop=true;
			int t=cur;
			for(int j=t;j<t+k;j++){
				if(s[j]=='-')s[j]='+';
				else if(s[j]=='+'){
					stop=false;
					s[j]='-';}
				if(stop)cur++;
			}
			
		//	cout<<"e :"<<cur<<endl;	
			
		}
		bool possible=true;
		for(int i=cur;i<s.length();i++){
			if(s[i]=='-'){
				possible=false;break;
			}}
			
		if(possible)
			fout<<"Case #"<<cnt<<": "<<ans<<endl;
		else fout<<"Case #"<<cnt<<": IMPOSSIBLE"<<endl;		
		cnt++;
		}
		
		
	return 0;
}

