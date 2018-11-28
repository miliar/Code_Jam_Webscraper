#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <complex>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

struct Node{
    Node* next;
    char color;
};

int T;
int N;
pair<int,char> c[6];
char colors[] = "ROYGBV";

Node *head = NULL;
Node *cur = NULL;
typedef Node* pNode;

void delete_linkedlist(pNode& head) {
    pNode p = head->next;
    pNode h = head;
    while(p != h) {
        delete h;
        h = p;
        p = h->next;
    }
    head = NULL;
}

void add_color(char c,int cnt) {
    for(int i = 0 ; i < cnt ; i++ ) {
        if( cur == NULL ) {
            cur = new Node;
            head = cur;
            cur->color = c;
            cur->next = cur;
        } else {
            pNode p = new Node;
            p->color = c;
            p->next = cur->next;
            cur->next = p;
            cur = p->next;
        }
    }
}

void display_list(pNode head) {
    pNode p = head->next;
    printf("%c",head->color);
    while(p!=head) {
        printf("%c",p->color);
        p = p->next;
    }
}

bool isValid(pNode head) {
    pNode p = head->next;
    if(head->color == p->color) return false;
    while(p != head) {
        if(p->color == p->next->color) return false;
        p = p->next;
    }
    return true;
}

void solve(int cases) {
    scanf("%d",&N);
    priority_queue< pair<int,char> > q;
    for(int i = 0 ; i < 6; i++){
        scanf("%d",&c[i].first);
        c[i].second = colors[i];
        q.push(c[i]);
    }
    while(!q.empty()) {
        pair<int,char> now = q.top(); q.pop();
        add_color(now.second,now.first);
        
    }
    printf("Case #%d: ",cases);
    if(isValid(head)) {
        display_list(head);
        printf("\n");
    } else {
        printf("IMPOSSIBLE\n");
    }
    delete(head);
    cur = NULL;
}

int main() {
    scanf("%d",&T);
    for(int t = 1 ; t<=T; t++) solve(t);
    return 0;
}
