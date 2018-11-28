#include<iostream>
#include<cstring>
#include<algorithm>

#define int long long

using namespace std;

bool arr[1000];
int cl[1000];
int cr[1000];

#undef int
int main(void) {
#define int long long
    
    int T; cin >> T;
    int ca = 0;
    while(T--) {
        int n,k; cin >> n >> k;
        for(int i=0; i<1000; i++) {
            arr[i] = false;
            cl[i] = i;
            cr[i] = n-i-1;
        }
        
        int l,r,idx = 0;
        
        for(int i=0; i<k; i++) {
            
            l=r=-1;
            for(int j=0; j<n; j++) {
                if(arr[j]) continue;
                if(min(cr[j], cl[j]) > min(l,r)) {
                    l=cl[j];
                    r=cr[j];
                    idx = j;
                } else if(min(cr[j], cl[j]) == min(l,r)) {
                    if(max(cr[j], cl[j]) > max(l,r)) {
                        l=cl[j];
                        r=cr[j];
                        idx = j;
                    }
                }
            }
            arr[idx] = true;
            int j=idx+1;
            while(j<n && !arr[j]) {
                cl[j] = j-idx-1;
                j++;
            }
            j=idx-1;
            while(j>=0 && !arr[j]) {
                cr[j] = idx-j-1;
                j--;
            }
        }
        
        cout << "Case #" << ++ca << ": " << max(l,r) << " " << min(l,r) << endl;
    }
    return 0;
}