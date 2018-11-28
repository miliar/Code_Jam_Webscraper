#include<iostream>
#include <string>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int nn;
	cin>>nn;
	int ii=0;
	while(ii<nn){
		string str;
		int fap;
		int ctr=0;
		cin>>str>>fap;
		for(int i=str.size()-1;i>=fap-1;i--){
			if(str[i]=='-'){
				for(int j=0;j<fap;j++)str[i-j]=((str[i-j]=='-')?'+':'-');
				ctr++;
			}
			else continue;
		}
		for(int i=0;i<fap;i++)
			if(str[i]=='-'){
				ctr=199782200;
			}
		cout<<"Case #"<<ii+1<<": ";
		if(ctr==199782200)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ctr<<endl;
		ii++;
	}
}

