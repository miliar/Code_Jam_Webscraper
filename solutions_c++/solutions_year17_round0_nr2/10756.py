#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int t,c=1;
	scanf("%d",&t);
	while(c<=t)
	{
		unsigned long n;
		scanf(" %lu", &n);
		vector<int> numArr;
		unsigned long tempNum=n;
		while(tempNum>0)
		{
			numArr.push_back((int)tempNum%10);
			tempNum=tempNum/10;
		}
		vector<int>::iterator i;
		reverse(numArr.begin(),numArr.end());
		int length=numArr.size();
		int equalCount=1;
		for(i=numArr.begin()+1;i!=numArr.end();++i)
		{
			if(*i==*numArr.begin())
			{
				++equalCount;
			}
		}
		if(equalCount==length)
		{
			printf("Case #%d: %lu\n",c,n);
			c++;
			continue;
		}
		int breakIndex=-1;
		for(i=numArr.begin();i!=numArr.end();++i)
		{
			if((i+1)!=numArr.end() && (*i>*(i+1)))
			{
				breakIndex=i-numArr.begin();
				break;
			}
		}
		if(breakIndex==-1)
		{
			printf("Case #%d: %lu\n",c,n);
			c++;
			continue;
		}
		int breakvalue=*(breakIndex+numArr.begin());
		if(breakIndex!=0)
			{
				vector<int>::reverse_iterator r=(numArr.rend()-1-(breakIndex-1));
					while(r!=(numArr.rend()) && *r==breakvalue)
					{						
							breakIndex--;
							r++;
					}
			}
		*(numArr.begin()+breakIndex)=*(numArr.begin()+breakIndex)-1;
		i=breakIndex+1+numArr.begin();
		while(i!=numArr.end())
		{
			*i=9;
			++i;
		}
		printf("Case #%d: ",c);
		i=numArr.begin();
		if(*numArr.begin()==0)
			i=numArr.begin()+1;
		while(i!=numArr.end())
		{
			printf("%d",*i);
			++i;
		}
		printf("\n");
		++c;
	}
	return 0;
}