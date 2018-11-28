#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("1.txt","w",stdout);
	int T,TT=0;
	scanf("%d",&T);
	while(T--){
		char a[2005];
		int l,n;
		cin>>a>>l;
		n=strlen(a);
		printf("Case #%d: ",++TT);
		int cnt=0;
		for(int i=0;i<n-l+1;i++)
			if(a[i]=='-'){
				for(int j=i;j<=i+l-1;j++)
					if(a[j]=='+')
						a[j]='-';
					else
						a[j]='+';
				cnt++;
			}	
		bool can=true;
		for(int i=n-l+1;i<n;i++)
			if(a[i]=='-'){
				can=false;
				break;
			}	
		if(can)
			printf("%d\n",cnt);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4

*/
