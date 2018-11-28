// OB3LISK's C++ template for Google Code Jam.

#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <queue>

using namespace std;
typedef long long ll;
typedef long double ld;

// Do all the work for the code jam problem here.
// Write the answer to a test case.
////////////////////////////////////
#define filein "B-large.in"


template <class T>
inline std::string to_string (const T& t)
	{
    std::stringstream ss;
    ss << t;
    return ss.str();
	}


// Recursively make the number tidy.
string FindTidy(string n)
	{
	int min = 0;
	
	// Go through each digit of the number.
	for(int i = 0; i < n.length(); i++)
		{
		// The digit we're on.
		int digit = n[i] - '0';
		if(min <= digit)
			{
			min = digit;
			}
		// We found a violation.
		else
			{
			// If the violation is digit 1 and 2, make the new number 99999s
			if(i == 1 && n[0] == '1')
				{
				string ss = "";
				for(int j = 0; j < n.length() - 1; j++)
					{
					ss += '9';
					}
				return ss;
				}

			// If the violating digit is 0, make it a 9.
			n[i] = '9';
			// Reduce the other digit by 1.
			n[i-1] = static_cast<char>(n[i-1]-1);
			// Make the rest 9s
			for(int j = i+1; j < n.length(); j++)
				{
				n[j] = '9';
				}
			return FindTidy(n);
			}
		}
	
	return n;
	}

void solve()
    {
	
    	///////////////////
    	// Read number
    	string n; cin >> n;
    	
    	// Single digit default.
    	if(n.length() == 1) { cout << n; return; }
    	
	// Find the min
    	string ans = FindTidy(n);
    	
    	// Output answer
    	cout << ans;
    	///////////////////
    }
////////////////////////////////////

// Program begins here. Handles writing "Case #: "
int main()
    {
    freopen(filein, "r", stdin);
    freopen("B.out", "w", stdout);

    int tt; cin >> tt;
    for(int t = 1; t <= tt; t++)
        {
        cout << "Case #" << t << ": ";
        solve();
        if(t != tt) { cout << "\n"; }
        }
    return 0;
    }
