#include <iostream>
#include <set>
#include <iomanip>


using namespace std;

typedef pair<double,int> pdi;
#define mp make_pair
#define eps 0.00000001

int main(){
	int t;
	cin >> t;
	int c=1;
	while (c<=t){
		cout << "Case #" << c++ << ": ";
		int n,k;
		cin >> n >> k;
		double q;
		cin >> q;
		set < pdi > SET;
		
		for (int i=0;i<n;i++){
			double x;
			cin >> x;
			SET.insert(mp(x,i));
		}

		if (n==1){
			cout << SET.begin()->first + q << '\n';
			continue;
		}

		while (q>=eps){
			set<pdi>::iterator it = SET.begin();
			pdi sm = mp(it->first,it->second);
			it++;
			pdi lar = mp(it->first,it->second);
			double diff = eps+ (lar.first - sm.first);
			if (diff>q){
				diff = q;
			}
			if (diff*n<q){
				diff = q/n;
			}
			q -= diff;
			pdi NEW = mp(sm.first,sm.second);
			NEW.first += diff;
			SET.erase(sm);
			SET.insert(NEW);
		}

		set<pdi>::iterator it;
		double prob = 1;
		for (it = SET.begin(); it!=SET.end(); it++){
			//cout << (it->second) << " " << (it->first) << endl;
			prob *= (it->first);
		}

		cout << setprecision(30) << prob << '\n';
	}
}
