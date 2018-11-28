#include<bits/stdc++.h>
using namespace std;

bool areSorted(long int n)
{
	// Note that digits are traversed from last to first
	int next_digit = n%10;
	n = n/10;
	while (n)
	{
		int digit = n%10;
		if (digit > next_digit)
			return false;
		next_digit = digit;
		n = n/10;
	}

	return true;
}

int main(){
 int T,flag=0,temp;
 long long int i,N;
 cin>>T;
 temp=T;
 while(T-->0)
 {
   cin>>N;
   flag=0;
   for(i=N;i>=1;i--){
	  if(areSorted(i))
      { flag=1; break; }		  
   } 
  if(flag==1){
	cout<<"Case #"<<(temp-T)<<": "<<i<<endl;   
  } 
 } 
 return 0;
}