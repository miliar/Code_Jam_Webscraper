#include <iostream>

using namespace std;

int main()
{
    int t;
    int d,n;
    cin >> t;
    long long int k[1010];
    long long int s[1010];

    double mins;
    double eiei;
    cout.precision(20);
    for(int q =1;q<=t;q++){
        cin >> d >> n;
        for(int i = 0;i<n;i++ ){
            cin >> k[i] >> s[i];
        }
        mins = ((double)(k[0]*s[0]))/(d-k[0]) + s[0];

        for(int i =0;i<n;i++){
            eiei = ((double)(k[i]*s[i]))/(d-k[i]) + s[i];
            if(eiei<mins) mins = eiei;
           //if(mins < 0) cout << k[i] << " " << s[i] << " " << d ;
        }

        cout << "Case #" << q << ": " << mins << endl;


    }


    return 0;
}
