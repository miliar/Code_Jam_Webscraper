#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <fstream>
#include <map>
using namespace std;
const int N = 2120;

struct Node
{
    int x;
    int y;
    int len;
    Node(int a=0, int b=0, int c=0)
    {
        x = a;
        y = b;
        len = c;
    }
    friend bool operator < (const Node& A, const Node& B)
    {
        if(A.len<B.len) return true;
        if(A.len == B.len && A.x > B.x) return true;
        return false;
    }
};

int t;
int n, k;

int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
        scanf("%d%d", &n, &k);
        priority_queue<Node> q;
        q.push(Node(0, n+1, n));
        int x, y, mid;
        while(k--)
        {
            Node temp = q.top();
            q.pop();
            x = temp.x;
            y = temp.y;
            mid = (x+y)/2;
            q.push(Node(x, mid, mid-x-1));
            q.push(Node(mid, y, y-mid-1));
        }
        printf("Case #%d: %d% d\n", i, y-mid-1, mid-x-1);
    }
    return 0;
}

