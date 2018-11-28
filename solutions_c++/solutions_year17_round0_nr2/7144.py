#include <iostream>
#include <vector>
#include <string>
using namespace std;
typedef unsigned long long ull;
vector<ull> v;
void generate (void) {
    int digits = 18,prev, curr ;
    //Lets fill single  digits first
    for ( int i = 1; i <= 9; i++)
        v.push_back(i);
    prev = 0;
    curr = 9;

    // 1 digit is already done.. 
    //so we have to take care only for more than 2 digits
    for (int i = 1;i < digits; i++) {
          //prev and curr denote the range of previous set of
          // digits in the vector.
          for ( int j = prev; j< curr; j++) {
            for ( int k = 1; k <=9; k++) {
                if ( (v[j]%10) <= k )
                    v.push_back( (v[j]*10) + k);
            }
          }
          prev= curr;
          curr = v.size();
    }
    //for ( int i = 0; i < v.size(); i++)
    //    cout<<v[i]<<" ";
    //cout<<"TOPGUN : "<<v.size()<<endl;    
}

int main() {
	int T,len;
	cin>>T;
    generate();
    len = v.size();
	for (int cases = 1; cases <= T;cases++) {
        ull n,last_tidy;
        cin>>n;
        for(int i = 0; i < len; i++) {
            if ( v[i] <= n)
                last_tidy = v[i];
            else break;    
        }
        cout<<"Case #"<<cases<<": "<<last_tidy<<endl;
	}
    
	return 0;
}
