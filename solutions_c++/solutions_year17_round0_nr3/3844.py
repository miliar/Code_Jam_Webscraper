//in the name of allah
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void solve(){
        int n , k;
        scanf("%d%d" , &n , &k);      
        unordred_map<int> mp;      
        st.insert(0);
        st.insert(-n);
        k--;
        while(k--){
                int d = *st.begin();
                d = -d;
                st.erase(st.begin());
                st.insert(-(d-1)/2);
                st.insert(-(d/2));
        }
        int d = *st.begin();
        d = -d;        
        printf("%d %d\n" , d/2 , (d - !(d&1))/2);
}

int main(){
        int t , it=0;
        scanf("%d" , &t);
        while(++it <= t){
                printf("Case #%d: " , it);
                solve();
        }
        return 0;
}
