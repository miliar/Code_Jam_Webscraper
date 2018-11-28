#include<bits/stdc++.h>
using namespace std;
int main(){
	
	int t;
	string n;
	
	scanf("%d", &t);
	
	int cont=1;
	
	
	while(t--){
		cin>>n;
		int s = n.size();
		bool order = false;
		while(order==false){
			order = true;
			for(int i=0;i<s-1;i++){
				if(n[i] > n[i+1]){
					order = false;
					n[i] = n[i]-1;
					while(i<s-1)n[++i] = '9';
				}
				//cout<<n[i];
			}
		}
		int i=0;
		while(n[i] == '0') i++;
		string resp = "";
		for(;i<s;i++){
			resp+=n[i];	
		}
		
		printf("Case #%d: ", cont++);
		cout<<resp<<endl;
	}
	
	return 0;
}
