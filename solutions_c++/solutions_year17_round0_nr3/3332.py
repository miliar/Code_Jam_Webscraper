#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<fstream>
#include <string>
#include <set>
#include <map>
using namespace std;
typedef struct node
{
	int data;
	node * left;
	node * right;
}node;
void insertIt(node * root, int value)
{
	if (value > root->data)
	{
		if (root->right != NULL)
		{
			insertIt(root->right, value);

		}
		else
		{
			root->right = new node;
			root->right->data = value;
			root->right->left = NULL;
			root->right->right = NULL;
		}
	}
	else
	{
		if (root->left != NULL)
		{
			insertIt(root->left, value);
		}
		else
		{
			root->left = new node;
			root->left->data = value;
			root->left->left = NULL;
			root->left->right = NULL;
		}
	}
}

node * insert(node * root, int value)
{
	node* therooot = root;
	insertIt(root, value);
	return therooot;
}
int checkNumber(string S)
{
	int length = S.length();
	int *arr = new int[length];
	for (int i = 0; i < length; i++)
	{
		arr[i] = S[i] - '0';
	}
	for (int i = 1; i < length; i++)
	{
		if (arr[i] >= arr[i - 1])
			continue;
		else
		{
			delete[]arr;
			return i;
		}
	}
	delete[]arr;
	return -1;
}
int main()
{
	ifstream cin("C-large.in", ios::in);
	ofstream cout("output.out", ios::out);
	int testCases;
	cin >> testCases;
	for (int x = 0; x < testCases; x++)
	{
		unsigned long long n, k;
		cin >> n >> k;

		unsigned long long v = n - (n - k);
		unsigned long long treeLevel = 0;
		unsigned long long temp = 1;
		unsigned long long Sum = 1;
		unsigned long long HowManyNumbBeforeThisLevel = n;
		while (v > Sum)
		{
			HowManyNumbBeforeThisLevel -= temp;
			temp *= 2;
			Sum += temp;
			//treeLevel++;
		}
		unsigned long long kNum = (k%temp);
		kNum++;
		unsigned long long templs = HowManyNumbBeforeThisLevel % temp;
		unsigned long long y;
		if (kNum <= templs)
		{
			y = HowManyNumbBeforeThisLevel / temp;
			if (y % 2 == 1)
				cout << "Case #" << (x + 1) << ": "  << (y / 2 + 1) << " " << y / 2 << endl;
			else
				cout << "Case #" << (x + 1) << ": "  << (y / 2) << " " << (y / 2) << endl;
		}
		else
		{
			y = (HowManyNumbBeforeThisLevel / temp) - 1;
			if (y % 2 == 1)
				cout << "Case #" << (x + 1) << ": " << (y / 2 + 1) << " " << y / 2 << endl;
			else
				cout << "Case #" << (x + 1) << ": " << (y / 2) << " " << (y / 2) << endl;
		}
	}
	return 0;
}

