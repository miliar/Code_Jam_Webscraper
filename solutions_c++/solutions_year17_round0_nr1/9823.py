#include <iostream>
#include <string>
#include <map>
#include <queue>

using namespace std;

void flip(string &cakes, int start, int end);

int flipable(string &cakes, int start, int end);

int search(map<string, int> &memory, string &cakes, int k, int depth);

bool all_happy(string &cakes, int start, int end);

bool all_unhappy(string &cakes, int start, int end);

int _max(int a, int b);

int _min(int a, int b);

void flip(char &a);

struct WeightedNode {

public:
	
	double weight;

	int start;

	int end;
};

struct Comparison
{

	bool operator() (const WeightedNode& node1, const WeightedNode&node2) const
	{
		return (node1.weight < node2.weight);
	}
};

int main() {

	int t, k;

	string pancakes = "";

	cin >> t;

	map<string, int> strings;

	for (int i = 0; i < t; ++i) {
		
		cin >> pancakes;

		cin >> k;

		strings.clear();

		int flips = search(strings, pancakes, k, 0);
		
		if (flips >= 0)
			cout << "Case #" << (i + 1) << ": "<< flips << endl;
		else
			cout << "Case #" << (i + 1) << ": "<< "IMPOSSIBLE" << endl;
	}

	return 0;
}

void flip(string &cakes, int start, int end) {

	int length = cakes.length();

	end = _min(length, end);

	start = _max(0, start);

	for (start; start < end; ++start) {

		flip(cakes[start]);
	}
}

int flipable(string &cakes,int start, int end) {

	int score = 0;

	int length = cakes.length();

	end = _min(length, end);

	start = _max(0, start);

	char start_char = cakes[start];

	char end_char = cakes[end - 1];
	
	--start; // check start neighbor

	if (start >= 0) {

		if (start_char != cakes[start])
			score += 2;
		else
			--score;
	}
		
	if (end < length) {

		if (end_char != cakes[end])
			score += 2;
		else
			--score;
	}
		
	return score;
}

int _max(int a, int b) {

	if (a > b) 
		return a;
	else
		return b;
}

int _min(int a, int b) {

	if (a < b)
		return a;
	else
		return b;
}

bool all_happy(string &cakes, int start, int end) {

	int length = cakes.length();

	end = _min(length, end);

	start = _max(0, start);

	for (start; start < end; ++start) {

		if (cakes[start] == '-')
			return false;	 
	}
	
	return true;
}

bool all_unhappy(string &cakes, int start, int end) {

	int length = cakes.length();

	end = _min(length, end);

	start = _max(0, start);

	for (start; start < end; ++start) {

		if (cakes[start] == '+')
			return false;
	}

	return true;
}

void flip(char &a) {

	if (a == '-')
		a = '+';
	else
		a = '-';
}

int search(map<string, int> &memory, string &cakes, int k, int depth) {

	int length = cakes.length();

	if (all_unhappy(cakes, 0, length)) {

		if (length % k == 0) {

			int s = length / k;

			flip(cakes, 0, k*s);

			return s + depth;
		}
		else
			return -1;
	}

	if(all_happy(cakes, 0, length))
		return depth;
	else {

		map<string, int>::iterator itr = memory.find(cakes);

		if (memory.find(cakes) != memory.end()) {

			if (depth < itr->second)
				itr->second = depth;
			else
				return -1;
		}
	}
		
	memory[cakes] = depth;

	int min_depth = -1;

	int d;

	priority_queue<WeightedNode, vector<WeightedNode>, Comparison> p_queue;

	WeightedNode node;

	node.start = 0;

	node.end = k;

	for (; node.end <= length; ++node.end, ++node.start) {

		node.weight = flipable(cakes, node.start, node.end);

		if(node.weight >= 0)
		  p_queue.push(node);
	}

	while (!p_queue.empty()) {

		const WeightedNode &n = p_queue.top();

		string temp = cakes;

		flip(temp, n.start, n.end);

		p_queue.pop();

		d = search(memory, temp, k, depth + 1);

		if (d != -1) {

			if (min_depth == -1)
				min_depth = d;
			else
				min_depth = _min(d, min_depth);
		}
	}

	return min_depth;
}