//bismillahir rahmanir raheem

#include <string>
#include <vector>
#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<math.h>
#include<string.h>
#include <stdlib.h>
#include<map>
#include<queue>
#include<stack>
#include<utility>
#include<stdlib.h>
#include<string>
#include<set>
#include<iomanip>
#define lld long long int
#define CLR(a) memset(a,0,sizeof(a))
#define RESET(a) memset(a,-1,sizeof(a))
#define act(a) memset(a,1,sizeof(a))
#define setinf(a) memset(a,0b01111111,sizeof(a));
#define FRO freopen("/Users/sheikahm/Contests/General/General/C-small-2-attempt0.in","r",stdin);
#define FROF(a) freopen(a,"r",stdin);
#define FROut freopen("/Users/sheikahm/Contests/General/General/M-SMALL-output.txt","w",stdout);
#define ui unsigned int
#define came "came"
#define pii pair<int,int>
#define plii pair<long long int, int>
#define pll pair<long long,long long>
#define pic pair<int,char>
#define ninf (-1e9)-2
#define inf (1e9)+2
#include<fstream>
#include <assert.h>
#include <bitset>
#include <unordered_map>
#define foreach(x) for(__typeof(x.begin()) it=x.begin(); it!=x.end();it++)

using namespace std;
#define pid pair<int,double>
#define pdi pair<double,int>

#define PB push_back
#define MP make_pair
#define pri(x) printf("%d\n",x)
#define F first
#define S second
#define vit vector<int>::iterator

struct Node {
    int nodeValue;
    int mn;
    int mx;
    Node(int value, int mn, int mx) {
        this->nodeValue = value;
        this->mn = mn;
        this->mx = mx;
    }
};

class Compare {
public:
    bool operator() (const Node &a, const Node &b) const {
        if(a.mn != b.mn) {
            return a.mn < b.mn;
        }
        
        if(a.mx != b.mx) {
            return a.mx < b.mx;
        }
        return a.nodeValue>b.nodeValue;
    }
};

priority_queue<Node,vector<Node>, Compare> pq;

Node getNode(int start, int end) {
    int mid = start + (end - start) / 2;
    int szLeft = mid - start;
    int szRight = end - mid;
    assert(szLeft <= szRight);
    return Node(mid, szLeft, szRight);
}

pii findKth(int k) {
    while(k!=1 && !pq.empty()) {
        Node topNode = pq.top();
        pq.pop();
        if(topNode.mn)
        {
            pq.push(getNode(topNode.nodeValue - topNode.mn, topNode.nodeValue - 1));
        }
        if(topNode.mx)
        {
            pq.push(getNode(topNode.nodeValue + 1, topNode.nodeValue + topNode.mx));
        }
        k--;
    }
    assert(!pq.empty());
    Node ret = pq.top();
    return MP(ret.mx, ret.mn);
}

pii smallCalc(int n, int k) {
    
    int i,j;
    vector<int> map;
    map.resize(n);
    Node lastNode(0,0,0);
    for(j = 0; j < k; j++) {
        vector<int> l,r;
        l.resize(n);
        r.resize(n);
        l[0] = 0;
        r[n-1] = 0;
        for(i = 1; i< n; i++) {
            if(map[i] == 0 && map[i-1] ==0) {
                l[i] = l[i - 1] + 1;
            } else {
                l[i] = 0;
            }
        }
        for(i = n -2; i >= 0; i--) {
            if(map[i] == 0) {
                r[i] = r[i+1] +1;
            } else {
                r[i] = 0;
            }
        }
        
        Node mnnd(1e9,0,0);
        for(i = 0; i< n; i++) {
            Compare com;
            Node tmp = Node(i, min(l[i], r[i]), max(l[i], r[i]));
//            cout<< tmp.mn<<" "<<tmp.mx<<endl;
            if(com.operator()(mnnd, tmp)) {
                mnnd = tmp;
            }
        }
        cout<<mnnd.nodeValue<<endl;
        map[mnnd.nodeValue] = 1;
        lastNode = mnnd;
    }
    return MP(lastNode.mx, lastNode.mn);
}

int main() {
    FRO
    FROut
    int t, ca;
    scanf("%d",&t);
    for(ca = 1; ca <= t; ca++) {
        long n,k;
        cin>>n>>k;
        while(!pq.empty()) {
            pq.pop();
        }
        pq.push(getNode(0, (int) n-1));
        pii ret = findKth((int)k);
//        pii ret = smallCalc(n,k);
        printf("Case #%d: %d %d\n",ca, ret.first, ret.second);
    }
    return 0;
}
