#include <vector>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;

void main2(){
	string S;
	cin>>S;
	int m=0;
	int j=0; 
	for(int i=0;i<S.size();i++){
		int d=S[i]-'0';
			//cerr<<'['<<d<<']';
		if(d>m){
			m=d;
			j=i;
			//cerr<<m<<','<<j<<'.';
		}else if(d==m){
		}else{
			if(j==0 && m==1){
				for(j=0;j<S.size()-1;j++){
					cout<<'9';
				}
				return;
			}else{
				S[j]='0'+m-1;
				for(j++;j<S.size();j++){
					S[j]='9';
				}
				break;
			}
		}
	}
	cout<<S;
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
