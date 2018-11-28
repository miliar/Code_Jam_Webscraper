#include<bits/stdc++.h>
using namespace std;

long long int n;



int main()
{
	int T;
	scanf("%d",&T);
	int t,a,i,j;
	
	ofstream o("program3data.txt");
	for(t=1;t<=T;t++)
	{char s[1005];
	o<<"Case #"<<t<<": ";
	scanf("%s",s);
		scanf("%d",&n);
		
		int ans=0;
		for(i=0;i<strlen(s);i++){
			
			int c=i;
			if(s[i]=='+')continue;
		ans++;
			if(i+n>strlen(s))  
			c= strlen(s)-n;
			for(j=0;j<n;j++){
				if(s[c+j]=='+')
				s[c+j]='-';
				else
				s[c+j]='+';
			}
				
			
			
			
		}
		
				for(i=0;i<strlen(s);i++){
				if(s[i]=='-')
				{
				cout<<"Impossible";
				o<<"Impossible";
				break;}
				
				}

	if(i==strlen(s))
	{
	cout<<ans;
	o<<ans;
}
		cout<<"\n";
		o<<endl;
	
	}
	return 0;
}
