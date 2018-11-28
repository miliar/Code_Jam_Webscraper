#include<bits/stdc++.h>
#define max 100005
#define mod 1000000007
using namespace std;

typedef long long int lli;
typedef long int li;

int main()
{
    
   li t=1,k,i,g,count,len,j,h,check,check1;
   char str[100005];
   cin>>h;
   while(t<=h)
   {
	   cin>>str>>k;

//	   cout<<"first "<<str<<" "<<k<<"\n";
	   count=0;

	   len=strlen(str);

	   for(i=0 ; i+k<len ; )
	   {
		   if(str[i] == '-')
		   {
			 count++;  
			 j=i;
			 g=k;
			 while(g--)
			 {
				 if(str[j] == '-')
					 str[j]='+';
				 else
					 str[j]='-';
				 j++;
			 }
			 i++;
		   }
		   else
		   {
			   i++;
		   }	   
			   
			   
	   }
	   check=0;check1=0;
	   for( ; i<len ; i++)
	   {
		   if(str[i]=='+')
		   {
			   check1=1;
		   }
		   else
		   {
			   check=1;
		   }

	   }
	   if(check && check1)
	   {
		   cout<<"Case #"<<t<<": "<<"IMPOSSIBLE\n";
	   }
	   else
	   {
		   if(check)
			   cout<<"Case #"<<t<<": "<<count+1<<"\n";
		   else
			   cout<<"Case #"<<t<<": "<<count<<"\n";

	   }


	   
	   //cout<<"second "<<str<<" "<<k<<"\n";
	   t++;
   }
    
    
    
    
    return 0;
}
