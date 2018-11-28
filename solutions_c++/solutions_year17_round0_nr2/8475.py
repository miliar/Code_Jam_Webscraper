#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;

int main()
{
	int t,i=0,s=0,k;
	char a[20];
	cin>>t;
	cin.getline(a,20);
 	for(s=0;s<=t-1;s++)
	{   
	  	cin.getline(a,20);  	
	    k=strlen(a);

         for(i=0;i<=k-2;i++)
         {
         	if(a[i]=='0')
         	{
         	  k--;
			  for(;i<=k-1;i++)
		 	  a[i]='9';

			}
         	else if(a[i+1]<a[i])
         	{
		 	 a[i]-=1;i++;
		 	 for(;i<=k-1;i++)
		 	 a[i]='9';
		 	 i=-1;
	        }
	     }
	    cout<< "Case #" << s+1<<": ";
	    for(i=0;i<=k-1;i++)
	    cout<<a[i];
	    cout<<"\n";
	}
}
	   
