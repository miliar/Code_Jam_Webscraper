#include <iostream>
using namespace std;
#include <string>

int minFlipsK(string pancakes,int K);
int Flip(string pancakes,int start_pos,int K);

main()
{
	int T;
	cin>>T;

	string pancakes;
	int K,no_pancakes;

	int i,j,l,minFlips;
	for(i=0;i<T;++i)
	{
		cin>>pancakes>>K;
			
		no_pancakes=pancakes.length();

		minFlips=0;

		for(j=0;j<no_pancakes;++j)
			//look for back facing pancakes in the row
			if(pancakes[j]=='-')
				if(j+K>no_pancakes)
					break;

				else
				{
					//flip the K pancakes starting at j
					for(l=0;l<K;++l)
					{
						if(pancakes[j+l]=='-')
							pancakes[j+l]='+';

						else
							pancakes[j+l]='-';
					}

					minFlips++;

				}
			
			

		cout<<"case #"<<i+1<<": ";
		if(j==no_pancakes)
			cout<<minFlips<<endl;

		else
			cout<<"IMPOSSIBLE"<<endl;

	}


}
