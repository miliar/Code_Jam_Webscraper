#include<iostream>
using namespace std;
long long check_z(long long);
long long check_t(long long);
int main()
{
    int t,total,cnt;
    
    long long n,num,tidy;
    cin>>t;
    total=t;
    cnt=1;
while(t--)
{
    cin>>num;
    n=check_z(num);
    tidy=check_t(n);
    
    //cout<<tidy<<endl;
    
    //for (int i = 1; i <= total; ++i) {
      // read n and then m.
    cout << "Case #" << cnt << ": " <<tidy<< endl;
    cnt++;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  
    
    
//	int d,i;
//    i=0;
//	while(n)
//    {
//        
//        d=n%10;
//        arr[i]=d;
//        i++;
//        n=n/10;
//    }
//    int j;
//    for(j=i-1;j>0;j--)
//    {
//        if(!(arr[j]>arr[j-1])
//    }
//    cout<<endl;

}

    return 0;
}
long long check_z(long long a)
{
	long long numbre=a;
	int c=0;
	while(a)
	{
		int d;
		d=a%10;
		if(d==0)
		{
			c=1;
			break;	//zero present
		}
		a=a/10;
		
	}
	if(c==1)
	{
		return check_z(numbre-1);
	}
	else
	{
		return numbre;
	}
	
}
long long check_t(long long b)
{
	int d,i;
	int arr[18];
	long long number=b;
    i=0;
	while(b)
    {
        
        d=b%10;
        arr[i]=d;
        i++;
        b=b/10;
    }
    
    int j,mark=0;
    for(j=i-1;j>0;j--)
    {
        if(!(arr[j]<=arr[j-1]))
        {
        	mark=1;
			break;	//not in increasing order
		}
    }
    if(mark==1)
    {
    	return check_t(number-1);
	}
	else
	{
		return number;
	}
    
}
