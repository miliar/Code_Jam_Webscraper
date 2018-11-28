#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

#define LARGE	0
#define SMALL_1	1
#define SMALL_2	2
#define TEST	3

#define FILE SMALL_1

#if FILE == SMALL_1
#define IN_FILE "C-small-1-attempt4.in"
#define OUT_FILE "C-small-1-attempt4.out"
#define N 1000
#elif FILE == SMALL_2
#define IN_FILE "C-small-2.in"
#define OUT_FILE "C-small-2.out"
#define N pow(10, 6)
#elif FILE == LARGE
#define IN_FILE "B-large.in"
#define OUT_FILE "B-large.out"
#define N pow(10, 18)
#elif FILE == TEST
#define IN_FILE "test.in"
#define OUT_FILE "test.out"
#define N 1000
#endif

unsigned long long c_k = 0;
void solve(unsigned long long n, unsigned long long k, unsigned long long * nr, unsigned long long * kr);



// C program to demonstrate delete operation in binary search tree
#include<stdio.h>
#include<stdlib.h>

struct node
{
	int key;
	struct node *left, *right;
};

// A utility function to create a new BST node
struct node *newNode(int item)
{
	struct node *temp = (struct node *)malloc(sizeof(struct node));
	temp->key = item;
	temp->left = temp->right = NULL;
	return temp;
}

// A utility function to do inorder traversal of BST
void inorder(struct node *root)
{
	if (root != NULL)
	{
		inorder(root->left);
		printf("%d ", root->key);
		inorder(root->right);
	}
}

/* A utility function to insert a new node with given key in BST */
struct node* insert(struct node* node, int key)
{
	/* If the tree is empty, return a new node */
	if (node == NULL) return newNode(key);

	/* Otherwise, recur down the tree */
	if (key < node->key)
		node->left = insert(node->left, key);
	else
		node->right = insert(node->right, key);

	/* return the (unchanged) node pointer */
	return node;
}

/* Given a non-empty binary search tree, return the node with minimum
key value found in that tree. Note that the entire tree does not
need to be searched. */
struct node * minValueNode(struct node* node)
{
	struct node* current = node;

	/* loop down to find the leftmost leaf */
	while (current->left != NULL)
		current = current->left;

	return current;
}

/* Given a binary search tree and a key, this function deletes the key
and returns the new root */
struct node* deleteNode(struct node* root, int key)
{
	// base case
	if (root == NULL) return root;

	// If the key to be deleted is smaller than the root's key,
	// then it lies in left subtree
	if (key < root->key)
		root->left = deleteNode(root->left, key);

	// If the key to be deleted is greater than the root's key,
	// then it lies in right subtree
	else if (key > root->key)
		root->right = deleteNode(root->right, key);

	// if key is same as root's key, then This is the node
	// to be deleted
	else
	{
		// node with only one child or no child
		if (root->left == NULL)
		{
			struct node *temp = root->right;
			free(root);
			return temp;
		}
		else if (root->right == NULL)
		{
			struct node *temp = root->left;
			free(root);
			return temp;
		}

		// node with two children: Get the inorder successor (smallest
		// in the right subtree)
		struct node* temp = minValueNode(root->right);

		// Copy the inorder successor's content to this node
		root->key = temp->key;

		// Delete the inorder successor
		root->right = deleteNode(root->right, temp->key);
	}
	return root;
}

struct node *root = NULL;
void solve2(unsigned long long n, unsigned long long k, unsigned long long * nr, unsigned long long * kr);
int main()
{
	unsigned int num_tc, cur_tc;
	unsigned long long n = 0, k = 0;
	unsigned long long nr, kr; 

	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	scanf("%d\n", &num_tc);	//number of test cases

	for (cur_tc = 0; cur_tc < num_tc; cur_tc++)
	{
		root = NULL;
		printf("Case #%d: ", cur_tc + 1);
		scanf("%lld %lld", &n, &k);
		c_k = k;
		root = insert(root, n);
		solve2(n, k, &nr, &kr);
		printf("%lld", nr);
		printf(" %lld", kr);
		printf("\n");
	}
}

void solve2(unsigned long long n, unsigned long long k, unsigned long long * nr, unsigned long long * kr)
{
	k--;	// one person entered
	*nr = (n + 0.5) / 2;	// two new leafs
	*kr = (n - 0.5) / 2;	// two new leafs
	if (k == 0)
		return;
	root = deleteNode(root, n);
	root = insert(root, *nr);
	root = insert(root, *kr);
	solve2(root->key, k, nr, kr);
}

unsigned long long find_pow_2(unsigned long long k)
{
	unsigned long long i=0;
	while (pow(2, i) < k)
	{
		i++;
	}
	return i;
}

void solve(unsigned long long n, unsigned long long k, unsigned long long * nr, unsigned long long * kr)
{
	unsigned int nr_val = 0;
	unsigned int kr_val = 0;


	if (k > 0)
	{
		k--;
		if (k == 0)
		{
			*nr = (n+0.5) / 2;
			*kr = (n-0.5) / 2;
			return;
		}

		if (c_k % 2 == 0)	// original k is even ?
		{
			solve(((n + 0.5) / 2), --k, nr, kr);	//left
			nr_val = *nr;
			kr_val = *kr;
		}
		else
		{
			solve(((n - 0.5) / 2), --k, nr, kr);	//left
			nr_val = *nr;
			kr_val = *kr;
		}
	}
	else
	{
		*nr = (n + 0.5) / 2;
		*kr = (n - 0.5) / 2;
	}

	return;
}