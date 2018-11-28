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


ll sol(string N){
	string dummy;
	
	int put9=N.size();
	for (int i = N.size()-2; i>=0; i--){
		if (N[i] > N[i+1]){
			put9 = i+1;
			N[i]--;
		}
	}
	for (int j=put9; j < N.size(); j++) N[j] = '9';

	stringstream ss;
	ss << N;
	ll resp;
	ss >> resp;

	return resp;
}

int main(){
	int caso;
	cin >> caso;
	for (int c = 1; c <= caso; c++){
		string N;
		cin >> N;
		printf("Case #%d: %lld\n",c, sol(N));
	}
}


