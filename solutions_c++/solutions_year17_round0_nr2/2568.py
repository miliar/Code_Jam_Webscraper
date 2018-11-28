#include<iostream>
#include <string>
using namespace std;

string doatest(){
	char str[100];
	cin>>str;
	int cur=0;
	int i;
	int len=strlen(str);
	for(i=1;i<len;i++){
		if(str[i]>str[cur]){
			cur=i;
			continue;
		}
		if(str[i]==str[cur])continue;
		break;
	}
	if(i==len)
		return string(str);
	i=cur;
	str[i++]--;
	for(;i<len;i++)
		str[i]='9';
	int j=0;
	for(j=0;str[j]=='0';j++);
	i=0;
	for(;j<=len;j++)
		str[i++]=str[j];
	return string(str);
}

int main(){
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		string res=doatest();
		cout<<"Case #"<<t+1<<": "<<res<<endl;
	}
	return 0;
}