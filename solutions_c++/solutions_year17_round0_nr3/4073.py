#include <iostream>
#include <map>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;

typedef struct p {
  int val;
  struct p *left, *right;
} node;

bool cmpFunc(node *i, node *j){
  return i->val>j->val;
}

node *createT(map<int, node*> &tree, int val) {
  if(val <= 0) return NULL;
  map<int, node*>::iterator it = tree.find(val);
  if(it != tree.end()) return it->second;
  node *res = (node *) malloc(sizeof(node));
  res->val = val;
  int L = ceil(val/2.0) - 1;
  int R = val - L - 1;
  res->left = createT(tree, L);
  res->right = createT(tree, R);
  tree[val] = res;
}

void getLastLevel(map<int, int> &lastLevel, node *n, int s) {
  if(n == NULL) return;
  if(s == 0) {
    if(lastLevel.find(n->val) == lastLevel.end()) lastLevel[n->val] = 0;
    lastLevel[n->val]++;
  } else {
    getLastLevel(lastLevel, n->left, s-1);
    getLastLevel(lastLevel, n->right, s-1);
  }
}

int maxKey(map<int, int> &t) {
  int max=-1;
  for(map<int, int>::iterator it = t.begin(); it != t.end(); it++) {
    if(it->first > max) max = it->first;
  }
  return max;
}

int main() {
	int t;
	cin >> t;
  map<int, node*> tree;
  node *res = (node *) malloc(sizeof(node));
  res->val = 1;
  res->left = NULL;
  res->right = NULL;
  tree[1] = res;
  tree[0] = NULL;
	for(int caseCount = 1; caseCount <= t; caseCount++) {
	   int n,k,s=0;
	   cin >> n >> k;
     //build tree
     createT(tree, n);
     while(pow(2,s) - 1 < k) {
       s++;
     }
     s--;
     int noDel = pow(2,s) - 1;
     map<int, int> lastLevel;
     getLastLevel(lastLevel, tree[n], s);
    //  queue.push_back(tree[n]);
    //  while(noDel > 0) {
    //    node *temp = queue.front();
    //    queue.erase(queue.begin());
    //    if(temp->left != NULL)
    //      queue.push_back(temp->left);
    //    if(temp->right != NULL)
    //      queue.push_back(temp->right);
    //    k--;
    //    noDel--;
    //  }

    //  sort(queue.begin(), queue.end(), cmpFunc);
     int val=0;
     k -= noDel;
     while(k > 0) {
       int key = maxKey(lastLevel);
       if(lastLevel[key] >= k) {
         val = key;
         break;
       }
       k-=lastLevel[key];
       lastLevel.erase(lastLevel.find(key));
     }
    //  while(k > 0 && queue.size() != 0) {
    //    val = queue.front()->val;
    //    queue.erase(queue.begin());
    //    k--;
    //  }
     int L = ceil(val/2.0) - 1;
     int R = val - L - 1;
	   cout << "Case #" << caseCount << ": " << max(L,R) << " " << min(L,R) << endl;
	}
	return 0;
}
