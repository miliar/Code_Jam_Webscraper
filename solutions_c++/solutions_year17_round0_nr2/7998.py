#include<bits/stdc++.h>
using namespace std;
string processing(string inp,int inv){
	int len = inp.length();
	for(int i=inv+1;i<len;i++)
		inp[i]='9';
	inp[inv]-=1;
	return inp;
}
int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		string inp;
		cin >> inp;
		int len = inp.length();
		if(len!=1){
			for(int iter=0;iter<len;iter++){
				int inversion=-1;
				for(int i=0;i<len-1;i++){
					if(inp[i]>inp[i+1]){
						inversion = i;
						break;
					}
				}
				if(inversion!=-1){
					inp = processing(inp,inversion);
				}
			}
		}
		int zero=0;

		cout <<"Case #"<<t<<": ";

		while(inp[zero]=='0')
			zero++;
		for(int i=zero;i<len;i++)
			cout << inp[i];

		cout << endl;
	}
	return 0;
}
