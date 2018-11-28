#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <unistd.h>
#include <vector>

using namespace std;

/* #define DEBUG */
// #define PRINT

#ifdef DEBUG
#ifdef stdin
#undef stdin
#endif
#define stdin infile
#define infilename "/home/mate/docs/programming/google_code_jam/2017/qualification/A/sample.in"
#endif

size_t getNextPancake (char* buffer, size_t bufsize, size_t cursor, vector<char>& pancake)
{
	pancake.clear();

	/* find the start of the next pancake */
	while (cursor < bufsize &&
			buffer[cursor] != '+' && buffer[cursor] != '-')
	{
		++cursor;
	}

	/* fill the vector with the pancake*/
	while (cursor < bufsize &&
			(buffer[cursor] == '+' || buffer[cursor] == '-'))
	{
		pancake.push_back(buffer[cursor]);
		++cursor;
	}
	return cursor;
}

size_t getNextK (char* buffer, size_t bufsize, size_t cursor, size_t& K)
{
	/* find the start of the next K */
	while (cursor < bufsize &&
			(buffer[cursor] < '0' || buffer[cursor] > '9'))
	{
		++cursor;
	}

	K = 0;
	/* fill the vector with the pancake*/
	while (cursor < bufsize &&
			(buffer[cursor] >= '0' && buffer[cursor] <= '9'))
	{
		K*=10;
		K+=buffer[cursor]-'0';
		++cursor;
	}
	return cursor;
}

char buffer [10*1024*1024]; /*100 * 1000 characters + some stuff is expected. Must be enough.*/
vector<char> pancake; /*1000 characters at most. Must be enough.*/
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
#if 1 //defined(PRINT)
    	fprintf (stderr, "\n#%d-------------------\n", (int)(t+1));
#endif
        cursor = getNextPancake (buffer, sizeof(buffer), cursor, pancake);
        if (cursor >= sizeof(buffer))
        {
            fprintf (stderr, "cannot find next pancake!\n");
            return 0;
        }
        size_t K;

        cursor = getNextK(buffer, sizeof(buffer), cursor, K);
        if (cursor >= sizeof(buffer))
        {
            fprintf (stderr, "cannot find next K!\n");
            return 0;
        }

#if defined(PRINT)
        fprintf (stderr, "K=%u ", (unsigned int)K);
        fprintf (stderr, "[%u]\n", (unsigned int)pancake.size());
        for (unsigned int i = 0; i < pancake.size(); ++i)
        {
            fprintf (stderr, "%c", pancake[i]);
        }
        fprintf (stderr, "\n");
#endif

        int flipCount = 0;

        for (unsigned int i = 0; i < pancake.size(); ++i)
        {
            if (pancake[i] == '+')
            {
            	continue;
            }

            /* flip */
#if defined(PRINT)
            fprintf (stderr, "flip at %u\n", (unsigned int)i);
#endif
            if (i+K > pancake.size())
            {
            	flipCount = -1;
            	break;
            }

            for (unsigned int j = 0; j < K; ++j)
            {
            	if (pancake[i+j]=='-')
            	{
            		pancake[i+j]='+';
            	} else {
            		pancake[i+j]='-';
            	}
            }
            ++flipCount;
#if defined(PRINT)
            for (unsigned int i = 0; i < pancake.size(); ++i)
            {
                fprintf (stderr, "%c", pancake[i]);
            }
            fprintf (stderr, "\n");
#endif
		}
        fprintf (stderr, "Case #%d: ", (int)(t+1));
        if (flipCount < 0)
        {
        	fprintf (stderr, "IMPOSSIBLE\n");
        } else {
        	fprintf (stderr, "%d\n", flipCount);
        }

        printf ("Case #%d: ", (int)(t+1));
        if (flipCount < 0)
        {
        	printf ("IMPOSSIBLE\n");
        } else {
        	printf ("%d\n", flipCount);
        }
    }
}
