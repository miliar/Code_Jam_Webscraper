#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int xx=0;xx<t;xx++){
		string tstcase;
		getline(std::cin,tstcase,' ');
		int k;
		cin>>k;
		int ctr=0;
		for(int i=0;i<=tstcase.size()-k;i++){
			if(tstcase[i]=='-'){
				for(int j=0;j<k;j++){
					if(tstcase[i+j]=='-')
						tstcase[i+j]='+';
					else
						tstcase[i+j]='-';
				}
				ctr++;
			}
		}
		if(tstcase.find('-')==string::npos){
			cout<<"Case #"<<xx+1<<": "<<ctr<<"\n";
		}
		else{
			cout<<"Case #"<<xx+1<<": IMPOSSIBLE\n";
		}
	}
	return 0;
}
