#include <iostream>

using namespace std ;

int main()
{
	int T ;
	cin >> T ;

	for(int i = 0 ; i < T ;++i)
	{
		int K ;
		char inpstr[1002];
		cin >> inpstr >> K ;
		int size = 0 ;
		//getting size.
		while( inpstr[size] != '\0')
			++size ;
		int minNeeded = 0;	
		int nplus = 0;		
		int idx = 0 ;
		while( inpstr[idx] != '\0')
		{
			if(inpstr[idx] == '+')
			{
				++nplus ;
				++idx ;
			}
			else
			{
				if( (size - idx) < K )
					break ;
				int p = 0 ;
				//flip.
				while(p < K )
				{
					inpstr[idx + p] = (inpstr[idx + p] == '+') ? '-' : '+' ;
					++p ;
				}
				++minNeeded ;
			}				
			
		}	
		if( nplus == size)
		cout << "Case #" << i +1 << ": " << minNeeded << endl ;
		else
		cout << "Case #" << i +1 << ": IMPOSSIBLE" << endl ;
		
	}

	return 0 ;
}
