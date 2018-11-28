#include<iostream>
#include<string>

using namespace std;

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	int z=t;
	while(t--){
		string s;
		int k;
		cin>>s>>k;
		int count = 0;
		for(int i=0;i<=s.length()-k;i++){
			if(s[i]=='-')
			{
					
			count++;
			for(int j=i;j<i+k;j++){
				if(s[j]=='-')
					s[j]='+';
				else s[j]='-';
			
			
			}
		//	cout<<i<<" : "<<s<<endl;
		}
		}

		int flag = 1;
		
//		cout<<s<<endl;

		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){
				flag = 0;
				break;

			}
		}

		if(flag==1){
		cout<<"Case #"<<z-t<<": "<<count<<endl;
		}
		else cout<<"Case #"<<z-t<<": "<<"IMPOSSIBLE"<<endl;
	}
}
