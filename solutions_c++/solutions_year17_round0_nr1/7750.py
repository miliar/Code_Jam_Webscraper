#include <bits/stdc++.h>

int main()
{
	long long int t,T,k,len,res,l,i,j;
	char str[1005];

	for(std::cin >> T, t = 1; t <= T; t++)
	{
		std::cin>>str>>k;
		len = strlen(str);
		res = 0;
		for(i=0;i<len;i++)
		{
			if((str[i]=='-') && (i+k <=len))
			{
				for(j=i,l=0;l<k;l++,j++)
				{
					if(str[j]=='-')
						str[j]='+';

					else if(str[j]=='+')
						str[j]='-';
				}
				res++;
			}
		}
		bool flag = true;
		for(i=len-1;i>=0;i--)
		{
			if(str[i]=='-')
			{
				flag = false;
				break;
			}
		}
		if(flag == true)
			std::cout<<"Case #"<<t<<": "<<res<<"\n";
		else
			std::cout<<"Case #"<<t<<": IMPOSSIBLE\n";
	}
}