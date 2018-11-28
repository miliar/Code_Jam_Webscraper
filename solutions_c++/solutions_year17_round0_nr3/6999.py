#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    long long int a,b;
    long long int bes=0,besL=0;

    for(int i=0; i<n; i++){
        cin >> a >> b;
        multiset<long long int> mp{0,a+1};
        multiset<long long int>::iterator it,tmp1,tmp2;
        for(int j=0; j<b; j++){
            bes=0;
            besL=0;
            re:
            auto end = mp.end();
            auto sec = mp.begin();
            end--;
            sec++;
            for(it = mp.begin(); it != end; it++){
                if(it==mp.begin() && *sec-*it==1){
                    mp.erase(mp.begin());
                    goto re;
                }
                if(besL < *sec-*it) {
                    besL = (*sec - *it) -1;
                    bes = ((*it + *sec)+1) / 2;
                }
                sec++;
            }
            it = mp.insert(bes);
        }
        //it = mp.find(bes);
        tmp1 = it,tmp2 = it;
        tmp1--,tmp2++;
        cout << "Case #"<<i+1<<": "<<max(*tmp2-*it,*it-*tmp1)-1 <<" "<< min(*tmp2-*it,*it-*tmp1)-1 << endl;
    }
    return 0;
}