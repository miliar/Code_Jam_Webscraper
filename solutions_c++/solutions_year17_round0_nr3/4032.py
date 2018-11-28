#include <bits/stdc++.h>

//Input Output Macros
#define si(x) scanf("%d",&(x))
#define sl(x) scanf("%lld",&(x))
#define sc(x) scanf("%c", &(x))
#define ss(x) scanf("%s",(x))
#define pi(x) printf("%d",x)
#define pl(x) printf("%lld",x)
#define ps(x) printf("%s",(x))
#define pc(x) printf("%c",(x))
#define pn printf("\n")

//Useful container manipulation
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)
#define rfor(i,n) for(int (i)=n-1;(i)>=0;(i)--)
#define all(v) (v).begin(),(v).end()
#define PII pair<int,int>
#define PLL pair<long long, long long>
#define pb push_back
#define mk make_pair
#define sz(a) ((int)((a).size()))
#define ll long long
#define big 1000000007

//Useful hardware instructions
#define bitcount __builtin_popcount
#define gcd __gcd

//Useful functions
#define forall(i,a,n) for(int (i) =a;(i)<n;(i)++)
#define si2(a,b) scanf("%d %d",&(a),&(b))
#define si3(a,b,c) scanf("%d %d %d",&(a),&(b),&(c) )
#define mod(a,m) ( ( ( (a) % (m) ) + (m) ) % (m) )

//Debugging macros
#define what_is(x) cerr << #x << " is " << x << endl;

using namespace std;

class graph{
public:
	int vertices;
	vector<int> *adjlist;
	graph(int v){
		vertices = v;
		adjlist = new vector<int>[vertices];
	}
	void addEdge(int a, int b){
		adjlist[a].pb(b);
		adjlist[b].pb(a);
	}
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	for(int c=1;c<=t;c++){
		int n,K;
		cin >> n >> K;
		set< pair< pair<int,int> , pair<int,int> > > bruteopti;
		if(n%2==0) bruteopti.insert( mk( mk(n/2-1,n/2),mk(0,n) ) );
		else bruteopti.insert( mk( mk(n/2,n/2),mk(0,n) ) );
		for(int k=1;k<=K;k++){
			/*set< pair< pair<int,int> , pair<int,int> > >:: iterator itr = bruteopti.begin();
			while(itr!=bruteopti.end()){
				pair< pair<int,int> , pair<int,int> > p = (*itr);
				cout << "( " << p.first.first << ", " << p.first.second << " ) ";
				itr++;
			}
			cout << endl;*/
			pair< pair<int, int>,pair<int,int> >p =  *(bruteopti.rbegin());
			if(k==K){
				cout << "case #" << c << ": " << p.first.second <<" "<< p.first.first << endl;
				break;
			}
			bruteopti.erase(p);
			int n1 = p.second.second;
			int idx = p.second.first;
			if(n1%2==1){
				int n2 = n1/2;
				if(n2%2==0){
					bruteopti.insert( mk( mk(n2/2-1,n2/2),mk(2*idx+1,n2) ) );
					bruteopti.insert( mk( mk(n2/2-1,n2/2),mk(2*idx+2,n2) ) );
				}
				else if(n2%2==1){
					bruteopti.insert( mk( mk(n2/2,n2/2),mk(2*idx+1,n2) ) );
					bruteopti.insert( mk( mk(n2/2,n2/2),mk(2*idx+2,n2) ) );
				}
			}
			else if(n1%2==0){
				int n2 = n1/2;
				if(n2%2==0){
					//n2-1 odd
					bruteopti.insert( mk( mk(n2/2-1,n2/2),mk(2*idx+2,n2) ) );
					bruteopti.insert( mk( mk((n2-1)/2,(n2-1)/2),mk(2*idx+1,n2-1) ) );
				}
				else if(n2%2==1){
					//n2-1 even
					bruteopti.insert( mk( mk((n2-1)/2-1,(n2-1)/2),mk(2*idx+1,n2-1) ) );
					bruteopti.insert( mk( mk(n2/2,n2/2),mk(2*idx+2,n2) ) );
				}
			}
		}
	}
    return 0;
}
