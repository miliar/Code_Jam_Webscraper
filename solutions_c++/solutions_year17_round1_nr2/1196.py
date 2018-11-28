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
bool isIntersection(pair<int,int>a, pair<int,int> b){
	if(a.first<=a.second && b.first<=b.second){
		if(a.first>b.second || a.second<b.first){
			return false;
		}
		else return true;
	}
	else return false;
}

/* Function to swap values at two pointers */
void swap(pair<int,int> *x, pair<int,int> *y)
{
    pair<int,int> temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
 
/* Function to print permutations of string
   This function takes three parameters:
   1. String
   2. Starting index of the string
   3. Ending index of the string. */
void permute(pair<int,int> *a, int l, int r, int& max, int p, pair<int,int> *b)
{
   	int i;
   	if (l == r){
   		int ct=0;
   		for(int i=0;i<p;i++){
    		if(isIntersection(b[i],a[i])){
   				ct++;
  			}
   		}
    	if(ct>max) max = ct;
    }
   else
   {
       for (i = l; i <= r; i++)
       {
          swap((a+l), (a+i));
          permute(a, l+1, r,max,p,b);
          swap((a+l), (a+i)); //backtrack
       }
   }
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	rep(_,t){
		int n,p;
		cin >> n >> p;
		int Qneed[n];
		rep(i,n){
			cin >> Qneed[i];
		}
		int Qgiven[n][p];
		rep(i,n){
			rep(j,p){
				cin >> Qgiven[i][j];
			}
		}
		pair<int, int> range[n][p];
		rep(i,n){
			rep(j,p){
				int c1 = ceil((1.0*Qgiven[i][j])/1.1);
				int c2 = floor((1.0*Qgiven[i][j])/0.9);
				int q1 = ceil((1.0*c1)/(Qneed[i]*1.0));
				int q2 = floor((1.0*c2)/(Qneed[i]*1.0));
				range[i][j] = mk(q1,q2);
			}
		}
		cout << "case #" << _+1 <<": "; 
		if(n==1){
			int ct = 0;
			rep(i,n){
				rep(j,p){
					if(range[i][j].first<=range[i][j].second){
						ct++;
					}
				}
			}
			cout << ct << endl;
		}
		else if(n==2){
			int max = 0;
    		permute(range[1], 0, p-1,max,p,range[0]);
    		cout << max << endl;
		}
	}
    return 0;
}
 