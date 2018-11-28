#include <bits/stdc++.h>

using namespace std;

bool isTidy(string s)  {
  for(int i=0; i < s.length() - 1; i++)
    if(s[i] > s[i+1]) return false;
  return true;
}

int main() {
  int t, tc = 0; scanf("%d", &t);

  string s;
  bool sw;
  while(t--) {
    cin >> s;
    sw = false;

    while(!isTidy(s) && !sw) {
      for(int i=0; i<s.length() - 1; i++) {
	if(s[i] > s[i+1]) {
	  if(s[i] == '1') {
	    sw = true;
	    break;
	  } else {
	    s[i]--;
	    for(int j=i+1; j<s.length(); j++)
	      s[j] = '9';
	  }
	}
      }
    }

    if(sw) {
      cout << "Case #" << ++tc << ": ";
      for(int i=0; i<s.length() - 1; i++)
	printf("9");
      printf("\n");
    } else {
      cout << "Case #" << ++tc << ": " << s << endl;
    }
  }
  
  return 0;
}
