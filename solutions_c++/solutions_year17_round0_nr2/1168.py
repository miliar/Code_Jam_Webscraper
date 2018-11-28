#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
	int T,cases=0;
	cin>>T;
	string n;
	while(T--){
		cin>>n;
		int i;
		for(i=1;i<n.size();i++)
			if(n[i]<n[i-1])
				break;
		if(i<n.size()){
			for(i--;i&&n[i]==n[i-1];i--);
			n[i]--;
			for(i++;i<n.size();i++)
				n[i]='9';
		}
		printf("Case #%d: ",++cases);
		if(n[0]=='0'){
			for(i=1;i<n.size();i++)
				putchar(n[i]);
			puts("");
		}
		else{
			cout<<n<<endl;
		}
	}
}
