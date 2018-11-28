#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <unistd.h>
#include <vector>

using namespace std;

/* #define DEBUG */
// #define PRINT

//#define PARANOID

#ifdef DEBUG
#ifdef stdin
#undef stdin
#endif
#define stdin infile
#define infilename "/home/mate/docs/programming/google_code_jam/2017/qualification/A/sample.in"
#endif

size_t getNextNumberDigits (char* buffer, size_t bufsize, size_t cursor, vector<int>& digits)
{
	/* find the start of the next number */
	while (cursor < bufsize &&
			(buffer[cursor] < '0' || buffer[cursor] > '9'))
	{
		++cursor;
	}

	digits.clear();
	/* fill the vector with the number*/
	while (cursor < bufsize &&
			(buffer[cursor] >= '0' && buffer[cursor] <= '9'))
	{
		digits.push_back(buffer[cursor]-'0');
		++cursor;
	}
	return cursor;
}

bool isTidy (size_t i)
{
	int lastDigit = 10;
	while (i)
	{
		int remainder = i%10;
		if (remainder <= lastDigit)
		{
			lastDigit = remainder;
			i /=10;
		} else {
			return false;
		}
	}
	return true;
}

bool isTidy (const vector<int>& digits)
{
	for (size_t i = 1; i < digits.size(); ++i)
	{
		if (digits[i-1] > digits[i])
		{
			return false;
		}
	}
	return true;
}

size_t getNumberFromDigits (const vector<int>& digits)
{
	size_t ret = 0;
	for (size_t i = 0; i < digits.size(); ++i)
	{
		ret *= 10;
		ret += digits[i];
	}
	return ret;
}

size_t getLargestTidy (size_t n)
{
	size_t largestTidy = 0;
	for (size_t i = 0; i <= n; ++i)
	{
		if (isTidy(i))
		{
			largestTidy = i;
		}
	}
	return largestTidy;
}

void getLargestTidy (vector<int>& digits)
{
	bool checkAgain = true;
	while (checkAgain)
	{
		checkAgain = false;
		for (size_t i = 1; i < digits.size(); ++i)
		{
			if (digits[i-1] <= digits[i])
			{
				continue;
			}

			if (digits[i-1] < 1)
			{
				fprintf (stderr, "Internal error 1\n");
				exit(1);
				return;
			}
			digits[i-1] -= 1;
			for (size_t j = i; j < digits.size(); ++j)
			{
				digits[j] = 9;
			}
			checkAgain = true;
		}
	}
}


char buffer [10*1024*1024]; /*100 * 1000 characters + some stuff is expected. Must be enough.*/
int main(int argc, char** argv) {

    unsigned int T = 0;

#ifdef DEBUG
    FILE* infile;
    infile = fopen(infilename, "r");
    if (!infile)
    {
    	fprintf (stderr, "Failed to open %s\n", infilename);
    	return 1;
    }
#endif

    fscanf (stdin, "%u", &T);

    fprintf (stderr, "Doing %d testcases\n", T);

    ssize_t bytesRead = fread(buffer, 1, sizeof(buffer), stdin);
    if (bytesRead < 0 || (size_t)bytesRead >= sizeof(buffer))
    {
        fprintf (stderr, "Need more memory!\n");
        return 0;
    }

    size_t cursor = 0;

    for (size_t t = 0; t < T; ++t)
    {
    	vector<int> digits;
        cursor = getNextNumberDigits(buffer, sizeof(buffer), cursor, digits);
        if (cursor >= sizeof(buffer))
        {
            fprintf (stderr, "cannot find next Number!\n");
            return 0;
        }

#ifdef PARANOID
        size_t N = getNumberFromDigits(digits);
#endif

#if 1 //defined(PRINT)
    	fprintf (stderr, "\n#%d = ", (int)(t+1));
		for (size_t i = 0; i < digits.size(); ++i)
		{
			fprintf (stderr, "%u", digits[i]);
		}
#ifdef PARANOID
		fprintf (stderr, " (%u)", (unsigned int)N);
#endif
		fprintf (stderr, "\n");
#endif

        getLargestTidy(digits);

#ifdef PARANOID
        size_t largestTidy = getLargestTidy(N);
        size_t largestTidyFromVector = getNumberFromDigits(digits);

        if (largestTidy != largestTidyFromVector)
        {
        	fprintf (stderr, "Mismatch: %u != %u\n", (unsigned int)largestTidy, (unsigned int)largestTidyFromVector);
        	return (1);
        }
#endif

        fprintf (stderr, "Case #%d: ", (int)(t+1));
		for (size_t i = 0; i < digits.size(); ++i)
		{
			if (digits[i])
			{
				fprintf (stderr, "%u", digits[i]);
			}
		}
#ifdef PARANOID
		fprintf (stderr, " (%u)", (unsigned int)largestTidy);
#endif
		fprintf (stderr, "\n");

        fprintf (stdout, "Case #%d: ", (int)(t+1));
		for (size_t i = 0; i < digits.size(); ++i)
		{
			if (digits[i])
			{
				fprintf (stdout, "%u", digits[i]);
			}
		}
		fprintf (stdout, "\n");
    }
}
