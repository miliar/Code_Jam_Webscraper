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

void getDigits(long long n, vector<int>& digits){
	while(n!=0){
		digits.pb(n%10);
		n = n/10;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	for(int m=1;m<=t;m++){
		long long n;
		cin >> n;
		vector<int> digits;
		getDigits(n,digits);
		int siz = sz(digits);
		rep(i,siz-1){
			if(digits[i]<digits[i+1]){
				digits[i+1] += -1;
				for(int j=i;j>=0 && digits[j]!=9;j--){
					digits[j] = 9;
				}
			}
		}
		cout << "case #" << m << ": ";
		if(digits[siz-1]==0){
			for(int i=siz-2;i>=0;i--){
				cout << digits[i];
			}
		}
		else{
			for(int i=siz-1;i>=0;i--){
				cout << digits[i];
			}	
		}
		cout << endl;
	}
    return 0;
}

