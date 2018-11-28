#include <iostream>
#include<string.h>
using namespace std;

int main() {
	int test=0;
	cin>>test;
	for(int n =1;n<=test;n++){
	    int f=0;
	char str[10];
	int k=10;
	cin>>str>>k;
	int c=0;
	for(int i=0;i<strlen(str);i++){
	    if(str[i]=='-' && (strlen(str)-i>=k)){
	        ++c;
	        for(int j=i;j<k+i;j++){
	            if(str[j]=='-')
	            str[j]='+';
	            else
	            str[j]='-';
	        }
	    }
	}
	
	for(int m=0;m<strlen(str);m++){
	    if(str[m]=='-')
	    f=1;
	}
	if(f==1)
	cout<<"Case #"<<n<<": IMPOSSIBLE"<<endl;
	else
	cout<<"Case #"<<n<<": "<<c<<endl;
	
	};
	return 0;
}
