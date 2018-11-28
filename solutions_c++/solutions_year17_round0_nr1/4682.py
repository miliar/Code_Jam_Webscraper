#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;




int main() {

#ifndef ONLINE_JUDGE
	freopen("filename.in","r",stdin);
	freopen("filename.txt","w",stdout);
#endif

	int n,k,i,j,a,b;
	int array[1005];
	char string[1005];
	int flip,flip_count,len,check;
	
	cin>>n;
	
	for(j=1;j<=n;j++)
	{	
		string[0]='\0';
		cin>>string;
		cin>>k;
		flip=0;
		len=strlen(string);
		
		
		for(i=0;i<len;i++)
		array[i]=0;

		for(i=0;i+k<=len;i++)
		{
			flip_count=array[i];
			if(flip_count%2==1) 
				{
					if(string[i]=='+') string[i]='-';
					else if(string[i]=='-') string[i]='+';
				}
			
			array[i]=0;
			
			if(string[i]=='-') 
				{
				flip++;
				if(string[i]=='+') string[i]='-';
					else if(string[i]=='-') string[i]='+';
				for(a=i+1;a<i+k;a++) array[a]++; 
				}
	
	/*		cout<<string<<endl;
			for(b=0;b<len;b++)
				cout<<array[b];
			cout<<endl;
	*/		
		}
		
		int check=1;
		for(i=len-k+1;i<len;i++)
		{
			flip_count=array[i];
			if(flip_count%2==1) 
				{
					if(string[i]=='+') string[i]='-';
					else if(string[i]=='-') string[i]='+';
				}
			array[i]=0;
		}
		
		for(i=0;i<len;i++)
			if(string[i]=='-') check=0;
			
		if(check==1) cout<<"Case #"<<j<<": "<<flip<<endl;
		if(check==0) cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;

	}
	
	return 0;
}

