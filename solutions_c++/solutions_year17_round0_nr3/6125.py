#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <queue>
#define rep(i,a,b) for (int i = (a); i <= (b); ++i) 
#define rep2(i,a,b) for (int i = (a); i >= (b); --i)
using namespace std;
const int maxn = 1000010;
typedef long long ll;
int mymin, mini, tt, n, k, ans, zmin[maxn], zmax[maxn], l[maxn], r[maxn];
bool b[maxn];
int lll,rrr;
struct Node
{
    int l,r;
    bool operator <(Node a) const  {  return  (r-l<a.r-a.l) || (r-l==a.r-a.l&&l>a.l); }
    bool operator >(Node a) const  {  return 1; }
};
                       //大根堆
    //priority_queue<Node, vector<Node>, greater<Node> > B;    //小根堆 

void work(int ss){
	memset(zmin, -1, sizeof(zmin));
			memset(zmax, -1, sizeof(zmax));
			mymin = 1e9;
			rep (j,1,n)
			if (b[j])
			{//each of which is the number of empty stalls 
			//between S and the closest occupied stall to the left or right
				lll = j;
				while (lll > 0 && b[lll]){
					lll--;
				}
				l[j] = j - lll - 1;
				rrr = j;
				while (rrr <= n && b[rrr]){
					rrr++; 
				} 
				r[j] = rrr-j-1;
				zmin[j] = min(l[j], r[j]);
				zmax[j] = max(l[j], r[j]);
				if (zmin[j] > zmin[mini]) 
					//mymin = zmin[j];
					mini = j;
				else if (zmin[j] == zmin[mini]){
					if (zmax[j] > zmax[mini]){
						mini = j;	
					}else{
						
					}
				}
				
			}
			b[mini] = false;
			//cout << mini << " " << zmin[mini] << " " << zmax[mini] << endl;
			
			printf("Case #%d: %d %d\n",ss,zmax[mini],zmin[mini]);
		//printf("--------");
}
int main()
{
//freopen("CCC.txt","w",stdout);
	cin >> tt;
	Node t,nt;
	int mid;
	
	
	for (int ss = 1; ss <= tt; ++ss){
		priority_queue<Node> A; 
		cin >> n >> k;
		memset(b,true,sizeof(b));
		//printf("%d %d\n",n, k);
		t.l = 1;
		t.r = n;
		A.push(t);
		rep (i,1,k){
			t = A.top();
			A.pop();
			mid = (t.l+t.r) >> 1;
			b[mid] = false;
			nt.l = t.l;
			nt.r = mid-1;
			A.push(nt);
			nt.l = mid+1;
			nt.r = t.r;
			A.push(nt);
			//work();
		}
		
		//work(ss);
		
		printf("Case #%d: %d %d\n",ss,max(mid-t.l,t.r-mid),min(mid-t.l,t.r-mid));
		
		//printf("Case #%d: %d %d\n",ss,zmax[mini],zmin[mini]);
		//printf("--------");
		//cout << zmax[mini] << " " << zmin[mini] << endl;
	}
		
	
	return 0;
}

