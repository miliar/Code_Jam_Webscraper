#include <iostream>
using namespace std;
int tidy(int n)
{
  int ans=1,take,rem;
  for(int i=1;i<=n;i++)
     { take=i;
       rem=9;
       while(take!=0)
       {
	 if(rem>=(take%10))
	   {
	     rem=take%10;
	     take=take/10;
	   }
	  else
	     break;
       }
       if(take==0)
       ans=i;
     }
  return ans;
}

int main() {
	int no[100],cas[100],t;
  cin>>t;
  for(int i=0;i<t;i++)
  cin>>no[i];

  for(int i=0;i<t;i++)
  cas[i]=tidy(no[i]);

  for(int j=0;j<t;j++)
  {cout<<"Case #"<<j+1<<":"<<cas[j]<<"\n";}
	return 0;
}