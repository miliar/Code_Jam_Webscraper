#include <stdio.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <thread>
#include <mutex>

using namespace std;

std::mutex checked_mutex,
	depthfound_mutex;

template<typename Out>
void split(const std::string &s, char delim, Out result) {
		std::stringstream ss;
		ss.str(s);
		std::string item;
		while (std::getline(ss, item, delim)) {
				*(result++) = item;
		}
}

vector<string> split(const string &s, char delim) {
	vector<string> elems;
	split(s, delim, back_inserter(elems));
	return elems;
}

void flip(string p, int index, int m, int depth, map<string, map<int, vector<int>>>* checked, vector<int>* founddepth) {
	// If we've already found a match at a less depth abort!
	for(int found: *founddepth) {
		if(depth >= found) {
			return;
		}
	}

	// Return 0 flips if all pancakes are upside right without flipping
	if(p.find('-') == string::npos) {
		depthfound_mutex.lock();
		founddepth->push_back(depth);
		depthfound_mutex.unlock();
		return;
	}

	++depth;

	// If we've already checked flipping this sequence at this index return -1 since the other will find it if it is succesful
	try {
		map<string, map<int, vector<int>>>::iterator mapelement = checked->find(p);
		if(mapelement != checked->end()) {
			map<int, vector<int>>::iterator indexfound = checked->at(p).find(index);
			if (indexfound != checked->at(p).end()) {
				for(int i = 0; i < indexfound->second.size(); ++i) {
					if(indexfound->second.at(i) <= depth) {
						return;
					}
				}
			}
		}
	} catch (const exception& e) {

	}

	// Add this sequence and index to the checked map
	checked_mutex.lock();
	(*checked)[p][index].push_back(depth);
	checked_mutex.unlock();

	// Flip the pancakes
	for(int i = 0; i < m; ++i) {
		p[index + i] = (p[index + i] == '-' ? '+' : '-');
	}

	// Return 1 flips if all pancakes are upside right
	if(p.find('-') == string::npos) {
		depthfound_mutex.lock();
		founddepth->push_back(depth);
		depthfound_mutex.unlock();
		return;
	}

	thread ts[p.size() - (m-1)];

	for(int i = 0; i < p.size() - (m-1); ++i) {
		ts[i] = thread(flip, p, i, m, depth, checked, founddepth);
	}

	for(int i = 0; i < p.size() - (m-1); ++i) {
		ts[i].join();
	}
}

int main(void) {
	string tmpin;
	getline(cin, tmpin);

	int count = stoi(tmpin);

	for(int x = 0; x < count; ++x) {
		string line;
		getline(cin, line);

		vector<string> s = split(line, ' ');

		string p = s[0];
		int m = stoi(s[1]);

		// Keep track of the pancake layout and indexes flipped
		map<string, map<int, vector<int>>> checked;
		vector<int> founddepth;

		// Begin bruteforcing, breadth-first threaded bruteforcing xP
		/* int lowestflips = -1; */
		thread ts[p.size() - (m-1)];
		for(int i = 0; i < p.size() - (m-1); ++i) {
			ts[i] = thread(flip, p, i, m, 0, &checked, &founddepth);
		}

		for(int i = 0; i < p.size() - (m-1); ++i) {
			ts[i].join();
		}

		int closest = -1;
		for(int found: founddepth) {
			if(closest == -1
					|| found < closest) {
				closest = found;
			}
		}

		cout << "Case #" << x + 1 << ": "
				 << (closest < 0 ? "IMPOSSIBLE" : to_string(closest))
				 << endl;
	}

	return 0;
}
