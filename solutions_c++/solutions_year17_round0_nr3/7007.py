#include<bits/stdc++.h>
#define FRU freopen("out.txt","w",stdout)
#define FRO freopen("in.txt","r",stdin)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define mem(ara,n) memset(ara,n,sizeof ara)
#define loop(i,j,n) for(i=j;i<n;i++)
#define rloop(i,j,n) for(i=n;i>=j;i--)
#define INF 2147483647
#define ll long long
#define pii pair<int,int>
#define eps 1e-9
#define mii map<int,int>
#define vi vector<int>
#define all(n) n.begin(),n.end()
#define inf INF

//const int row[]={-1, -1, -1,  0,  0,  1,  1,  1};  // Kings Move
//const int col[]={-1,  0,  1, -1,  1, -1,  0,  1};  // Kings Move
//const int row[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int col[]={-1,  1, -2,  2, -2,  2, -1,  1};  // Knights Move
//const int row[]={-1,0,0,1,0};
//const int col[]={0,-1,1,0,0};
int gcd(int a,int b)
{
    return b==0?a:gcd(b,a%b);
}
int lcm(int a,int b)
{
    return ((a*b)/gcd(a,b));
}

/*bool bitcheck(int n,int pos)
{
    return (bool)(n & (1<<pos));
}

int biton(int n,int pos)
{
    return n=n or (1<<pos);
}
int bitoff(int n,int pos)
{
    return n=n & ~(1<<pos);
}*/

using namespace std;

int main () {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
#endif
	freopen("out", "w", stdout);
	int t; 
	cin>>t; 
	for(int T = 1; T <= t; T++ ) {
		int n, k; cin>>n>>k;
		priority_queue<int> Q; 
		Q.push(n);
		for(int i=0; i<k-1; i++) {
			int nxt = Q.top(); Q.pop();
			if(nxt & 1) {
				nxt /= 2;
				Q.push(nxt);
				Q.push(nxt);
			} else {
				nxt /= 2;
				Q.push(nxt);
				Q.push(nxt-1);
			}
		}
		int fk = Q.top();
		cout<<"Case #"<<T<<": ";
		if(fk & 1) {
			fk /= 2; 
			cout<<fk<<" " << fk<<endl;
		} else {
			fk /= 2;
			cout<<fk<<" " << fk-1<<endl;
		}

	} 
}
