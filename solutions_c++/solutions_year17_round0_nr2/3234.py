#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<fstream>
#include <string>
#include <set>
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
	string line;
	ifstream inFile("B-large.in", ios::in);
	ofstream outFile("output.out", ios::out);
	int testCases;
	inFile >> testCases;
	for (int x = 0; x < testCases; x++)
	{
		string s;
		inFile >> s;
		string out = "";
		while (true)
		{
			int index = checkNumber(s);
			if (index == -1)
			{
				outFile << "Case #" << (x + 1) << ": ";
				for (int i = 0; i < s.length(); i++)
				{
					if (s[i] == '0')
						continue;
					else
						outFile << s[i];
				}
				outFile << endl;
				break;
			}
			else
			{
				s[index - 1] = s[index - 1]--;
				for (int i = index; i < s.length(); i++)
				{
					s[i] = '9';
				}
			}
		}
	}
	return 0;
}

