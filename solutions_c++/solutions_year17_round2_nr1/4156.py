#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<int(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(int)(n-1);i>=int(s);i--)
#define si(a) ((int)(a).size())
#define pb push_back
#define mp make_pair
#define endl '\n'
#define all(c) (c).begin(), (c).end()
#define D(a) cerr << #a << "=" << a << endl;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int tint;

const int MAXN = 1e3+10;
int p[MAXN];
double v[MAXN], t[MAXN];

int main() {
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	ios_base::sync_with_stdio(false); 
	cin.tie(0);

	int nc;
	cin >> nc;
	
	forn(caso, nc) {
		int f, n;
		cin >> f >> n;
		
		dforsn(i, 0, n) cin >> p[i] >> v[i];
		
		p[n] = f;
		t[n-1] = (f-p[n-1]) / v[n-1];
		
		dforsn(i, 0, n-1) {
			//cout << "start " << p[i] << ' ' << p[i+1] << ' ' << v[i] << endl;
			t[i] = (p[i+1]-p[i])/v[i];
			
			double tact = t[i];
			forsn(j, i+1, n) {
				//cout << "antes " << t[i] << ' ' << t[j] << ' ' << v[i] << ' ' << v[j] << endl;
				if (t[j] > tact) {
					v[j] = min(v[i], (f-p[j])/(t[j]-tact));
					t[j] = (p[j+1]-p[j])/v[j];
				}
				else {
					v[j] = v[i];
					t[j] = (p[j+1]-p[j])/v[j];
				}
				tact += (p[j+1]-p[j])/v[j];
				
				//cout << "desp " << j << ' ' << v[j] << ' ' << t[j] << ' ' << t[i] << endl;
			}
			//cout << endl;
		}
		
		double tot = 0;
		forn(i, n) tot += t[i];
		
		cout << "Case #" << caso+1 << ": " << fixed << setprecision(6) << f/tot<< endl;
	}

	return 0;
}
