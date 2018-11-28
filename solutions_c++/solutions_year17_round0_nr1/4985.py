#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;


int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  string s;
  int k;
  for (int cntt = 1; cntt <= t; cntt++) 
  {
    cin >> s >> k;
    //    cout << s << k;
    int l = s.length();
    int  *S = new int[l];
    // cout << l << k;
    for (int i = 0; i < l; i++) 
      if (s[i]=='-') S[i] = 0; else S[i] = 1;
    //for (int i = 0; i < l; i++) cout << S[i];
    //cout << "dasd";
    int cnt = 0;
    for (int i = 0; i + k - 1 < l; i++)
      if (S[i] == 0) 
      {
	cnt++;
	for (int j = i; j <= i + k - 1; j++) S[j] = 1 - S[j];
      }
    bool w = 1;
    for (int i = 0; i < l; i++)
      { if (S[i] == 0) { w = 0; break; } }
    if (w)
    {
      cout << "Case #" << cntt << ": " << cnt << endl;
    }
    else
    {
      cout << "Case #"<< cntt<< ": "<< "IMPOSSIBLE" << endl;

    }
    
  }  
  return 0;
}
