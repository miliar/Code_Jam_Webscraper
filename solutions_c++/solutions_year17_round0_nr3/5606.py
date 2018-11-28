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
#include <cstdio>
#include <queue>

using namespace std;
typedef long long ll;
typedef long double ld;

// Do all the work for the code jam problem here.
// Write the answer to a test case.
#define filein "C-small-2-attempt1.in"
void solve()
    	{
    	// Get input.
	long n, k;
	cin >> n >> k;

	// Default case where stalls are over half full.
	//if( (n+1)/2 + 1 <= k  ) { cout << "0 0"; return;}

		
	// Keep a vector that holds the size of each partition we have left.
	//vector<long> parts;
	priority_queue<long> q;
	// Add the first partition.
	//parts.push_back(n);
	q.push(n);
	
	// Go through each person.
	for(long i = 0; i < k; i++)
		{
		// Sort the vector. 
		//sort(parts.begin(), parts.end());

		// Pick the last item (the one with the biggest size).
		//int m = parts.size() - 1;
		//int size = parts[m];

		// The max partition is always on top.
		//long size = parts[0];
		//long size = q.front();
		long size = q.top();

		// Remove that item from the vector.
		//parts.erase(parts.begin());
		q.pop();
		
		// If the size is zero then we only have 0 0 stalls left
		if(size == 0) { cout << 0 << " " << 0; return; }
		
		// Divide this new size into two.
		// If even
		if(size % 2 == 0)
			{
			// Add one less than half, and half.
			//parts.push_back(size/2);
			//parts.push_back((size/2) - 1);
			q.push(size/2);
			q.push(size/2 - 1);

			//if(t == 6) { cout << size << " -> " << size/2 << " " << size/2 - 1 << endl; }
			/*
			int value1 = (size/2) - 1;
			auto it = upper_bound(parts.begin(), parts.end(), value1);
			parts.insert(it, value1);
			
			int value2 = (size/2);
			auto it1 = upper_bound(parts.begin(), parts.end(), value2);
			parts.insert(it1, value2);
			*/
			}
		// If odd
		else
			{
			//parts.push_back((size)/2);
			//parts.push_back((size)/2);
			q.push(size/2);
			q.push(size/2);
			//if(t == 6) { cout << size << " -> " << size/2 << " " << (size/2) << endl; }
			/*
			int value2 = (size/2);
			auto it = upper_bound(parts.begin(), parts.end(), value2);
			parts.insert(it, value2);
			parts.insert(it, value2);
			*/
			}			
			
		// If we're at the last k, just output the answer.
		if(i == k-1)
			{
			//cout << size;
			
			// If even
			if(size % 2 == 0)
				{
				cout << (size/2)  << " " << (size/2) - 1;	
				}
			// if odd
			else
				{
				cout << (size/2)  << " " << (size/2);
				}			
			
			}
		
		}

  	} // End of void solve

// Program begins here. Handles writing "Case #: "
int main()
    {
    // Handle reading and writing to file.
    freopen(filein, "r", stdin);
    //freopen("C-large-practice.in", "r", stdin);
    freopen("C.out", "w", stdout);

    int tt; cin >> tt;
    for(int t = 1; t <= tt; t++)
        {
        cout << "Case #" << t << ": ";
        solve();
        if(t != tt) { cout << "\n"; }
        }
    return 0;
    }
