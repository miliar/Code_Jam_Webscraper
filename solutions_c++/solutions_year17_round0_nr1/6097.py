#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int n, x, j, sixe, happy, koniec;
string word;
int main()
 {
     freopen("pan.txt", "r", stdin);
    freopen("panodp.txt", "w", stdout);
     cin >> n;
      for(int i = 1; i<=n; i++)
      {
          cin >> word;
          cin >> sixe;
          x = 0;
          happy = 0;
          koniec = 0;
          while(x<word.size())
          {
              if(word.at(x)=='+')
              {
                  x++;
                 happy++;
                 continue;
              }
              if(word.at(x)=='-')
              {
                  koniec++;
                  j=0;
                  while(j<sixe)
                  {

                      if(x+j<word.size())
                      {
                          if(word.at(x+j)=='+') word.at(x+j)='-';
                          else word.at(x+j)='+';
                      }
                      else{happy--; break;}
                      j++;
                  }
              }
          }
          if(happy==word.size()) cout << "Case #" << i << ": " << koniec << "\n";
          else cout<< "Case #" << i << ": IMPOSSIBLE\n";
      }
      return 0;
}
