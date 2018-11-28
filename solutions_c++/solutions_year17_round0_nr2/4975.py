#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;


int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  string s;
  //  int k;
  for (int cntt = 1; cntt <= t; cntt++) 
  {
    cin >> s;
    //    cout << s << k;
    int l = s.length();
    int  *S = new int[l];
    // cout << l << k;
    for (int i = 0; i < l; i++) S[i] = s[i] - '0';//s[i]=='-') S[i] = 0; else S[i] = 1;
    int k = 0;
    for (int i = 1; i < l; i++)
    {
      if (S[i] > S[i - 1]) k = i;
      if (S[i] < S[i - 1]) 
      {
        S[k]--;
	for (int j = k + 1; j < l; j++) S[j] = 9;
      }
    }
      
    cout << "Case #" << cntt << ": ";
    int j = 0;
    while (S[j] == 0) j++;
    for (int i = j; i < l; i++) cout << S[i];
    cout << endl;
    /*}
    else
    {
      cout << "Case #"<< cntt<< ": "<< "IMPOSSIBLE" << endl;

      }*/
    
  }  
  return 0;
}
