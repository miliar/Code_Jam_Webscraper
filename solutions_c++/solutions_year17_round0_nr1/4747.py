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
    	//	printf("Case #%d: ", qq);
            string s;
            int k,n,ans=0,i;
            cin >> s;
            cin >> k;
          //  cout << s << k;
            n = s.length();
            for(i=0;i<n;i++){
                if(s[i]=='-'){
                    if(i+k>n){
                        cout << "IMPOSSIBLE\n";
                        break;
                    }
                    for(int j=i;j<i+k;j++){
                        if(s[j]=='-'){
                            s[j] = '+';
                        }
                        else{
                            s[j] = '-';
                        }
                    }
                    ans++;
                }
            }
            if(i==n){
                cout << ans << endl;
            }
    }
  return 0;
}
