#include<bits/stdc++.h>
using namespace std;
typedef int ll;
int main()
{
	ll n,t,cnt=0;
	string s;
	scanf("%d",&t);
	for (int i = 1; i <= t; ++i)
	{
		cin>>s;
		scanf("%d",&n);
		
		cnt=0;
		int flag=0;

		for(int j=0;j<s.length();j++){
				if(s[j]=='-'){
					cnt++;
					if(j+n<=s.length()){
					for (int k= j; k < j+n; ++k)
					{
						if(s[k]=='+')s[k]='-';
						else s[k]='+';
					}
				}
				}


		}


		for(int j=0;j<s.length();j++){
			if(s[j]=='-'){
				//cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
				printf("Case #%d: IMPOSSIBLE\n",i);
				flag=1;
				break;
			}
		}
		if(!flag){
			//cout<<"Case #"<<i<<": "<<cnt<<endl;
			printf("Case #%d: %d\n",i,cnt);
		}
		
	

	}
	
}
