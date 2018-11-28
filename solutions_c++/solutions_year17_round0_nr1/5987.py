#include<bits/stdc++.h>

using namespace std;

int main(){
	
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	
	int t;cin>>t;
  for(int j=1;j<=t;j++){
  		string str;cin>>str;
  		int d;cin>>d;
  		
  		int count = 0;int flag = 0;
  		for(int i=0;i<str.size();i++){
  			if(str[i]=='-'){
  				int left = str.size() - i;
  				if(left<d){
  					cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
  					flag = 1;
  					break;
				  }
				  for(int k=i;k<i+d;k++){
				  	if(str[k]=='-'){
				  		str[k]='+';
					  }else{
					  	str[k] = '-';
					  }
				  }
				  count++;
			  }
		  }
		  if(flag==0){
		  	cout<<"Case #"<<j<<": "<<count<<endl;	
		  }
	}
		  
	return 0;
}
