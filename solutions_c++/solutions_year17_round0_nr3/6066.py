#include<iostream>
#include<set>
using namespace std;
typedef long long ll;


int main()
{
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=0; t<T; t++) {
        int N, K;
        cin >> N >> K;
        multiset<ll> s;
        s.insert(N);
        for(int i=0; i<K; i++) {
            ll diff = *s.rbegin();
            s.erase(s.find(diff));

            int remaining = diff-1;
            int left = remaining / 2;
            s.insert(left);
            s.insert(remaining - left);
            if( i == K-1 )
                cout << "Case #" << t+1 << ": " << remaining - left << " " << left << endl;
        }
    }
    return 0;
}
