/* 
	author: Bhrigu Gupta
		aka “bhrigudov”
*/

#include <bits/stdc++.h>

using namespace std;

#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,b,a) for(i=b; i>=a; i--)
#define tr(c, i) for(auto i= c.begin(); i!= c.end(); i++) 
#define pb push_back
#define mp make_pair
#define ub upper_bound
#define lb lower_bound
#define inp(str) getline(cin, str)
#define INF 1e11
#define MX 200002

typedef long long ll;
typedef vector<int> vi;

int n;

void Solve(char a, char b, char c, int x, int y, int z) {
	if(x>y+z) {
		cout<<"IMPOSSIBLE";
		return;
	}

	int i, extra;
	extra = y+z-x;

	int cnt = 0;
	fo(i,0,y) {
		cout<<a;
		x--;
		cout<<b;
		cnt+=2;;
		if(extra) {
			cout<<c;
			extra--;
			cnt++;
		}
	}

	fo(i,0,x) {
		cout<<a;
		cnt+=2;
		cout<<c;
	}
	if(cnt!=n) {
		cout<<"cnt = "<<cnt<<"  n = "<<n<<endl;
		cout<<"ERROR!\n";
	}
}

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false); 

	int N, R, O, Y, G, B, V, i, j, t, k, ans, temp;

	cin>>t;
	fo(k,1,t+1)
	{
		cin>>N; n= N;
		cin>>R>>O>>Y>>G>>B>>V;

		cout<<"Case #"<<k<<": ";

		if(R>=Y && Y>=B && R>=Y) Solve('R', 'Y', 'B', R, Y, B);
		else if(R>=B && B>=Y && R>=Y)  Solve('R', 'B', 'Y', R, B, Y);
		else if(B>=R && R>=Y && B>=R) Solve('B', 'R', 'Y', B, R, Y);
		else if(B>=Y && Y>=R && B>=Y) Solve('B', 'Y', 'R', B, Y, R);
		else if(Y>=B && B>=R && Y>=B) Solve('Y', 'B', 'R', Y, B, R);
		else Solve('Y', 'R', 'B', Y, R, B);
		cout<<endl;
	}

	return 0;
}