#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int max(int a, int b){
    if(a > b) return a;
    else return b;
}



struct unic {
    char farba;
    int pocet;
    bool operator<(unic const &r) const {
        if(pocet > r.pocet) return true;
        else if (pocet == r.pocet && farba < r.farba) return true;
        else return false;
        
        
    } 
};

int main(){
	int T;
	cin >> T;
	for(int ii = 0; ii < T; ii++){
        int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;
    

        vector<unic> v;
        v.push_back((unic) {'R', R});
        v.push_back((unic) {'Y', Y});
        v.push_back((unic) {'B', B});

        vector<char> zoznam;
        sort(v.begin(), v.end());

        char posl = 'o';
        for(int i = 0; i < N; i++){
            if(v[1].pocet != 0 && posl == v[0].farba){
                zoznam.push_back(v[1].farba);
                v[1].pocet = v[1].pocet - 1;
            } else {
                zoznam.push_back(v[0].farba);
                v[0].pocet = v[0].pocet - 1;
            }
            
            posl = zoznam.back();
            sort(v.begin(), v.end());
        }

        if(zoznam.back() == zoznam[0] && N >= 2){
            zoznam[N-1] = zoznam[N-2];
            zoznam[N-2] = zoznam[0];
        }
        bool ci = true;
        for(int i = 0; i < N - 1; i++){
            if(zoznam[i] == zoznam[i+1]) {
                ci = false;
                break;
            }
        }

        if(zoznam[0] == zoznam[N - 1]){
            ci = false;
        }

        //cout << ci << "\n";
        //cout << v[0].pocet;

        /*
        int trojic = v[2].pocet;
        int dvojic = v[1].pocet - trojic;
        int ostava = v[0].pocet - dvojic;

        cout << trojic << " " << dvojic << " ostava " << ostava << "\n";
        if(ostava <= trojic){
            cout << "ide to\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
        */
        cout << "Case #" << ii+1 << ": ";
        if(ci == false) cout << "IMPOSSIBLE";
        else {
            for(int i = 0; i < N; i++){
                cout << zoznam[i];
            }
        }
        //cout << (long double)D / (long double)max;
        cout << "\n";
	}
	return 0;
}
