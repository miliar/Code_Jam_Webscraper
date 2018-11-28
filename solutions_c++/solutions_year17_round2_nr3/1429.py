// Kasimir Tanner 2017
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;
typedef long double ld;

vector<pair<ld,ld> > horses;
vector<ld> distances;
ullint N;

ld findMin(ullint n, ld dleft, ld speed){
   // cout << "CALL: " << n << "  DLEFT, SPEED " << dleft << " " << speed << "\n";
    //cout << "DISTANCE: " << distances[n] << "\n";
    if(n == N-1)return 0;
    ld r = 0;
    if(dleft < distances[n]){
        r = (distances[n]/horses[n].second) + findMin(n+1,horses[n].first-distances[n],horses[n].second);
        return r;
    }
    r = distances[n]/horses[n].second + findMin(n+1,horses[n].first-distances[n],horses[n].second);
    ld d = distances[n]/speed+findMin(n+1,dleft-distances[n],speed);
    return min(r,d );
}

int main(){
    ullint T;
    cin >> T;
    for(ullint t = 0;t<T;t++){
        ullint Q;
        cin >> N >> Q;
        horses.clear();
        distances.clear();
        for(ullint i = 0;i<N;i++){
            ld d,s;
            cin >> d >> s;
            horses.push_back(make_pair(d,s));
        }
        for(ullint i =0;i<N;i++){
            for(ullint j = 0;j<N;j++){
                ld c;
                cin >> c;
                if(i +1== j){
                    distances.push_back(c);
                }
            }
        }
        ullint f,g;
        cin >> f >> g;
        cout << "Case #" << t+1 << ": " << fixed << setprecision(6) << findMin(0,0,0) << "\n";
    }

}