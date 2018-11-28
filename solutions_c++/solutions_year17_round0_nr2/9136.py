#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

int issort(char str[])
{	
	int n=strlen(str);
	for(int i=0;i<n-1;i++)
	{	
		if(str[i]>str[i+1]) return i;
	}
	return -1;
}

int main()
{
	int T;
	cin >> T;
	for(int j=0;j<T;j++)
	{
		char num[20];
		cin >> num;
		int n=strlen(num);
	
		while(issort(num)!=-1)
		{	
		
			int key=issort(num);
			num[key]--;
			for(int i=key+1;i<n;i++)
				num[i]='9';			
				
		}
		
		
		cout << "Case #"<<j+1<<": ";
		
		
		if(num[0]!='0') cout << num[0];
		for(int i=1;i<n;i++)
		{
			cout << num[i]; 
		}
		cout << endl;
	 
	} 
	
	
	
	return 0;
}
