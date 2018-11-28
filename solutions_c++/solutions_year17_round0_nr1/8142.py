#include<bits/stdc++.h>

using namespace std;

int main(){

	cin.sync_with_stdio(0); cin.tie(0);

	int t,k;
	string s;

	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>s>>k;


		int mov=0;
		int tam=s.size();
		int ini=0,fin=k-1;


		while(fin<tam){

			if(s[ini]=='-'){
				mov++;
				for(int j=ini;j<ini+k;j++){
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}

			ini++,fin++;

		}

		bool ans=true;
		for(int j=0;j<tam;j++)
			if(s[j]=='-') ans=false;


		cout<<"Case #"<<i<<": ";
		if(ans) cout<<mov<<"\n";
		else cout<<"IMPOSSIBLE\n";

	}






	return 0;
}