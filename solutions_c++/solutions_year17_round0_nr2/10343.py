///José Luiz da Silva Neto
///Computer Engineering - Federal University of Itajubá
#include <bits/stdc++.h>
 
using namespace std;
 
#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define DEG_to_RAD(X)   (X * PI / 180)
#define MOD 1000000007LL
 
typedef pair <int,int> pii;
typedef vector <int> vi;
typedef vector < pii > vii;
typedef long long ll;
typedef unsigned long long ull;	

#define D(x) cout << #x << " = " << x << endl
#define C(x) cout << "Chegou aqui " << x << endl
#define pn printf("\n")
#define ps printf(" ")

int vx[] = {1,0,-1,0};
int vy[] = {0,1,0,-1};

bool verify(int x) {
	bool flag = true;
	int aux = 9;
	while(1) {
		if(x%10 > aux)
			flag = false;
		aux = x%10;
		x/=10;
		if(x == 0)
			break;
	}
	return flag;
}

int f(int x) {
	while(1) {
		if(x == 0)
			return 0;
		if(verify(x))
			return x;
		x--;
	}
}

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Output","w",stdout);
	int q;
	scanf("%d",&q);
	for(int i = 1;i <= q;i++) {
		int n;
		scanf("%d",&n);
		printf("Case #%d: %d\n",i,f(n));
	}	
	return 0;
}