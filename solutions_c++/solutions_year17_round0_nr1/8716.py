#include <iostream>
#include <string.h>
using namespace std;
void checkdigits(char* num,int k)
{
int i,l,j,c=0;
l=strlen(num);
for(i=0;i<l;i++){
	j=0;
	if(num[i]=='-'){
		if(i+k>l){
		 cout<<"IMPOSSIBLE";
		 return;}
		while(j<k){
			if(num[i+j]=='-')
			 num[i+j]='+';
			else
			 num[i+j]='-';
			 j++;
			 //cout<<num<<endl;
		}
		c++;
	}
	  
}
cout<<c;
}
int main() {
	int t,i,j,check=0,len,f=0,k;
	char n[20];
	cin>>t;
	for(i=1;i<=t;i++)
	{f=0;
		cin>>n;
		cin>>k;
        cout<<"Case #"<<i<<": ";
		 checkdigits(n,k);
		 cout<<endl;
	}
	return 0;
}
