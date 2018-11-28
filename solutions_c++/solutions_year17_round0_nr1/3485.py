#include <iostream>
using namespace std;

bool cakes[2000];

int onecase()
{
	int k;
	string s;

	cin>>s>>k;

	int l=s.length();
	for(int i=0;i<l;i++){
		cakes[i]=(s[i]=='+');
	}


	int count=0;
	for(int i=0;i<l-k+1;i++){
		if(cakes[i])continue;

		count++;
		for(int j=i;j<i+k;j++){
			cakes[j]=!cakes[j];
		}

	}

	bool cond=true;
	for(int i=0;i<l;i++)
		cond=cond && cakes[i];
	if(cond) cout<<count<<endl;
	else cout<<"IMPOSSIBLE"<<endl;
	return 0;
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		onecase();
	}
	return 0;
}