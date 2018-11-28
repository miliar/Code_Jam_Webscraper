#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int test;
	cin >> test;
	int casen=1;
	while(test--)
	{
		int num,k,last,next,flag;
		cin >> num;
		num=num+1;
		int count=0;
		while(num--)
		{
			k=num;
			last=9;next=0;flag=0;
			while(k>0)
			{
				next=k%10;
				k=k/10;
				if(next>last)
				{
					flag=1;
					break;
				}
				else
				{
					last=next;
				}

			}
			if(flag==0)
                        {
			count=num;
                        break;
                        }
		}
		printf("Case #%d: %d\n",casen,count);
		casen++;
	}
	return 0;
}
