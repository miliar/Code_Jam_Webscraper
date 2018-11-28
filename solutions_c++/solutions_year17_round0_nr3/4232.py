#include <bits/stdc++.h>

using namespace std;

struct mindol{
    int a, b;
};

bool operator <(mindol a, mindol b)
{
    if(a.b-a.a == b.b-b.a)return a.a<b.a;
    else return a.b-a.a < b.b-b.a;
}

priority_queue<mindol> PQ;

int n, k, t;

int solve(int y)
{
    scanf("%d %d", &n, &k);
    while(!PQ.empty())PQ.pop();
    PQ.push({0, n+1});
    for(int i=1;i<=k;i++){
        mindol s = PQ.top(); PQ.pop();
        int mid = (s.a+s.b)/2;
        if(i==k)return printf("Case #%d: %d %d\n", y, s.b-mid-1, mid-s.a-1);
        if(s.a+1<mid)PQ.push({s.a, mid});
        if(mid+1<s.b)PQ.push({mid, s.b});
    }

}

int main()
{
    freopen("C-small-2-attempt1.in", "r", stdin);
    freopen("C_output_2.txt", "w", stdout);
    scanf("%d", &t);
    for(int i=1;i<=t;i++)solve(i);
    return 0;
}
