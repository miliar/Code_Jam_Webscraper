#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<bool> list;

int main(){
	string s;
	int k,n,count;
	int test;
	int total;
	cin>>test;
	total=test;
	while(test--){
		bool flag=false;
		count=0;
		cin>>s;
		cin>>k;
		n=s.length();
		for(int i=0;i<n;i++){
			if(s[i]=='+')
			list.push_back(true);
			else
			list.push_back(false);
		}
		for(int i=0;i<=n-k;i++){
			if(list[i]==false){
				count++;
				for(int j=i;j<i+k;j++){
					list[j]=list[j]?false:true;
				}
			}
			
		}
		cout <<"Case #"<<total-test<<": ";
		for(int i=n-k+1;i<n;i++){
			if(list[i]==false){
				cout<<"IMPOSSIBLE"<<endl;
				
				flag=true;
				break;
			}
			
		}
		if(!flag){
		
		/*	for(int i=0;i<n;i++){
				cout<<list[i]<<" ";
			}*/
			cout<<count<<endl;
		}
		list.clear();
	}
}
