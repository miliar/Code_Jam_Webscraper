#include<iostream>
#include<cstdio>
using namespace std;
int main()
{

}

node* bst1(node* root, int val)
{
	if(root==NULL || root->val == val)
	{
		return root;
	}
	if(val < root->val)
	{
		bst1(root->left, val);
	}
	else
	{
		bst1(root->right, val);
	}

}


node* bst2(node* root, int val)
{
	while(root!=NULL && root->val != val)
	{
		if(val < root->val)
		{
			root=root->left;
		}
		else
		{
			root=root->right;
		}
	}
	return root;
}

