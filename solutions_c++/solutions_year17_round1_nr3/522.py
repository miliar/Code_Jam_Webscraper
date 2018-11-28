#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
#include<array>
#include<cassert>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())




int hd, ad, hk, ak, b, d;

int calc(){
	int res=INF;
	int nd=0;
	while (1){//debuff
		int nb=0;
		while (1){
			int _ad = ad;
			int _ak = ak;
			int _hd=hd, _hk=hk;
			int turn=0;
			int x=0,y=0;
			while (turn < 300){
				if (x < nd){
					if (_hd - (_ak - d) <= 0){
						_hd=hd;
					}
					else{
						_ak -= d;
						x++;
					}
				}
				else{
					if (_hk - _ad <= 0)_hk-=_ad;
					else if (_hd-_ak <=0){
						_hd=hd;
					}
					else{
						if (y < nb){
							_ad += b;
							y++;
						}
						else{
							_hk -= _ad;
						}
					}
				}
				_hd -= _ak;

				turn++;
				if (_hk <= 0){
					res = min(res,turn);
					break;
				}

				if (_hd <= 0)break;
			}
			if (b==0 || (ad+nb*b) >= hk)break;
			nb++;
		}
		if (d==0 || (ak-nd*d) <= 0)break;
		nd++;
	}
	return res;
}





int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;
	rep(_case,t){
		cin>>hd>>ad>>hk>>ak>>b>>d;


		int ans = calc();
		cout << "Case #" << _case + 1 << ": " ;
		if (ans == INF)cout << "IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}

	return 0;
}