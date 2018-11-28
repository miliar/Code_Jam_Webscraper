#include<iostream>
using namespace std;

int main()
{
  int t;
  unsigned long long int n;
  cin>>t;
  for(int i=1; i <= t; i++)
    {
      cin>>n;
      unsigned int digits = 1;
      unsigned long long int temp = n;
      while(temp /= 10)
	digits++;
      unsigned int dig = digits;
      unsigned int *arr = new unsigned int[digits];
      while(dig--)
	{
	  arr[dig] = n % 10;
	  n /= 10;
	}
  
      for(int j=digits-1; j > 0; j--)
	{
	  if(arr[j] < arr[j-1])
	    {
	      arr[j-1]--;
	      for(int k=j; k < digits; k++)
		arr[k] = 9;
	    }
	}
      
      bool flag = 0;
      cout<<"Case #"<<i<<": ";
      for(int j=0; j < digits; j++)
	{
	  if(arr[j] == 0 && flag == 0)
	    flag = 1;
	  else
	    cout<<arr[j];
	}
      cout<<"\n";
    }
}
