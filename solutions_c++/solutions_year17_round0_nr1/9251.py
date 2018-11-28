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



int main(){

     freopen("/Users/bajaj/Downloads/input-3.in", "r", stdin);
	 freopen("/Users/bajaj/Downloads/manic_output.txt", "w", stdout);

	//debug(ans270);

//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);


	int t;
	cin>>t;
	int casi = 1;

	while(t--){

		int k, ans=0;
		bool yes = 0;
		string s;
		cin>>s>>k;

		int len = s.length();
		int i=0;

		for(i=0;i<len;i++){
			if(s[i]=='-'){
				if(i+k > len){
					break;
				}
				else{
					ans++;
					for(int j=i;j<i+k;j++){
						if(s[j]=='-')
							s[j]='+';
						else
							s[j] = '-';
					}
				}
			}
		}


		if(i==len)
			cout<<"Case #"<<casi++<<": "<<ans;
		else{
			cout<<"Case #"<<casi++<<": IMPOSSIBLE";
		}

		cout<<"\n";

	}



	return 0;

}
