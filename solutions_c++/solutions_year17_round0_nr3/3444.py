#include <bits/stdc++.h>
using namespace std;

#define f(i,a,b) for(int i=(a); i < (b); i++)

#define all(c) c.begin(), c.end()
#define SORT(c) sort(all(c))
#define pb push_back
#define sz size()
#define D(x) cout << __LINE__ <<" "<< #x " = " << (x) << endl;
#define D2(x,y) cout << __LINE__ <<" "<< #x " = " << (x) \
<<", " << #y " = " << (y) << endl;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;

const long long int LINF = ((1LL)<<60);
const int INF = 0x3f3f3f3f;
const double EPS = 1e-6;
const double pi = acos(-1.0);

int K, N;

struct interval{
	int s, e;
	interval(int s=0, int e=0):s(s), e(e) {}
	
	void show(){
		cout << "("<< s << " " << e << ")\n";
	}
	
	bool operator < (interval q) const{
		if ( (e-s) != (q.e-q.s) )
			return ( (e-s) > (q.e-q.s) );
		return e < q.e;
	}		
};

set<interval> st;
set<interval> :: iterator it;

int main(){
	int caso;
	cin >> caso;
	
	int a, b, aa, bb; // last interval choosen
	for (int c = 1; c <= caso; c++){
		cin >> N >> K;
		st.clear();
		st.insert(interval(1,N));
		while(K--){
			it = st.begin();
			a = it->s;
			b = it->e;
			aa = a; bb = b;
			st.erase(it); 
			int mid = (a + b)/2;
			if (mid != a) st.insert(interval(a,mid-1));
			if (mid != b) st.insert(interval(mid+1,b));	
		}
		int a = aa, b = bb;
		int mid = (a + b)/2;
		int L = abs(mid-a);
		int S = abs(b-mid);
		if (L < S) swap(L,S);
		printf("Case #%d: %d %d\n",c, L,S);
	}
}
