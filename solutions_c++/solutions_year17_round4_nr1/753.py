#include <bits/stdc++.h>

using namespace std;

#define INTMAX 0x7FFFFFFF
#define INTMIN -0x80000000
#define LONGMAX 0x7FFFFFFFFFFFFFFF
#define LONGMIN -0x8000000000000000

int divup(int a, int b){
	int res = a/b;
	if(a%b!=0)
		res++;
	return res;
}

int main(){
	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		int n,p;
		cin>>n>>p;
		int g[n];
		for(int i=0; i<n; i++)
			cin>>g[i];
		
		int mod[4];
		mod[0] = mod[1] = mod[2] = mod[3] = 0;
		for(int i=0; i<n; i++)
			mod[ g[i]%p ]++;
		
		int res;
		if(p==2){
			res = mod[0] + divup(mod[1],2);
		}
		else if(p==3){
			res = mod[0] + min(mod[1],mod[2]) + divup(max(mod[1],mod[2])-min(mod[1],mod[2]),3);
		}
		else{
			res = mod[0] + min(mod[1],mod[3]) + mod[2]/2;
			mod[1] -= min(mod[1],mod[3]);
			mod[3] -= min(mod[1],mod[3]);
			int mod13 = mod[1] + mod[3];
			mod[2] = mod[2]%2;
			if(mod[2]==0){
				res += divup(mod13,4);
			}
			else{
				res++;
				mod13 = max(0, mod13-2);
				res += divup(mod13,4);
			}
		}
		
		cout<<"Case #"<<tc<<": "<<res<<endl;
	}
}