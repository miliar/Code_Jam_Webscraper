#include <iostream>
#include <vector>
using namespace std;

int main () {
    unsigned long long int t, i, j, l;
    cin >> t;
    unsigned long long int *n = new unsigned long long int[t];
    unsigned long long int *k = new unsigned long long int[t];
    for ( i = 0; i < t; i++ )
        cin >> n[i] >> k[i];
    unsigned long long int max, min, max_pos, max_val, diff, max_diff;
    vector <unsigned long long int> tmp;
    for ( i = 0; i < t; i++ ) {
        max = 0;
        min = 0;
        max_pos = 0;
        max_val = 0;
        max_diff = 0;
        diff = 0;

        tmp.push_back(1);
        tmp.push_back(n[i]+2);
        for ( j = 1; j <= k[i]-1; j++ )
        {   max_val = 0;
            max_diff = 0;
            for ( l = 1; l < tmp.size(); l++ ){
                diff = tmp[l] - tmp[l-1]-1;
                if ( diff > max_val ){
                    max_pos = l;
                    max_diff = diff;
                    max_val = diff;
                }
            }
            if ( max_val%2 == 0 )
                max_val = max_val/2;
            else max_val = (max_val + 1)/2;
            tmp.insert( tmp.begin()+max_pos, tmp[max_pos-1] + max_val );
        }
        if ( k[i] > 1 ){
            max_diff = 0;
        }
        for ( l = 1; l < tmp.size(); l++ ){
            diff = tmp[l] - tmp[l-1]-1;
            if ( diff > max_diff ){
                max_pos = l;
                max_diff = diff;
            }
        }
        if ( max_diff%2 == 0 ){
            min = max_diff/2 -1;
            max = min + 1;
        }
        else{
            max = (max_diff - 1)/2;
            min = max;
        }
        cout << "Case #" << i+1 << ": " << max << " " << min << endl;
        tmp.erase( tmp.begin(), tmp.end() );
    }

}
