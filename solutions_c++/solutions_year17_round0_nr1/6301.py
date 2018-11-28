#include<iostream>
#include<string>

using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
	freopen("C.txt","w",stdout);
	int t;
	cin>>t;

	int p=1;
	while(p<=t){

		int k;
		string s;
		cin>>s;
		cin>>k;

		int count = 0;

		int n = s.length();

		for(int i=0;i<n;i++){
			if(s[i]=='-' && i+k<=n){
				for(int j=i;j<k+i;j++)
					if(s[j]=='+')
						s[j] = '-';
					else 
						s[j] = '+';
				count++;
			}
		}

		int y=0;
		for(int i=n-1;i>=0;i--)
			if(s[i]=='-'){
				y=1;
				break;
			}

		if(y==1)
			cout<<"Case #"<<p<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<p<<": "<<count<<endl;

		p++;
	}
}