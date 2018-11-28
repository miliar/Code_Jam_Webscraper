#include<bits/stdc++.h> 
using namespace std;
struct  node{
	unsigned long long int key;
	long long int height;
	long long int size;
	node *left;
	node *right;
};

void swap(long long int *a, long long int *b)
{
	long long int t = *a; *a = *b; *b = t;
}

long long int max(long long int a, long long int b){
	return (a>b)?a:b;
}

node* createNode(long long int val)
{
	node *temp = new node();
	temp->key=val;
	temp->size=1;
	temp->height=0;
	temp->left=NULL;
	temp->right=NULL;
}

long long int Size(node *t)
{
	if(t==NULL)
		return 0;
	else
		return t->size;
}

long long int Height(node *t)
{
	if(t==NULL)
		return -1;
	else
		return t->height;
}

void updateHeightSize(node *t)
{
	t->height = max(Height(t->left),
			Height(t->right))+1;
	t->size = Size(t->left) + Size(t->right)+1;
}

node* insert(node *n, long long int key)
{
	if(n==NULL){
		n = createNode(key);
		return n;
	}
	if(n->left==NULL ||
			Size(n->left)<  int(pow(2, Height(n->left)+1))-1 ||
			Size(n->right)==Size(n->left)) 
		n->left = insert(n->left, key);
	else
		n->right = insert(n->right,key);

	if((n->left!=NULL && n->left->key > n->key) ||
			(n->right!=NULL && n->right->key>n->key)){
		if(n->left==NULL){
			swap(n->key, n->right->key);
		}
		else if(n->right==NULL)
			swap(n->key, n->left->key);
		else{
			if(n->left->key > n->right->key)
				swap(n->key, n->left->key);
			else
				swap(n->key, n->right->key);
		}
	}

	updateHeightSize(n);
	return n;
}

long long int top(node *root){
	return root->key;
}

void heapify(node *n)
{
	if(!n)
		return;
	while((n->left!=NULL && n->left->key>n->key) ||
			(n->right!=NULL && n->right->key>n->key)){
		if(n->left==NULL){
			swap(n->key, n->right->key);
			n = n->right;
		}
		else if(n->right==NULL){
			swap(n->key, n->left->key);
			n = n->left;
		}
		else{
			if(n->left->key > n->right->key){
				swap(n->key, n->left->key);
				n = n->left;
			}
			else{
				swap(n->key, n->right->key);
				n = n->right;
			}
		}
	}
}

node* remove(node *n, node *root)
{
	if(n==NULL)
		return NULL;
	if(n->left==NULL && n->right==NULL){
		swap(root->key, n->key);
		delete n;
		return NULL;
	}
	else if(Size(n->left) > Size(n->right))
		n->left = remove(n->left, root);
	else
		n->right = remove(n->right, root);

	updateHeightSize(n);
}

void pop(node **heap)
{
	*heap = remove(*heap, *heap);
	heapify(*heap);
}

void display(node *x)
{
	if(!x)
		return;
	display(x->left);
	cout<<x->key<<endl;    display(x->right);
}

int main()
{
	int t;
	cin >> t;
	for(int l=1;l<=t;l++)
	{
		node *heap=NULL;
		unsigned long long int n,k,g;
		cin >> n >> k;
		g=n;
		heap = insert(heap, g);
	//	k=k+1;
		k--;
		while(k--)
		{
			//	cout<<"Enter values to insert in heap. 0 to stop ";       cin>>x;
			unsigned long long p;
			p=g/2;
//			cout << "p= " << p << endl;
			if((g%2)==0)
			{
				heap=insert(heap,p);
				if(p>0)
				heap=insert(heap,p-1);
				else
				heap=insert(heap,p);

//				cout << "even\n" << endl;
			}
			else if((g%2)==1)
			{
				heap=insert(heap,p);
				heap=insert(heap,p);
//				cout << "odd\n" << endl;
			}
			pop(&heap);
			g=top(heap);
//		cout << g << endl;
			
		}
	long long p;
	p=g/2;

	if(g%2==0 && p!=0)
	cout << "Case #" << l << ": " << g/2 << " " <<  g/2-1 << endl;
	else
	cout << "Case #" << l << ": " << g/2 << " " <<  g/2 << endl;
	}//cout<<endl;
	return 0;
}
