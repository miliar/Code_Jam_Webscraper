#include <bits/stdc++.h>
#define prev fjioweajiof
#define x1 fjweoifakewop
#define y1 zfewfjwieofajoi
#define count fwjioewfjiwaofjo
#define ld long double
#define ll long long
#define int long long
using namespace std;

const int nmax = 100010;
const int inf = 100000000;

int t;
ld d, n, a[2][2020];

main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

int tests=0;
cin>>t;
	while (t--)
	{
	tests++;
		cin>>d>>n;
		for(int j = 0; j<n; j++)
			cin>>a[0][j]>>a[1][j];
		ld mn = -1;
		for(int j = 0; j<n; j++)
			if((d - a[0][j])/a[1][j] > mn)
				mn = (d - a[0][j])/a[1][j];
		cout<<"Case #"<<tests<<": ";
		cout << setprecision(8) << fixed << (d/mn) << endl;
	}






return 0;
}
