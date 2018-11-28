#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

struct Node{
    int length;
    Node *l, *r;
    int minValue, maxValue;

    Node(int len)
    {
        length = len;
        l = r = NULL;
        if (len & 1)
        {
            minValue = maxValue = (len - 1) / 2;
        }
        else
        {
            maxValue = len / 2;
            minValue = maxValue - 1;
        }
    }
    
    ~Node()
    {
        if (l != NULL)
            delete l;
        if (r != NULL)
            delete r;
    }
};

bool isBetter(Node *v, Node *u)
{
    return v->minValue > u->minValue || v->minValue == u->minValue && v->maxValue > u->maxValue;
}

void update(Node *node)
{
    if (isBetter(node->r, node->l))
    {
        node->minValue = node->r->minValue;
        node->maxValue = node->r->maxValue;
    }
    else
    {
        node->minValue = node->l->minValue;
        node->maxValue = node->l->maxValue;
    }
}

void insert(Node *node)
{
    if (node->l == NULL)
    {
        if (node->length & 1)
        {
            node->l = new Node(node->length / 2);
            node->r = new Node(node->length / 2);
        }
        else
        {
            node->l = new Node(node->length / 2 - 1);
            node->r = new Node(node->length / 2);
        }
        update(node);
        return;
    }
    if (isBetter(node->r, node->l))
    {
        insert(node->r);
    }
    else
    {
        insert(node->l);
    }
    update(node);
}

Node *root;
int ansMin, ansMax;

void solve(int n, int k)
{
    root = new Node(n);
    for (int i = 0; i < k - 1; ++i)
    {
        insert(root);
    }
    ansMin = root->minValue;
    ansMax = root->maxValue;
    delete root;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tn = 1; tn <= t; ++tn)
    {
        int n, k;
        scanf("%d%d", &n, &k);
        solve(n, k);
        printf("Case #%d: %d %d\n", tn, ansMax, ansMin);
    }
    return 0;
}