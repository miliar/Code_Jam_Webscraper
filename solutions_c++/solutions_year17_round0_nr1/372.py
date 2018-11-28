#include <vector>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;

void main2(){
	string S;
	int K;
	cin>>S>>K;
	int res=0;
	for(int i=0;i<S.size();i++){
		if(S[i]=='-'){
			if(i+K-1<S.size()){
				for(int j=i;j<i+K;j++){
					if(S[j]=='-') S[j]='+';
					else S[j]='-';
				}
				res++;
			}else{
				cout<<"IMPOSSIBLE";
				return;
			}
		}
	}
	cout<<res;
}

int main(){
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		main2();
		cout<<endl;
	}
}
