#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long int min2 (long long int a, long long int b) {
    if (a<b) return a;
    else return b;
}

long long int max2 (long long int a, long long int b) {
    if (a>b) return a;
    else return b;
}

int main()
{
    int t, i;
    long long int n, k, j, sector_max, sector_min,
    sector_size[120], sector_count[120], cycles, currsum;

    cin >> t;
    for (i=1; i<=t; i++) {
        cin >> n >> k;
        if (n==1) {
            cout << "Case #" << i << ": 0 0" << endl;
        } else {
            sector_size[0]=n;
            sector_max=n/2;
            sector_min=n/2-(1-n%2);
            sector_size[1]=sector_max;
            sector_size[2]=sector_min;
            sector_count[0]=1;
            sector_count[1]=1+n%2;
            sector_count[2]=1-n%2;
            cycles=1;
            while (sector_max>=1) {
                //cout << sector_max << " " << sector_min << endl;
                sector_max=sector_max/2;
                sector_min=sector_min/2-(1-sector_min%2);
                if (sector_max<=0) break;
                cycles+=2;
                sector_size[cycles]=sector_max;
                sector_size[cycles+1]=sector_min;
                if (sector_size[cycles-2]%2) { // last sector_max = 2m+1
                    sector_count[cycles]=sector_count[cycles-2]*2;
                    sector_count[cycles+1]=0;
                } else {  //last sector_max=2m
                    sector_count[cycles]=sector_count[cycles-2];
                    sector_count[cycles+1]=sector_count[cycles-2];
                }
                if (sector_size[cycles-1]%2) { //last sector_min = 2m+1
                    sector_count[cycles]+=0;
                    sector_count[cycles+1]+=2*sector_count[cycles-1];
                } else { //last sector_min=2m
                    sector_count[cycles]+=sector_count[cycles-1];
                    sector_count[cycles+1]+=sector_count[cycles-1];
                }
            };

            //for (j=0;j<=cycles+1;j++) cout << sector_size[j] << " " << sector_count[j] << endl;
            //cout << "Case #" << i << ": " << fsinal_sector/2 << " " << (final_sector/2)-(1-final_sector%2) << endl;
            currsum=0;
            for (j=0;j<=cycles+1;j++) {
                if (sector_size[j]>0) currsum+=sector_count[j];
                if (currsum>=k) {
                    cout << "Case #" << i << ": " << sector_size[j]/2 << " " << (sector_size[j]/2)-(1-sector_size[j]%2) << endl;
                    break;
                }
            }
        }
    }
    return 0;
}
