#include <iostream>
using namespace std;
#include <cstring>
int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,k=1;
	cin>>t;
	
	while(k<=t){
		cout<<"Case #"<<k<<": ";
	char str[20];
	int i,pos,flag=1,count=0;
	cin>>str;
	pos=strlen(str);
	for(i=0;i<strlen(str)-1;i++){
		if(str[i]>str[i+1]){
			if(str[i]=='1')
				flag=0;
			pos=i;
			break;
			}
		}
		
	for(i=pos+1;i<strlen(str);i++){
		str[i]='9';
	}
	for(i=pos;str[pos]==str[i-1];i--){
		pos--;
		str[i]='9';
	}
	if(pos==-1)
	pos++;
	if(pos<strlen(str))
		str[pos]=str[pos]-1;
	if(flag==0 && pos==0)
	{string s=str;
		cout<<s.substr(1)<<endl;
	}
	
	else{
	cout<<str<<endl;
	}
	k++;
}
	return 0;
	
}
