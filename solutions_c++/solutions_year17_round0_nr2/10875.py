#include<iostream>
using namespace std;
int areSorted(uint64_t n)
	{
	
	    uint64_t next_digit =n % 10;
	    n = n/10;
	    while (n!=0)
	    {
	         uint64_t digit =n%10;
	        if (digit > next_digit)
	            return 0;
	        next_digit = digit;
	        n = n/10;
	    }
	 
	    return 1;
	}

int  main ()
	{
		
        uint64_t T;
        cin>>T;
        uint64_t no;
		for(int i=0;i<T;i++)
		{
		cin>>no;
		
		while(no>0)
		{
			if(areSorted(no)==1)
			    {
			    cout<<"Case #"<<i+1<<": "<<no<<"\n";
			    break;
			    }
			
			no--;
		}
		}
		return 0;
	}
	
	
