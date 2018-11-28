// Tidy Number

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
using namespace std;

/* A utility function to reverse a string */
void reverse(char str[], int length)
{
	int start = 0;
	int end = length -1;
	while (start < end)
	{
		swap(*(str+start), *(str+end));
		start++;
		end--;
	}
}

// Implementation of itoa()
char* itoa(unsigned long num, char* str)
{
	int i = 0;
	// cout << "num: " << num << endl;
	if (num == 0)
	{
		str[i++] = '0';
		str[i] = '\0';
		return str;
	}

	// Process individual digits
	while (num != 0)
	{
	    // unsigned long rem = fmod(num,10);
		unsigned long rem = num % 10;
	    // cout << "rem: " << rem << endl;
		str[i++] = rem + '0';
		num /= 10;
	}

	str[i] = '\0'; // Append string terminator

	// Reverse the string
	reverse(str, i);
	return str;
}

bool Tidy(unsigned long n)
{
	char c[500];
	//itoa(n,c,10);
	// snprintf(c, sizeof(c), "%d", n);
	// cout << "itoa: -" << c  << "-" << endl;
	itoa(n, c);
	char* s;
	s = c;
	/*while (*s && *s == '0') s++; /* find the first non '0' element */
	// removing leading zeros
	// cout << "s: " << s << endl;
	for(int i = 0; s[i+1] != '\0'; i++)
	{
		if(s[i] > s[i+1]) 
		{ 
		    // cout << "i: " << i << endl;
		    return false;  
		}
	}
	return true;
}

int main()
{
	ofstream p;
	ifstream q;
	string src;
	
	p.open("output.txt");
	q.open("input.txt");

	int tc;
	q >> tc;

	for(int cnt = 1; cnt <= tc ; cnt++)
	{
		unsigned long N;
		q >> N;
		unsigned long output;
		
		while(!Tidy(N))
		{
			// Prep the 'N' value
			char str[100];
			itoa(N, str);
			int i;
			for(i = 0; str[i+1] != '\0'; i++)
			{
				if(str[i] > str[i+1])
					break;
				// cout << "i: " << i+1 << endl;
			}
			// unsigned long rest = atoi(str,i+1);
			{
				unsigned long res = 0;
				for (int j = i+1; str[j] != '\0'; ++j)
				{
					res = res*10 + str[j] - '0';
				}
			    // cout << "res: " << res << endl;
			    N -= res;
			    N--;
			}
			//if(!Tidy(N)) { N--; }
			// else { break; }
		}
		
		/*while(N >= 0)
		{
			if(Tidy(N))
			{
				output = N;
				break;
			}
			if(N == 99999999999999999) { break; }
			N--;
		}*/
 		p << "Case #" << cnt << ": " << N << endl;
	}
	// p << sizeof(unsigned long) <<  "-" << sizeof(long) << "-" << sizeof(long double) << endl;
	p.close();
	q.close();
}