#include<iostream>
#include<climits>
#include<cstring>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int m=1;m<=t;m++)
	{
		string s;
		int k;
		cin>>s;
		cin>>k;
		int count=0;
		int size = s.size();
		for(int i=0;i<=size-k;i++){
			if(s[i]=='-'){
				count++;
				for(int j=i;j<(i+k);j++){
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
			}
		}
		int flag=1;
		for(int i=size-k;i<size;i++){
			if(s[i]=='-'){
				flag=0;
			}
		}

		if(flag==0){
			cout<< "Case #" <<m<<": IMPOSSIBLE"<<"\n"; 
		}
		else{
			cout<<"Case #" <<m<<": "<<count<<"\n";
		}

	}
}