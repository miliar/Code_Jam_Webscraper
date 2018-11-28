#include<bits/stdc++.h>
#define lli long long int
#define test()  int test;cin>>test;while(test--)
const lli MOD = 1000000007ll;

using namespace std;

int main() {
  	freopen("in", "r", stdin);
  	freopen("out", "w", stdout);
	std::ios_base::sync_with_stdio(false);
  	int tt;
  	cin >> tt;
  	for (int qq = 1; qq <= tt; qq++) {
    	cout << "Case #" << qq << ": ";
    	int n,k;
        cin >> n >> k;
        if(k==1){
            cout << max(n/2,n-(n/2)-1)<<" "<<min(n/2,n-(n/2)-1)<<endl;
            continue;
        }
        
        multiset<int> mt;
        multiset<int>::iterator it;
        mt.insert(n/2);
        mt.insert(n-(n/2)-1);
        for(int i=2;i<k;i++){
            multiset<int>::reverse_iterator rit=mt.rbegin();
            mt.insert(*rit/2);
            mt.insert(*rit - (*rit/2)-1);
            it=mt.find (*rit);
            mt.erase (it);
           // mt.erase(*rit);
        }
        multiset<int>::reverse_iterator rt=mt.rbegin();
        cout << max(*rt/2,*rt - (*rt/2)-1) << " " << min(*rt/2,*rt - (*rt/2)-1)<<endl;
    }
  return 0;
}
