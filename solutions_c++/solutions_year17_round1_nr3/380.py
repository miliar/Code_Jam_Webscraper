#include <bits/stdc++.h>
using namespace std;

int T;
int Hd, Ad, Hk, Ak, B, D;


#define mp make_pair
#define hd second.first.first
#define hk second.first.second
#define ad second.second.first
#define ak second.second.second

int main(){
	cin >> T;
	for (int qr = 1; qr<=T; qr++){
		cout << "Case #" << qr << ": ";

		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		int maxH = Hd;

		queue<pair<int, pair< pair<int,int>, pair<int,int> > > > q;

		q.push(mp(0, mp( mp(Hd, Hk), mp(Ad, Ak))));

		int best = -1;

		set< pair< pair<int,int>, pair<int,int> > > s;
		s.insert(mp( mp(Hd, Hk), mp(Ad, Ak)));

		while (!q.empty()){

			int d = q.front().first;
			Hd = q.front().hd;
			Hk = q.front().hk;
			Ad = q.front().ad;
			Ak = q.front().ak;
			q.pop();

			//cout << "state = " << endl;
			//cout << d << " " << Hd << " " << Hk << " " << Ad << " " << Ak << endl;
			
			if (Hk <= 0) {
				best = d;
				break;
			}
			if (Hd <= 0){
				continue;
			}



			d = d+1;

			// attack

			pair< pair<int,int>, pair<int,int> > state = mp( mp(Hd-Ak, Hk-Ad), mp(Ad, Ak));
			if (s.count(state)==0){
				s.insert(state);
				q.push(mp(d, state));
			}


			// buff
			state = mp( mp(Hd-Ak, Hk), mp(Ad+B, Ak));
			if (s.count(state)==0){
				s.insert(state);
				q.push(mp(d, state));
			}

			// cure
			state = mp( mp(maxH-Ak, Hk), mp(Ad, Ak));
			if (s.count(state)==0){
				s.insert(state);
				q.push(mp(d, state));
			}

			// debuff
			int tmp = max(0, Ak - D);

			state = mp( mp(Hd-tmp, Hk), mp(Ad, tmp));
			if (s.count(state)==0){
				s.insert(state);
				q.push(mp(d, state));
			}

		}

		if (best == -1){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			cout << best << endl;
		}

	}
}