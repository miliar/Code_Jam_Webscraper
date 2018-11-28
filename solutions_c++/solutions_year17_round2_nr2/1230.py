#include <iostream>
#include <fstream>
using namespace std;

int next(int b, int prev, int R, int Y, int B, bool last)
{
  int q = 0;
  int best = -1;
  if((R > q || (b == 0 && R == q)) && prev != 0 && (!last || b != 0)) { best = 0; q = R; }
  if((Y > q || (b == 1 && Y == q)) && prev != 1 && (!last || b != 1)) { best = 1; q = Y; }
  if((B > q || (b == 2 && B == q)) && prev != 2 && (!last || b != 2)) { best = 2; q = B; }
  return best;
}

int getC(char c)
{
  if(c == 'R') return 0;
  if(c == 'Y') return 1;
  if(c == 'B') return 2;
}

char toC(int a)
{
  if(a == 0) return 'R';
  if(a == 1) return 'Y';
  if(a == 2) return 'B';
}

int main()
{
  int T;
  ifstream in("B-small-attempt0.in");
  ofstream out("output.txt");

  in>>T;
  for(int t=0; t<T; t++)
  {
    int N;
    in>>N;
    int R, O, Y, G, B, V;
    in>>R>>O>>Y>>G>>B>>V;

    string str = "";
    bool good = true;

    for(int i=0; i<N; i++)
    {
      int c = next(i == 0 ? -1 : getC(str[0]), i == 0 ? -1 : getC(str[i-1]), R, Y, B, i == N-1);
      if(c == 0) R--;
      if(c == 1) Y--;
      if(c == 2) B--;
      if(c == -1) { good = false; break; }
      else str += toC(c);
    }

    if(!good)
     out<<"Case #"<<(t+1)<<": IMPOSSIBLE\n";
    else
     out<<"Case #"<<(t+1)<<": "<<str<<"\n";
  }

  in.close();
  out.close();
  return 0;
}
