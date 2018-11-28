/*
	In the Name Of GOD
*/
#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>

using namespace std;
#define N 10020
#define MAXN 60
#define X first
#define Y second
#define CLR(x,a) memset(x,a,sizeof(x))
#define FOR(i,b) for(ll i=0;i<(b);i++)
#define FOR1(i,b) for(ll i=1;i<=(b);i++)
#define FORA(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORB(i,b,a) for(ll i=(b);i>=(a);i--)
#define sh(x) cerr<<(#x)<<" = "<<(x)<<endl
#define EPS 0.00001
#define ull unsigned long long int
#define ll long long 
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define EXIST(a,b) find(ALL(a),(b))!=(a).end()
#define Sort(x) sort(ALL(x))
#define UNIQUE(v) Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
//const double PI = acos(-1);
typedef complex<double> point;
typedef pair<ll,ll> pii;
typedef pair<int, pii> piii;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef vector<pii> vpii;
typedef vector<piii> vpiii;

int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test = 0;
	while(T--)
	{
		test++;
		int ans = 0;


		ll n,k;
		cin>>n>>k;
		vector<pii> myvec;
		myvec.PB(MP(n,1));
		while(k>0){
			vector <pii> newvec;
			set<ll> myset;
			map<ll,ll> mymap;
			bool b = 0;
			FOR(i,myvec.sz){
				pii tmp = myvec[i];
				myset.insert((tmp.X-1)/2);
				myset.insert(tmp.X/2);
				if(k<=tmp.Y){
					b = 1;
					cout<<"Case #"<<test<<": "<<(tmp.X/2)<<" "<<(tmp.X-1)/2<<endl;
					break;
				}
				mymap[(tmp.X-1)/2] = mymap[(tmp.X-1)/2] + tmp.Y;
				mymap[(tmp.X/2)] = mymap[(tmp.X/2)] + tmp.Y;
				k-=tmp.Y;
			}
			if(b) break;
			// sh(myset.size());
			for(set<ll>::reverse_iterator it = myset.rbegin();it!=myset.rend();it++){
				newvec.PB(MP(*it,0));
			}
			FOR(i,newvec.sz){
				newvec[i].Y = mymap[newvec[i].X];
			}
			myvec.clear();
			FOR(i,newvec.sz){
				// cerr<<newvec[i].X<<" "<<newvec[i].Y<<endl;
				myvec.PB(newvec[i]);
			}
			// getch();
			// int h;
			// cin>>h;
			// sh(k);
		}


		// cout<<"Case #"<<test<<": "<<ans<<endl;
	}
}
