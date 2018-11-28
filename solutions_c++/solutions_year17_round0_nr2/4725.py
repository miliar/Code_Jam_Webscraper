#include<bits/stdc++.h>
#define lli long long int
#define test()  int test;cin>>test;while(test--)
const lli MOD = 1000000007ll;

using namespace std;

int main() {
  	freopen("in", "r", stdin);
  	freopen("out", "w", stdout);
	std::ios_base::sync_with_stdio(false);
  	lli tt;
  	cin >> tt;
  	for (int qq = 1; qq <= tt; qq++) {
    		cout << "Case #" << qq << ": ";
            string s;
            cin >> s;
            lli l = s.length();
           // cout << l;
            for(int i=l-2;i>=0;i--){
                if(s[i]>s[i+1]){
                //    cout << s[i];
                    s[i] = s[i] - 1;
                    for(int j=i+1;j<l;j++){
                        s[j] = '9';
                    }
                }
            }
            int h=0;
            for(int i=0;i<l;i++){
                if(s[i]=='0' && h==0){
                    continue;
                }
                if(s[i]!='0'){
                    cout << s[i];
                    h=1;
                }
            }
            cout <<  endl;
    }
  return 0;
}
