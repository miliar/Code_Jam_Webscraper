#include <iostream>
#include <algorithm>

using namespace std;

const long double PI = 3.141592653589793238L;
struct pancake{
    double vyska;
    double polomer;

    //chcem od najvyssich
    bool operator<(pancake const &r) const {
        if(polomer * vyska  > r.vyska * r.polomer) return true;
        else return false;
    
    }
};

int main(){
    cout.precision(17);
	int T;
	cin >> T;
	for(int ii = 0; ii < T; ii++){
        int N, K;
        cin >> N >> K;

        int R, H;
        vector<pancake> palacinky;
        for(int i = 0; i < N; i++){
            cin >> R >> H;
            palacinky.push_back((pancake) {H, R});
        }
	    

        double max = 0;
        double okolo = 0;
        sort(palacinky.begin(), palacinky.end());
        //for(int i = 0; i < N; i++){
        //    cout << palacinky[i].vyska << " " << palacinky[i].polomer << " " <<
        //        palacinky[i].vyska * palacinky[i].polomer << endl;
        //}
        
        
        for(int i = 0; i < N; i++){
            //na spodku bude i-ta
            //cout << "RESET\n";


            int pocet = 0;
            okolo = 0;
            double vrch = PI * (double)(palacinky[i].polomer) *
                palacinky[i].polomer;
			
            okolo += 2 * PI * (double)palacinky[i].polomer * palacinky[i].vyska;
            pocet++;
            
            for(int j = 0; j < N; j++){
                if(i == j) continue;
                if(palacinky[j].polomer > palacinky[i].polomer) continue;
                if(pocet >= K) continue;

                okolo += 2 * PI * palacinky[j].polomer * palacinky[j].vyska;
                //cout << "Zac s "<< i << " pripocitavam " << j << " " <<
                //    palacinky[j].vyska << " " << okolo <<endl;
                pocet++;
            }
            if(pocet != K) continue;
			if(okolo + vrch > max) max = okolo + vrch;
            //2cout << i << " "<< palacinky[i].vyska << " " << palacinky[i].polomer << "\n";
        }

        //vyberes ktora je na spodku
        //od nej vezmes K najvyssich mensieho polomeru


        //nemozes vziat tu najvacsiu

        cout << "Case #" << ii+1 << ": ";
        cout << max;
			//cout << (long double)D / (long double)max;
        cout << "\n";
	}
	return 0;
}
