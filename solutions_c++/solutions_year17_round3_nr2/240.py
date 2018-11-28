#include <bits/stdc++.h>

using namespace std;
const double pi = 3.1415926535897932384;
class baby{
public:
	int s, e;
	bool c;
	baby(){};
	baby(int s, int e, bool c){
		this -> s = s;
		this -> e = e;
		this -> c = c;
	}
};

bool operator < (const baby &a, const baby &b){
	return a.s < b.s;
}

class hole{
public:
	int start, end;
	bool leftp, rightp;
	hole(){};
	hole(int start, int end, bool leftp, bool rightp){
		this -> start = start;
		this -> end = end;
		this -> leftp = leftp;
		this -> rightp = rightp;
	}
	int calc(){
		return end - start;
	}
};

bool operator < (const hole &a, const hole &b){
	return a.end - a.start < b.end - b.start;
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int Ac, Aj;
		cin >> Ac >> Aj;
		vector<baby> niza;
		vector<pair<int, int>> ac, aj;
		int sumc=0, sumj=0;
		for(int i=0; i<Ac; i++){
			int a, b;
			cin >> a >> b;
			ac.push_back(make_pair(a,b));
			baby nb(a, b, true);
			niza.push_back(nb);
			sumc += b-a;
		}
		for(int i=0; i<Aj; i++){
			int a, b;
			cin >> a >> b;
			aj.push_back(make_pair(a,b));
			baby nb(a, b, false);
			niza.push_back(nb);
			sumj += b-a;
		}
		sort(niza.begin(), niza.end());
		vector<hole> hc, hj, hd;
		for(int i=1; i<niza.size(); i++){
			hole hh(niza[i-1].e, niza[i].s, niza[i-1].c, niza[i].c);
			if(niza[i].c == niza[i-1].c){
				if(niza[i].c == true){
					hc.push_back(hh);
				} else {
					hj.push_back(hh);
				}
			} else {
				hd.push_back(hh);
			}
		}
		sort(hc.begin(), hc.end());
		sort(hd.begin(), hd.end());
		sort(hj.begin(), hj.end());
		int hcp=0, hjp=0, hdp=0;
		for(int i=0; i<hc.size(); i++){
			if(sumc + hc[i].calc() <= 720){
				sumc += hc[i].calc();
				hcp ++;
			} else {
				break;
			}
		}
		for(int j=0; j<hj.size(); j++){
			if(sumj + hj[j].calc() <= 720){
				sumj += hj[j].calc();
				hjp++;
			} else {
				break;
			}
		}
		int res = 0;

		if(niza[0].c == niza[niza.size()-1].c){
			if(niza[0].c){
				if(sumc + niza[0].s + (1440 - niza[niza.size()-1].e) <= 720){
					sumc += niza[0].s + (1440 - niza[niza.size()-1].e);
				} else {
					res += 2;
				}
			} else {
				if(sumj + niza[0].s + (1440 - niza[niza.size()-1].e) <= 720){
					sumj += niza[0].s + (1440 - niza[niza.size()-1].e);
				} else {
					res += 2;
				}
			}
		} else {
			res ++;
		}
		/*if(niza[0].c && sumc + niza[0].s <= 720){
			sumc += niza[0].s;
		} else if(niza[0].c){
			res++;
		} else if(niza[0].c == false && sumj + niza[0].s <= 720){
			sumj += niza[0].s;
		} else if(niza[0].c == false){
			res++;
		}

		if(niza[niza.size()-1].c && sumc + (1440 - niza[niza.size()-1].e) <= 720){
			sumc += 1440 - niza[niza.size()-1].e;
		} else if(niza[niza.size()-1].c){
			res++;
		} else if(niza[niza.size()-1].c == false && sumj + (1440 - niza[niza.size()-1].e) <= 720){
			sumj += 1440 - niza[niza.size()-1].e;
		} else if(niza[niza.size()-1].c == false){
			res++;
		}*/

		res += hd.size();
		res += (hc.size() - hcp) * 2;
		res += (hj.size() - hjp) * 2;
		cout << res << endl;
	}


	return 0;
}

