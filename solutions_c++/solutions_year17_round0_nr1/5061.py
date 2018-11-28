#include<bits/stdc++.h>
using namespace std;
const int maxn=1e3+5;
int val[maxn];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int k,t;string s;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		int res=0;
		cin>>s>>k;
		
		for(int i=0;i<s.length();i++)
			if(s[i]=='+')val[i]=1;
			else val[i]=0;
		bool ok=1;
		for(int i=0;i<s.length();i++)
			if((val[i]&1)==0){
				if(s.length()-i<k){
					ok=0;break;
				}
				res++;
				for(int j=0;j<k;j++)val[i+j]++;
			}
		printf("Case #%d: ",cas);
		if(!ok)puts("IMPOSSIBLE");
		else cout<<res<<endl;
	}
	return 0;
}