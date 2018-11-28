#include <iostream>
#include <cstdio>
using namespace std;


bool judge(int inp){
	if(inp<10)return true;

	char s[1000];
	sprintf(s,"%d",inp);
	int i=0;
	while(s[i+1]!='\0'){
		if(s[i]>s[i+1])return false;
		i++;
	}
	return true;
}

int onecase()
{
	int n;
	cin>>n;
	while(!judge(n))n--;
	cout<<n<<endl;
	return 0;
}

int main(){
	//onecase();return 0;

	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		onecase();
	}
	return 0;
}