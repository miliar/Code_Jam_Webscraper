#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int T=1;T<=t;T++){
		string inp;
		cin >> inp;
		int k;
		cin >> k;
		int len = inp.length();
		int str[len];
		for(int i=0;i<len;i++)
			if(inp[i]=='-')
				str[i]=0;
			else
				str[i]=1;

		int count=0;
		for(int i=0;i<=len-k;i++){
			if(str[i]==0){
				count++;
				for(int j=i;j<k+i;j++)
					str[j]=1-str[j];
			}
		}

		//---+-++-
		//01234567
		int flag=true;
		for(int i=0;i<len;i++)
			if(str[i]==0)
				flag=false;
		cout <<"Case #"<<T<<": ";
		if(flag)
			cout << count << endl;
		else
			cout <<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
