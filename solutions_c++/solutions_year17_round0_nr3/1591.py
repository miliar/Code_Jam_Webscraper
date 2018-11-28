#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<set>
using namespace std;
//int m[6];
//int ma[6];
//long long getans(long long N){
//   
//    return ans;
//}

int main()
{
    freopen ("/Users/Victor/Desktop/myfile.txt","w",stdout);
    freopen ("/Users/Victor/Desktop/C-large.in","r",stdin);
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        
        long long N, K;
        cin >> N >> K;
        
//        map<long long, int> v;
//        long long k = K;
        long long count = K;
//        v.push_back(N);
//        while (k) {
//            count ++;
//            k >> 1;
//        }
        long long l=N;
        long long s=N;
        long long lc = 1;
        long long sc = 0;
//        for (int j =0; j<k; j++) {
        
        while (count>(lc+sc)) {
            if (l==s) {
                if (l%2) {
                    l = l/2;
                    s = s/2;
                    lc = lc*2;
                    sc = 0;
                }
                else{
                    l = l/2;
                    s = s/2-1;
                    lc = lc;
                    sc = lc;
                }
            }
            else{
                if (l%2) {
                    l = l/2;
                    s = s/2-1;
                    lc = lc*2+sc;
                    sc = sc;
                }
                else{
                    l = l/2;
                    s = s/2;
                    lc = lc;
                    sc = sc*2+lc;
                }
            }
            count -= (lc+sc)/2;
        }
//        count += (lc+sc)/2;
        long long y,z;
//        cout<<lc<<" "<<sc << " "<<l<<" "<<s<<" "<<count<<endl;
        if (count>lc) {
            if (s%2) {
                y = s/2;
                z = s/2;
            }
            else{
                y = s/2;
                z = s/2-1;
            }
        }
        else{
            if (l%2) {
                y = l/2;
                z = l/2;
            }
            else{
                y = l/2;
                z = l/2-1;
            }
        }

        if (y<0) {
            y=0;
        }
        if (z<0) {
            z=0;
        }
    
        cout << "Case #"<<i+1<<": "<<y<<" "<<z<<endl;
    }
    return 0;
}

