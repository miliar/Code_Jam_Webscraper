#include <bits/stdc++.h>
#define el '\n'
using namespace std;

string n;

bool tidy(string x){
  for (int i = 1; i < x.size(); i++) if (x[i] < x[i-1]) return false;
  return true;
}

string solve(){
  string ans = n;

  while (!tidy(ans)){
    while (ans[0] == '0' && ans.size()) ans.erase(ans.begin());
    
    for (int i = 1; i < ans.size(); i++)
      if (ans[i] < ans[i-1]){
	for (int j = i; j < ans.size(); j++) ans[j] = '9';
	ans[i-1]--;
      }	
  }

  while (ans[0] == '0' && ans.size()) ans.erase(ans.begin());

  return ans;
}

int main ()
{
  ios_base::sync_with_stdio(0); cin.tie(0);

  int t;
  cin >> t;
    
  for (int test = 1; test <= t; test++){
    cin >> n;
    cout << "Case #" << test << ": " << solve() << el;
  }
  
  return 0;
}
