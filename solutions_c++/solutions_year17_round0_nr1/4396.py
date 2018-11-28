#include <bits/stdc++.h>
using namespace std;
 
#define N 100005
#define fi first
#define se second
#define MOD 1000000007
 
#define pb push_back
 
#define ll long long
 
#define eps 1.0e-7
#define inf 1e9 + 5
#define double long double

#define pp pair<int,int>


int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t,i,n,m,k;
  string s ;

  cin>>t ;
  for(int i = 1; i <= t; i++)
  {
  	cin >> s >> k;
  	int n = s.size();
  	int ans = 0;
  	for(int j = 0; j < n - k + 1; j++){
  		if(s[j] == '-'){
  			ans++;
  			for(int w = j; w < j + k && w < n; w++){
  				if(s[w] == '-') s[w] = '+';
  				else s[w] = '-';
  			}
  		}
  	} 
  	bool chk = true;
  	for(int j = 0; j < n; j++){
  		if(s[j] == '-') chk = false;
  	}

  	if(chk){
  		cout << "Case #" << i << ": ";
  		cout << ans << "\n";
  	} else{
  		cout << "Case #" << i << ": ";
  		cout << "IMPOSSIBLE\n";
  	}

  }



}