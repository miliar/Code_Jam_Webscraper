#include<iostream>

int Flipper( std::string pancakes, int k )
{
	int flip = 0;
	for( int i=0;i<=pancakes.length()-k;i++ )
	{
		if( pancakes[i] == '-' )
		{
			flip++;
			for( int j=i;j<i+k;j++ )
				if( pancakes[j] == '-' )
					pancakes[j] = '+';
				else
					pancakes[j] = '-';
			i=0;
		}
	}
	for( int i=pancakes.length()-k;i<pancakes.length();i++ )
	{
		if( pancakes[i] == '-' )
			return -1; 
	}
	return flip;
}

int main()
{
	int times;
	std::cin>>times;
	int ans[times];
	for( int i=0;i<times;i++ )
	{
		std::string pancakes;
		int k;
		std::cin>>pancakes>>k;
		ans[i] = Flipper( pancakes, k );
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
