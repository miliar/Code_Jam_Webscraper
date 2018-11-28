#include <bits/stdc++.h>

using namespace std;



void tiny(char b[],int n){
	int i,j;
	for(i=0;i<n-1;i++){
		if(b[i]>b[i+1]){
			while((i)&&(b[i]==b[i-1])){
				i--;
			}
			b[i]--;
			for(j=i+1;j<n;j++){
				b[j]='9';
			}
			break;
		}
	}
	if(b[0]=='0'){
		for(i=0;i<n;i++){
			b[i]=b[i+1];
		}
	}
	b[n]='\0';
}

main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	char a[20];
	int i,n,m;
	cin>>n;
	gets(a);
	for(i=0;i<n;i++){
		gets(a);
		m=strlen(a);
		tiny(a,m);
		cout<<"Case #"<<i+1<<": ";
		puts(a);
	}
	return 1;
}

