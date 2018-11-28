// Example program
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

class Node {
public:
	long first;
	long second;
	Node * next;
	Node(long f, long s) {
		first = f;
		second = s;
		next = NULL;
	}


};

class PQ {
public:
	Node * root;

	PQ(Node *node) {
		root = node;
	}

	void push(long first, long second) {
		if (root == NULL) {
			Node * n = new Node(first, second);
			root = n;
			return;
		}
		else if (root->first == first) {
			root->second += second;
			return;
		}
		else if (root->first < first) {
			Node * n = new Node(first, second);
			n->next = root;
			root = n;
			return;
		}

		Node* curr = root;
		while (curr != NULL) {
			if (first == curr->first) {
				curr->second += second;
				return;
			}
			else if (curr->next == NULL || curr->next->first < first) {
				Node * node = new Node(first, second);
				node->next = curr->next;
				curr->next = node;
				return;
			}
			curr = curr->next;
		}
	}

	Node* top() {
		return root;
	}

	void pop() {
		Node * prev = root;
		root = root->next;
		delete prev;	
	}

	void print() {
		Node *curr = root;
		cout << "PQ: ";
		while (curr != NULL) {
			cout << "(" << curr->first << ", " << curr->second << ") --> ";
			curr = curr->next;
		}
		cout << endl;
	}
};


void fill(PQ & pq, long & k) {
	Node* p = pq.top();
	long n = p->first;
	long count = p->second;
	// long n = pq.top().first;
	// int count = pq.top().second;
	k -= count;
	if (k <= 0) {
		return;
	}
	pq.pop();
	if (n%2 == 0) {
		pq.push((n-1)/2, count);
		pq.push(n/2, count);         // CANT DOUBLE HERE. REWRITE.    NEED CUSTOM CLASS PRIORITY QUEUE, CHECK FOR DUPLICATE VALUES OF COUNT (then just add to the value of count, instead of adding a new queue node).
	}
	else {
		pq.push(n/2, count*2);
	}
}

// void print(priority_queue<pair<long, int>> pq, long k) {
	// cout << "pq.top()=" << pq.top() << " k=" << k << " pq.size()=" << pq.size() << "." << endl;
// }

int main() {

	int t;
	cin >> t;
	for (int x = 0; x < t; x++) {
		long n, k; // n + 2 stalls, ends occupied; k people enter
		cin >> n >> k;

		// implement priority queue

		Node * node = new Node(n, 1);
		PQ pq(node);
        while (k > 0) {
        	// cout << "k=" << k << "   ";
        	// pq.print();
        	fill(pq, k);
        	// print(pq, k);
        }
        long min, max, sol;
        sol = pq.top()->first;
        if (sol%2 == 0) {
        	min = sol/2 - 1;
        	max=  sol/2;
        }
        else {
        	min = sol/2;
        	max = sol/2;
        }

		cout << "Case #" << (x+1) << ": " << max << " " << min << endl;
	}
}

