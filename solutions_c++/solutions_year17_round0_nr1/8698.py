#include <iostream>
#include <string.h>
using namespace std;
void check(char* num,int k)
{
int i,l,j,c=0;
l=strlen(num);
for(i=0;i<l;i++){
	j=0;
	if(num[i]=='-'){
		if(i+k>l){
		 cout<<"IMPOSSIBLE";
		 return;}
		while(j<k&& i+j<l){
			if(num[i+j]=='-')
			 num[i+j]='+';
			else
			 num[i+j]='-';
			 j++;
		}
		c++;
	}
	  
}
cout<<c;
}
int main() {
	int t,i,k;
	char num[1000];
	cin>>t;
	for(i=1;i<=t;i++)
	{cin>>num;
		cin>>k;
        cout<<"Case #"<<i<<": ";
		 check(num,k);
		 cout<<endl;
	}
	return 0;
}