#include<iostream>

using namespace std;

int main(){
	int T;
	cin>>T;
	char *N = new char[1024];
	int i,j,k;
	int a;
	char tmp;
	for(i=0;i<T;i++){
		tmp = '0';
		a = 0;
		cin>>N;
		for(j=0;N[j]!='\0';j++){
			if(N[j]>tmp){
				a = j;
				tmp = N[j];
			}
			else {
				if(N[j]<tmp) break;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(N[j]=='\0'){
			for(k=0;k<j;k++) cout<<N[k];
			cout<<endl;
		}
		else {
			if(a>0){
				for(k=0;k<a;k++) cout<<N[k];
				cout<<N[a]-'1';
				for(k=a+1;N[k]!='\0';k++) cout<<'9';
				cout<<endl;
			}
			else {
				if(N[0]=='1'){
					for(k=1;N[k]!='\0';k++) cout<<'9';
					cout<<endl;
				}
				else {
					cout<<N[0]-'1';
					for(k=1;N[k]!='\0';k++) cout<<'9';
					cout<<endl;
				}
			}
		}
	}

	return 0;
}
