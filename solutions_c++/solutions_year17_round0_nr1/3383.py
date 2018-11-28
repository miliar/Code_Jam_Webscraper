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

string S, OK;
int N, K;

int main(){
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++){
		cin >> S >> K;
		N = S.size();
			
		OK.clear();
		for (int i = 0; i < N; i++){
			OK += "+";
		}

		int cont = 0;
		for (int i=0; i <= (N-K); i++){
			if (S[i] == '-'){
				cont++;
				for (int j=i; j < i+K; j++)
					S[j] = (S[j]=='+'? '-':'+');
			}
		}	

		if (S != OK) 
			printf("Case #%d: IMPOSSIBLE\n",c);
		else
			printf("Case #%d: %d\n",c, cont);
	}
}
