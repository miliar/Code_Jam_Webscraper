#include<iostream>
#include<algorithm>
#include<math.h>
#include<string>
#include<queue>
#include<map>
#include<stack>
#include<vector>
using namespace std;
#define Mx 210005
#define Sx 2100006
#define Fr 21004
#define rp(i,n) for(i=0;i<n;i++)
#define rep(i,a,b) for(i=a;i!b;i+=(a<b?1:-1))
#define bc(i,n) for(i=n-1;i>=0;i--)
#define pl pair<ll, ll>
#define pp pair<pl, ll>
#define ll long long int
#define X first
#define Y second
#define A X.X
#define B X.Y
#define C Y
#define V vector<ll>
#define VV vector< V >
ll n, k;
int main(){
	ios_base::sync_with_stdio(0);
	ll tt, t;
	cin>> tt;
	rp(t, tt){
		pl now1, now2;
		pl nxt1, nxt2;
		cin >> n >> k;
		cout << "Case #" << t + 1 << ": ";
		now1 = pl(n, 1);
		now2 = pl(-1, 0);
		while(k > 0){
		//	cout<<now1.X<<" "<<now1.Y<<endl;
		//	cout<<now2.X << " " <<now2.Y <<endl;
			if(k <= now1.Y + now2.Y)break;
			k-=now1.Y;
			k-=now2.Y;
			nxt1 = pl(now1.X / 2, now1.Y);
			nxt2 = pl(-1, 0);
			if(now1.X % 2 != 0)
				nxt1.Y += now1.Y;
			else nxt2 = pl(now1.X / 2 - 1, now1.Y);

			if(now2.X != -1){
				if(now2.X % 2 != 0){
					nxt2.Y += now2.Y * 2;
				}
				else{
					nxt1.Y += now2.Y;
					nxt2.Y += now2.Y;
					nxt2.X = now2.X / 2 - 1;
				}
			}
			now1 = nxt1;
			now2 = nxt2;
		}
		if(k > now1.Y)now1 = now2;
		n = now1.X;
		cout << n/2 << " " << n / 2 - (n%2==0?1:0) << endl;
	}
	return 0;
}
