#include<bits/stdc++.h>
using namespace std;

typedef long long int LL;

int main()
{
	int t, n, ca=1;
	char str[22];
	
	scanf("%d", &t);
	
	while(t--)
	{
		cin>>str;
		printf("Case #%d: ", ca);
		ca += 1;
		
		n = strlen(str);
		
		if(n == 1)
		{
			printf("%s\n", str);
		}
		
		else
		
		{
			int i,j;
			for(i=0;i<n-1;++i)
			{
				//Reduce
				if(str[i+1]-'0'<str[i]-'0')
				{
					//cout<<"Found at index: "<<i<<endl;
					
					for(j=i-1;j>=0 && str[j]==str[i];--j);
					++j;
					//cout<<"To flip from: "<<j<<endl;
					//Change this to zero and next all to 9s
					if(str[j]=='1')
					{
						str[j]='0';	
					}
					
					else
					{
						str[j] = (char)(((int)str[j])- 1);
					}
					
					//cout<<"After flip "<<str<<endl;
					for(++j;j<n;++j)str[j]='9';
					break;
				}
			}
			
			//cout<<str<<endl;
			
			LL sum = 0;
			
			for(i=0;i<n;++i)sum = sum*10 + str[i]-'0';
			printf("%lld\n", sum);
		}
	}
	return 0;
}
