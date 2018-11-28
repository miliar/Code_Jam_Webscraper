#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		string S; int K;
		cin>>S>>K;
		vector<bool> line(S.size());
		for(int i=0;i<S.size();i++) line[i] = S[i]=='+';
		int count=0;
		for(int i=0;i<=line.size()-K;i++){
			if(!line[i]){
				for(int j=0;j<K;j++){
					line[i+j]=!line[i+j];
				}
				count++;
			}
		}
		bool valid=true;
		for(int i=line.size()-K+1;i<line.size();i++){
			if(!line[i]){
				valid=false;
				break;
			}
		}
		cout<<"Case #"<<t<<": ";
		if(valid) cout<<count;
		else cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}