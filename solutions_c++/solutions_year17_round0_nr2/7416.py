#include<iostream>

bool IsTidy( long long n )
{
	int last = 9;
	int cur;

	while( n>0 )
	{
		cur = n%10;
		if( cur > last )
			return false;
		last = cur;
		n/=10;
	}
	return true;
}

int Tidy( long long n )
{
	while( !IsTidy( n ) )
	{
		n--;
	}
	return n;	
}

int main()
{
	int times;
	std::cin>>times;
	int ans[times];
	for( int i=0;i<times;i++ )
	{
		long long n;
		std::cin>>n;
		ans[i] = Tidy( n );
	}

	for( int i=0;i<times;i++ )
	{
		std::cout<<"Case #"<<(i+1)<<": ";
		if( ans[i] == -1 )
			std::cout<<"IMPOSSIBLE\n";
		else
			std::cout<<ans[i]<<"\n";
	}
	std::cout<<std::endl;
}
