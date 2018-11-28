#include <bits/stdc++.h>

using namespace std;
const double pi = 3.1415926535897932384;
class P{
public:
	long long rad;
	long long hei;
	P(){};
	P(long long rad, long long hei){
		this -> rad = rad;
		this -> hei = hei;
	}
	double find_P(){
		return pi * 2 * rad * hei;
	}
};

bool operator < (const P &a, const P &b){
	return a.rad * a.hei > b.rad * b.hei;
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int N, K;
		cin >> N >> K;
		int rad[N], hei[N];
		P niza[N];
		for(int i=0; i<N; i++){
			cin >> rad[i] >> hei[i];
			P p(rad[i], hei[i]);
			niza[i] = p;
		}
		double pi = 3.1415926535897932384;
		double res = 0.0000000;

		sort(niza, niza+N);

		for(int i=0; i<N; i++){
			double tmp = pi * niza[i].rad * niza[i].rad + niza[i].find_P();
			int cnt = 1, j = 0;
			while(cnt < K){
				if(i == j) j++;
				else {
					tmp += niza[j].find_P();
					j++;
					cnt++;
				}
			}
			res = max(res, tmp);
		}
		cout << setprecision(9) << fixed << res << endl;
	}

	return 0;
}

