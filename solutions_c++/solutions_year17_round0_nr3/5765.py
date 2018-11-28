#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <unistd.h>
#include <vector>
#include <set>

using namespace std;

/* #define DEBUG */
// #define PRINT

//#define PARANOID

#define MAX(a, b) (((a)>(b))?(a):(b))
#define MIN(a, b) (((a)<(b))?(a):(b))

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


struct Stall
{
	bool occupied;
	int ls;
	int rs;
	int index;

	bool operator< (const Stall& rhs) const
	{
		const Stall& lhs = *this;
		if (MAX(lhs.ls, lhs.rs) != MAX(rhs.ls, rhs.rs))
		{
			return MAX(lhs.ls, lhs.rs) > MAX(rhs.ls, rhs.rs);
		} else {
			return lhs.index < rhs.index;
		}
	}
};
void getSolution (int N, int K, int& min, int& max)
{
	vector<Stall> v;
	for (int i = 0; i < N; ++i)
	{
		Stall s;
		s.occupied = false;
		s.ls = 0;
		s.rs = 0;
		s.index = i;
		v.push_back(s);
	}
	while (K)
	{
		for (int i = 0; i < N; ++i)
		{
			if (!v[i].occupied)
			{
				v[i].ls = 0;
				for (int j = i-1; j >=0; --j)
				{
					if (!v[j].occupied)
					{
						++v[i].ls;
					} else {
						break;
					}
				}
				v[i].rs = 0;
				for (int j = i+1; j < N; ++j)
				{
					if (!v[j].occupied)
					{
						++v[i].rs;
					} else {
						break;
					}
				}
			}
		}

		int max_minLSRS = 0;
		for (int i = 0; i < N; ++i)
		{
			int min = MIN(v[i].ls, v[i].rs);
			if (!v[i].occupied && min > max_minLSRS)
			{
				max_minLSRS = min;
			}
		}

		set<Stall> maxSet;
		for (int i = 0; i < N; ++i)
		{
			int min = MIN(v[i].ls, v[i].rs);
			if (!v[i].occupied && min == max_minLSRS)
			{
				maxSet.insert(v[i]);
			}
		}

		Stall& first = v[maxSet.begin()->index];
		min = MIN(first.ls, first.rs);
		max = MAX(first.ls, first.rs);
		first.occupied = true;
		--K;
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
        size_t N = getNumberFromDigits(digits);
        cursor = getNextNumberDigits(buffer, sizeof(buffer), cursor, digits);
        if (cursor >= sizeof(buffer))
        {
            fprintf (stderr, "cannot find next Number!\n");
            return 0;
        }
        size_t K = getNumberFromDigits(digits);

        fprintf(stderr, "\nN=%lu K=%lu\n", N, K);

        int min, max;
        getSolution (N, K, min, max);

        vector<size_t> segments;
        segments.push_back(N);

        size_t current = 0;
    	size_t left, right;
        while (K)
        {
        	size_t l = segments[current];
        	size_t h = l/2;
			if (l%2 == 1)
        	{
				left = h;
        		right = h;
        	} else {
        		if (h > 0)
        		{
        			right = h-1;
        		}
				left = h;
        	}

			fprintf(stderr, "%lu -> %lu|%lu\n", l, left, right);

    		if (left > 0)
    		{
    			segments.push_back(left);
    		}
    		if (right > 0)
			{
    			segments.push_back(right);
			}
        	--K;
        	++current;
        }
        //fprintf (stderr, "Case #%d: %lu %lu\n", (int)(t+1), MAX(left, right), MIN(left, right));
        //fprintf (stdout, "Case #%d: %lu %lu\n", (int)(t+1), MAX(left, right), MIN(left, right));
        fprintf (stdout, "Case #%d: %d %d\n", (int)(t+1), max, min);
    }
}
