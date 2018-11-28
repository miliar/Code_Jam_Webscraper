#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <cstdio>
using namespace std;

void findDepth(unsigned long long int n,
               unsigned int& level, unsigned long long int& ind){
    level = 0;
    unsigned long long int u = 1;
    while(n > (u << level)){
        n -= (u << level);
        ++level;
    }
    ind = n;
}

unsigned long long int space(unsigned long long int n, unsigned long long int k){
    if( k == 1 ) return n;
    unsigned long long int value[2], counter[2], ind1, ind2,  u = 1;
    unsigned int levelN = 0, levelK = 0;
    findDepth(n, levelN, ind1);
    findDepth(k, levelK, ind2);
    value[0] = 0;
    value[1] = 1;
    counter[0] = ( u << levelN ) - ind1;
    counter[1] = ind1;
//    cout<<levelN<<' '<<ind1<<' '<<levelK<<' '<<ind2<<endl;
    while( levelN > levelK){
        --levelN;
        unsigned long long int tmp0 = value[0], tmp1 = value[1], total;
        total = ( u << levelN );
        if(counter[0] >= total ){
            value[0] = tmp0*2 + 1;
            value[1] = tmp0 + tmp1 + 1;
            counter[0] -= total;
            counter[1]  = total - counter[0];
        }
        else{
            value[0] = tmp0 + tmp1 + 1;
            value[1] = tmp1 * 2 + 1;
            counter[1] -= total;
            counter[0]  = total - counter[1];
        }
    }
    if(ind2 <= counter[1]) return value[1];
    else return value[0];
}

int main()
{
    freopen("d://C-large.in", "r", stdin);
    freopen("d://C-large.out", "w", stdout);

	int numcase;
	cin >> numcase;
//	cout<<setiosflags(ios::fixed);
//	cout<<setprecision(7);
	for(int i=0; i<numcase; i++) {
        unsigned long long int n, k, dmin, dmax;
		cin>>n>>k;
		dmax = space(n, k);
        if(dmax%2){
            dmax /=2;
            dmin = dmax;
        }
        else{
            dmax /=2;
            dmin = dmax - 1;
        }
        cout << "case #" << (i+1) << ": " << dmax << ' ' << dmin << endl;
	}
	return 0;
}
