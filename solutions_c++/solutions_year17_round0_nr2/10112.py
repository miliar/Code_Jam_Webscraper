#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	int t;
	int no[120];
	cin >> t;
	for(int i=0; i<t; i++)
	{
		cin >> no[i];
	}

	int a, b, len=0, num, found=0, findNext=0, tempno;
	for(int i=0; i<t; i++)
	{	no[i]++;
		while(found==0)
		{	no[i]--;
			num = no[i];
			while(num!=0)
			{
				num=num/10;
				len++;
			}
			findNext=0;
			for(int j=0; j<len; j++)
			{
				tempno = ((no[i])/(int(pow(10,j))));
				a = (tempno)%10;
				tempno = ((no[i])/(int(pow(10,j+1))));
				b = (tempno)%10;
				if(a<b) {
					findNext=1;
					break;
				}
			}
			if(findNext==0)
			{
				cout << "Case #" << i << ":"  << no[i] << endl;
				found=1;
			}
		}
		found=0;
	}
	return 0;
}