#include <iostream>
#include <algorithm>
#include <climits>
#include <iomanip>

using namespace std;
typedef  double lld;

const double epsilon = 0.0000001;
const  bool dbg = false;


lld getMaxSpeed(lld d, lld hPosition, lld hSpeed){
    lld horseTime = (d - hPosition) / hSpeed;
    lld maxSpeed = d/horseTime;

    return maxSpeed;
}


int main() {

    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    for(int caseId = 1; caseId <= t ; ++ caseId){
        lld maxSpeed = 1e16  ;
        lld d,n;
        cin >> d >> n;

        if(caseId ==18 && dbg){
            cout <<"sepcial" << endl;
            cout << d << " " <<n << endl;
        }

        for(int i=0; i <n; i++){
            lld hPosition, hSpeed;
            cin >> hPosition >> hSpeed;
            if(caseId ==18 && dbg)
            cout << hPosition << " " <<hSpeed << endl;
            maxSpeed = min(maxSpeed, getMaxSpeed(d,hPosition, hSpeed));
        }

        if(caseId ==18 && dbg)
            cout << "spc end" << endl;

        cout << "Case #" << caseId << ": "  << setprecision (10) << fixed << maxSpeed << "\n";

    }

}