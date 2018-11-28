#include<bits/stdc++.h>

using namespace std;

int main(){
 freopen("input.txt", "r", stdin);
             freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	int c=0;
	while(t--){
		c++;
		string s;
		int k;
		cin>>s;
		cin>>k;

		int len = s.size();

		//cout<<len<<" "<<k<<endl;

		int count = 0;
		for(int i=0;i<len-k+1;i++){
			if(s[i]=='-'){
				for(int j=0;j<k;j++){
					if(s[i+j]=='-'){
						s[i+j]='+';
					}else{
						s[i+j]='-';
					}
				}


			count++;
			}
		}

	// checking whether any '-' is still present or not 	

		int flag = 0;
		for(int i=0;i<len;i++){
			if(s[i]=='-'){
				flag=1;
				break;
			}
		}

     // if more '-' then impossible else count value

		if(flag){
			cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
		}else{
			cout<<"Case #"<<c<<": "<<count<<endl;
		}
	
	}	

}
