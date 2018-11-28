#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int valid(char* x){
	int len=strlen(x);
	for(int i=0;i<len;i++){
		if (x[i]=='-') return 0;
	}
	return 1;
}


int main(){
	freopen("A-large.in","r",stdin);
	freopen("outALarge.txt","w",stdout);
	ll t,n;
	char str[10005];
	cin>>t;
	int k;
	for(int z=1;z<=t;z++){
		int ans=0;
		cin>>str>>k;
		int len=strlen(str);
		for(int i=0;i<len;){
			//printf("i %d ans %d ",i,ans);
			//cout<<str<<endl;
			if (str[i]=='-'){
				int j;
				for(j =i;j<i+k;j++){
					if (str[j]=='-') str[j]='+';
					else str[j]='-';	
				}
				i++;
				ans++;
			}else i++;
		}
		
		if (valid(str))
			printf("Case #%d: %d\n",z,ans);
		else {
			printf("Case #%d: IMPOSSIBLE\n",z);
		}
	}
		
	
	return 0;
}

