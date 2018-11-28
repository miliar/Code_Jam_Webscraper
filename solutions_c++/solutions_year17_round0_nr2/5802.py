#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;


int main(){
	int t;
	char num[30];
	char aux[30];
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>num;
		if(strlen(num)==1){
			cout<<"Case #"<<i+1<<": "<<num<<endl;
		}else{
			for(int jj=0;jj<strlen(num);jj++){
				for(int k=0;k<strlen(num)-1;k++){
					if(num[k]>num[k+1]){
						num[k]--;
						for(int j=k+1;j<strlen(num);j++){
							num[j]='9';
						}
					}
				}
				if(!strcmp(aux,num))break;
				strncpy(aux,num,30);
				//printf("%s\n",aux);
			}

			cout<<"Case #"<<i+1<<": ";
			if(num[0]=='0'){
				for(int ll=1;ll<strlen(num);ll++){
					cout<<num[ll];
				}
			}else{
				cout<<num;
			}
			cout<<endl;
		}
	}
	return 0;
}