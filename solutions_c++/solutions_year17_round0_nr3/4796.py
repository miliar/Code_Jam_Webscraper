#include <iostream>
#include <fstream>
#include <limits.h>

using namespace std;

#define INF LONG_LONG_MAX

struct Node
{
    long long int key;
    struct Node *left;
    struct Node *right;
    long long int height;
    long long int amount;

    Node(const long long int& key)
    {
        this->key = key;
        this->left = NULL;
        this->right = NULL;
        this->height = 1;
        this->amount = 1;
    }
};

inline long long int height(Node *node)
{
    if (node)
        return node->height;
    return 0;
}

Node* rightRotate(Node *y)
{
    Node* x = y->left;
    Node* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left), height(y->right))+1;
    x->height = max(height(x->left), height(x->right))+1;

    return x;
}

Node* leftRotate(Node *x)
{
    Node *y = x->right;
    Node *T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left), height(x->right))+1;
    y->height = max(height(y->left), height(y->right))+1;

    return y;
}

long long int getBalance(Node *node)
{
    if (node)
        return height(node->left) - height(node->right);
    return 0;
}

Node* minValueNode(Node* node)
{
    Node* current = node;

    while (current->left != NULL)
        current = current->left;

    return current;
}

Node* insertNode(Node* node, long long int key)
{
    if (node == NULL)
        return new Node(key);

    if (key < node->key)
        node->left  = insertNode(node->left, key);
    else if (key > node->key)
        node->right = insertNode(node->right, key);
    else
    {
        node->amount++;
        return node;
    }

    node->height = 1 + max(height(node->left), height(node->right));

    long long int balance = getBalance(node);

    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    if (balance > 1 && key > node->left->key)
    {
        node->left =  leftRotate(node->left);
        return rightRotate(node);
    }

    if (balance < -1 && key < node->right->key)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

Node* deleteNode(Node* root, long long int key)
{
    if (root == NULL)
        return root;

    if ( key < root->key )
        root->left = deleteNode(root->left, key);
    else
    if( key > root->key )
        root->right = deleteNode(root->right, key);
    else
    {
        root->amount--;
        if(root->amount > 0)
            return root;

        if( (root->left == NULL) || (root->right == NULL) )
        {
            Node* temp = root->left ? root->left : root->right;

            if (temp == NULL)
            {
                temp = root;
                root = NULL;
            }
            else
             *root = *temp;

            delete temp;
        }
        else
        {
            Node* temp = minValueNode(root->right);

            root->key = temp->key;

            root->right = deleteNode(root->right, temp->key);
        }
    }

    if (root == NULL)
      return root;

    root->height = 1 + max(height(root->left),
                           height(root->right));

    long long int balance = getBalance(root);

    if (balance > 1 && getBalance(root->left) >= 0)
        return rightRotate(root);

    if (balance > 1 && getBalance(root->left) < 0)
    {
        root->left =  leftRotate(root->left);
        return rightRotate(root);
    }

    if (balance < -1 && getBalance(root->right) <= 0)
        return leftRotate(root);

    if (balance < -1 && getBalance(root->right) > 0)
    {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

Node* searchNode(Node* root, Node* lroot, long long int key)
{
    if(root == NULL)
        return lroot;

    if (root->key == key)
       return root;

    if (root->key < key)
       return searchNode(root->right, root,key);

    return searchNode(root->left, root, key);
}

int t;
long long int n, k;
Node* root = NULL;

int main()
{
    cout << "Hello world!" << endl;

    ifstream f("date.in");
    ofstream g("date.out");

    f >> t;
    for(int i = 1; i <= t; i++)
    {
        f >> n >> k;
        root = insertNode(root,n);

        for(long long int j = 1; j < k; j++)
        {
            int mx = searchNode(root, NULL,INF)->key;
            root = deleteNode(root, mx);
            if(mx % 2 == 0)
            {
                root = insertNode(root, mx/2-1);
                root = insertNode(root, mx/2);
            }
            else
            {
                root = insertNode(root, (mx-1)/2);
                root = insertNode(root, (mx-1)/2);
            }
        }
        long long int sol = searchNode(root, NULL,INF)->key;
        if(sol % 2 == 0)
            g << "Case #" << i << ": " << sol/2 << ' ' << sol/2-1 << '\n';
        else
            g << "Case #" << i << ": " << sol/2 << ' ' << sol/2 << '\n';
        root = NULL;
    }

    return 0;
}
