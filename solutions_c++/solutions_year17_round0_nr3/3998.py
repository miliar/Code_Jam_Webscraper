#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define oioi printf("oioi\n")
#define eoq cout << "eoq" << '\n'
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;
typedef pair<double, double> dd;
typedef vector<ll> vi;
typedef vector<ii> vii;
const int dx[] = {0 ,1,-1,0,1,-1,-1, 1};
const int dy[] = {-1,0,0, 1,1, 1,-1,-1};
const ll MOD = 0;
const ll N = 0;

int main () {
	
	int t, caso=1, n, k;
	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		priority_queue<int> pq;
		pq.push(n);
		
		int aux, aux1, aux2;
		for (int i = 0; i < n; i++)
		{
			aux = pq.top();
			pq.pop();
			
			aux--;
			if(aux%2==0) aux1 = aux/2, aux2 = aux/2;
			else aux1 = aux/2, aux2 = aux1+1;
			if(i==k-1){
				cout << "Case #" << caso++ << ": " << aux2 << " " << aux1 << "\n";
				break;
			}
			pq.push(ceil(aux*1.0/2.0));
			pq.push(floor(aux*1.0/2.0));
		}
		
		
	}
	
	
	return 0;
}
