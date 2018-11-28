#include <bits/stdc++.h>

using namespace std;

int main(){
	int test;
	cin>>test;
	int t=1;
	int cnt,n,k;
	string fin;
	while(test--){
		cnt=0;
		string res;
		cin>>res;
		cin>>k;
		n=res.size();
		fin="";
		for(int i=0;i<n;i++)
			fin+="+";
		reverse(res.begin(), res.end());
		for(int j=0;j+k<=n;j++){
			if(res[j]=='+')
				continue;
			cnt++;
			for(int x=j,y=0;y<k;y++,x++)
				if(res[x]=='+')
					res[x]='-';
				else
					res[x]='+';
		}
		cout<<"Case #"<<t<<": ";
		if(fin!=res)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<cnt<<"\n";
		t++;
	}
	return 0;
}