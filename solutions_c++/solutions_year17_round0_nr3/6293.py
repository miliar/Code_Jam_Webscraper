#include <iostream>
#include <vector>

#define ull unsigned long long

using namespace std;

struct Node {
	ull index, left_weight, right_weight, total_weight;
};

Node *build_tree(ull min, ull max, vector<Node *> *nodes) {
	if (max - min == 1 || max == 0) {
		return NULL;
	}
	Node *root = new Node;
	ull index = min + (max - min) / 2;
	root->index = index;
	Node *left_child = build_tree(min, index, nodes);
	ull left_weight = (left_child == NULL) ? 0 : left_child->total_weight + 1;
	root->left_weight = left_weight;
	Node *right_child = build_tree(index, max, nodes);
	ull right_weight = (right_child == NULL) ? 0 : right_child->total_weight + 1;
	root->right_weight = right_weight;
	ull total_weight = root->left_weight + root->right_weight;
	root->total_weight = total_weight;
	nodes->push_back(root);
	return root;
}

int main() {
	int num_test_cases;
	scanf("%d", &num_test_cases);
	for (int t = 1; t <= num_test_cases; t++) {
		ull n, k;
		scanf("%llu %llu", &n, &k);
		vector<Node *> nodes;
		Node *root = new Node;
		root->index = (n + 1) / 2;
		Node *left_child = build_tree(0, root->index, &nodes);
		root->left_weight = (left_child == NULL) ? 0 : left_child->total_weight + 1;
		Node *right_child = build_tree(root->index, n + 1, &nodes);
		root->right_weight = (right_child == NULL) ? 0 : right_child->total_weight + 1;
		root->total_weight = root->left_weight + root->right_weight;
		nodes.push_back(root);
		sort(begin(nodes), end(nodes), [](Node *a, Node *b) -> int {
			if (a->total_weight == b->total_weight) {
				return a->index < b->index;
			} else {
				return a->total_weight > b->total_weight;
			}
		});
		k--;
		ull max = (nodes[k]->right_weight > nodes[k]->left_weight) ? nodes[k]->right_weight : nodes[k]->left_weight;
		ull min = (nodes[k]->right_weight < nodes[k]->left_weight) ? nodes[k]->right_weight : nodes[k]->left_weight;
		printf("Case #%d: %llu %llu\n", t, max, min);
		for (int i = 0; i < n; i++) {
			delete (nodes[i]);
		}
	}
	return 0;
}

