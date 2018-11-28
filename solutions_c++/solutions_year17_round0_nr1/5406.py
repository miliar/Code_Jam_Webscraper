// OB3LISK's C++ template for Google Code Jam.
// Make g++ -std=c++0x a.cpp
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <unordered_map>
#include <map>
#include <cstdio>
#include <queue>

using namespace std;
typedef long long ll;
typedef long double ld;

// Do all the work for the code jam problem here.
// Write the answer to a test case.
#define filein "A-small-attempt0.in"
void solve()
    {
    	// Get input
    	string s; cin >> s;
	int n = s.length();
	int k; cin >> k;
	
	// Create string that represents perfect stack
	string perfect = "";
	for(int i = 0; i < n; i++)
		{
		perfect += '+';
		}

	// A struct that holds the pancakes string and the min
	struct Node
		{
		string p;
		int min;
		Node(string pp, int mmin) : p(pp), min(mmin) {}
		};

	// Create a queue for the pancake sets we check
	queue<Node> q;
	
	// Create a vector for the pancake sets we already did
	vector<string> alreadyDid;
	
	q.push(Node(s, 0));
	alreadyDid.push_back(s);
	
	// While we still have pancake sets unchecked.
	while(!q.empty())
		{
		// The top of our queue.
		Node node = q.front();
		q.pop();
		string pancakes = node.p;
		int min = node.min;
		
		//cout << "pancakes: " << pancakes << " min: " << min << endl;
		
		// Check if pancakes is perfect. If so we can stop.
		if(pancakes == perfect) { cout << min; return;}
		
		// A vector to hold the items we're going to push onto the queue.
		vector<string> addNext;
		
		// Try all orientations of flipping this set of pancakes.
		for(int i = 0; i <= n-k; i++)
			{
			// This will be the string we work with for this iteration.
			string p = pancakes;
	
			// Edit the set at this index by flipping the next k pancakes.
			for(int j = 0; j < k; j++)
				{
				if(p[i+j] == '+') { p[i+j] = '-'; }
				else { p[i+j] = '+'; }
				}
			
			// Check if perfect
			if(p == perfect) { cout << min + 1; return; }
			
			// Check if we did this pancake yet.
			bool did = false;
			for(int j = 0; j < alreadyDid.size(); j++)
				{
				if(alreadyDid[j] == p)
					{ did = true; break; }
				}
			
			if(did == true) { continue; }
			
			// Add this pancake set to our queue list and as already did.
			addNext.push_back(p);
			alreadyDid.push_back(p);
			} 
		
		// Add the new pancake sets to the queue and increment the min.
		for(int i = 0; i < addNext.size(); i++)
			{
			q.push(Node(addNext[i], min+1));
			}
		}
	
	// Output default impossible
	cout << "IMPOSSIBLE";
	
    }

// Program begins here. Handles writing "Case #: "
int main()
    {
    // Handle reading and writing to file.
    freopen(filein, "r", stdin);
    //freopen("A-large-practice.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int tt; cin >> tt; string s; getline(cin, s);
    for(int t = 1; t <= tt; t++)
        {
        cout << "Case #" << t << ": ";
        solve();
        if(t != tt) { cout << "\n"; }
        }
    return 0;
    }
