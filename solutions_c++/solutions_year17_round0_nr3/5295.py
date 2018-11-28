#define C
#ifdef C

#include <bits/stdc++.h>

using namespace std;

//typedef vector<long long> vi;

int main(){

    ios::sync_with_stdio(0);

    int tc , count = 1; cin >> tc;
    while ( tc-- ){
        long long n , k , l , r; cin >> n >> k;
        vector<long long> f,s,cnf,cns;
        if (n % 2)
            f.push_back(n / 2), cnf.push_back(2) , l = r = n/2;
        else{
            f.push_back(n / 2); f.push_back((n-1) / 2);
            cnf.push_back(1); cnf.push_back(1);
            l = n/2; r = (n - 1)/2;
        }
        k--;
        int i = 1 ;
        while ( k > 0){
            long long sum = 0;
            for ( int j = 0 ; j < f.size(); j++)
                sum += cnf[j];
            if ( k <= sum ) {
                if (f.size() == 2) {
                    if (k <= cnf[0])
                        l = f[0] / 2, r = (f[0] - 1) / 2;
                    else
                        l = f[1] / 2, r = (f[1] - 1) / 2;
                }
                else
                    l = f[0] / 2, r = (f[0] - 1 ) / 2;
                break;
            }
            else {
                k -= pow(2 , i);
                i++;
                cns.clear(); cns.resize(2,0);
                s.clear();
                if ( f.size() == 2){
                    s.push_back( f[0] / 2);
                    cns[0] += cnf[0];
                    if ( (f[0] - 1 ) / 2 == s[0])
                        cns[0] += cnf[0];
                    else{
                        s.push_back((f[0] - 1 ) / 2);
                        cns[1] += cnf[0];
                    }
                    if ( s.size() == 2){
                        if ( f[1] / 2 == s[0])
                            cns[0] += cnf[1];
                        else if ( f[1] / 2 == s[1])
                            cns[1] += cnf[1];
                        if ( (f[1] - 1 ) / 2 == s[0])
                            cns[0] += cnf[1];
                        else if ( (f[1] - 1 ) / 2 == s[1])
                            cns[1] += cnf[1];
                    }
                    else if ( s.size() == 1){
                        if ( f[1] / 2 == s[0])
                            cns[0] += cnf[1];
                        else {
                            s.push_back(f[1] / 2);
                            cns[1] += cnf[1];
                        }
                        if ( s.size() == 2) {
                            if ((f[1] - 1) / 2 == s[0])
                                cns[0] += cnf[1];
                            else if ((f[1] - 1) / 2 == s[1])
                                cns[1] += cnf[1];
                        }
                        else if( s.size() == 1){
                            if ( (f[1] - 1) / 2 == s[0])
                                cns[0] += cnf[1];
                            else {
                                s.push_back((f[1] - 1) / 2);
                                cns[1] += cnf[1];
                            }
                        }
                    }
                }
                else if( f.size() == 1){
                    s.push_back(f[0] / 2);
                    cns[0] += cnf[0];
                    if ( (f[0] - 1) / 2 == s[0])
                        cns[0] += cnf[0];
                    else{
                        s.push_back((f[0] - 1 ) / 2);
                        cns[1] += cnf[0];
                    }
                }
                f.clear(); cnf.clear();
                f = s;
                cnf = cns;
            }
        }
        cout << "Case #"<<count++<<": "<<l<<" "<<r<<endl;

    }

    return 0;
}

#endif