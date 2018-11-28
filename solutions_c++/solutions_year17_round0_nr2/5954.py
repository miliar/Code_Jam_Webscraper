#include<bits/stdc++.h>

using namespace std;

int main(){
	
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	
	int t;cin>>t;
  for(int k=1;k<=t;k++){
  		long long int n;cin>>n;
  		
  		stringstream ss;
		ss << n;
		string s = ss.str();
		
  		for(int i=s.size()-1;i>=1;i--){
  			if(s[i]<s[i-1] & s[i-1]!=0){
  				s[i-1]--;
  				int y=i;
				  while(y!=s.size()){
  					s[y]='9';
  					y++;
				  }
			  }
		  }
		  
		  cout<<"Case #"<<k<<": ";
  		int flag = 0;
  		for(int j=0;j<s.size();j++){
  			 	if(flag==1){
			  		cout<<s[j];
			  	}
			  
			  if(flag==0 && s[j]!='0'){
  				flag=1;
  				cout<<s[j];
			  }
			 
		  }
  		
  		cout<<endl;
  		
	}
		  
	return 0;
}
