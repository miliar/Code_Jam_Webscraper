#include <iostream>

using namespace std;

int main()
{
	std::ios::sync_with_stdio(false);
	
	unsigned int T;
	cin >> T;
	
	for (unsigned int i = 0; i < T; ++i)
	{
		unsigned int K;
		string S;
		
		cin >> S >> K;
		unsigned int len = S.length();
		
		unsigned int startIndex, endIndex;
		unsigned int flipCount = 0;
		
        startIndex = 0;
       
		
		//  Go forward until we encounter a '-'
		findStartIndex:
		while (startIndex < len && S[startIndex] != '-' )
		{
			++startIndex;
		}
		
		//setEndIndex:
		endIndex = startIndex + K - 1;
		
		//  Check if we are beyond last index
		if (endIndex >= len)
		{
			//  Check if all pancakes in the window are happy
			bool happy = true;
			for (unsigned int j = startIndex; j < len; ++j)
			{
				if (S[j] == '-')
				{
					happy = false;
					break;
				}
			}
			
			if (happy)
			{
			    //  Success
			    cout << "Case #" << i+1 << ": " << flipCount << endl;
			}
			else
			{
				//  Impossible
				cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
			}
			
			
			//  Go to next case
			continue;
		} 
		
		/*
		//  Find the first '+' in the window that will be converted to '-'
		for (unsigned int j = startIndex + 1; j <= endIndex; ++j)
		{
		*/
		
		
		//  Flip pancakes
		for (unsigned int j = startIndex; j <= endIndex; ++j)
		{
			switch (S[j])
			{
				case '-':
				    S[j] = '+';
				    break;
				case '+':
				    S[j] = '-';
				    break;
			}
		}
		++flipCount;
		
		goto findStartIndex;
	}
	
	
	
	
	return 0;
}
