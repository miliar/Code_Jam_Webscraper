#include<bits/stdc++.h>
using namespace std;
int main(){
	
		char a[99999];
		int t,i,j,k;
		cin>>t;
		int s=0;
		while(t--){
				int c=0;

			scanf("%s",a);
				s++;
			cin>>k;

			for(i=0;i<strlen(a);i++){

				if(a[i]=='-')
				{
					int p=i+k-1;
					//cout<<p<<endl;
					if(p<=strlen(a)-1){
					for(j=i;j<=p;j++){
						if(a[j]=='+')
							a[j]='-';
						else 
							a[j]='+';

						
						}
						c++;	
					}
				}	

		}
			

			int sign=0;
			for(i=0;i<strlen(a);i++)
			{
				if(a[i]=='-')
				{
					cout<<"Case #"<<s<<": "<<"IMPOSSIBLE"<<endl;
					sign=1;
					break;
				}
			}
			if(sign==0){
				cout<<"Case #"<<s<<": "<<c<<endl;
			}

				//printf("%s",a);
		}


	return 0;
}
