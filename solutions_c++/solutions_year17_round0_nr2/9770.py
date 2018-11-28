#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<bitset>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstring>
#include<sstream>
#include<climits>
#include<complex.h>
#include <unordered_map>


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;


#define S(x) scanf("%d",&x)
#define SD(x) scanf("%lf",&x)
#define SL(x) scanf("%lld",&x)
#define pb(x) push_back(x)
#define mp make_pair
#define F(i, a, b) for (int i = int(a); i < int(b); i++)
#define forit(it, a) for (it = (a).begin(); it != (a).end(); it++)
#define M(x,i) memset(x,i,sizeof(x))

/* -------------------CODE GOES HERE---------------------- */

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;


bool isTidy(int n){
	int pre = 10;
	while(n>0){
		int rem = n%10;
		if(rem>pre){
			return false;
		}
		pre = rem;
		n=n/10;
	}

	return true;

}


int main(){

     freopen("/Users/bajaj/Downloads/test.in", "r", stdin);
	 freopen("/Users/bajaj/Downloads/manic_output_2.txt", "w", stdout);

	//debug(ans270);

//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);


	int t;
	cin>>t;
	int casi = 1;

	while(t--){

		int ans;
		int n;
		cin>>n;

		for(int i=n;i>=1;i--){
			if(isTidy(i)){
				ans=i;
				break;
			}
		}

		cout<<"Case #"<<casi++<<": "<<ans;


		cout<<"\n";

	}



	return 0;

}
