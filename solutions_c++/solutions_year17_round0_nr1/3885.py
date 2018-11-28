#include <fstream>
using namespace std;

int main()
{
  int T;
  ifstream in("A-large.in");
  ofstream out("output.txt");
  in>>T;
  for(int t=0; t<T; t++)
  {
    string str;
    in>>str;
    int K;
    in>>K;

    int tot = 0;
    for(int i=0; i<=str.length() - K; i++)
     if(str[i] == '-')
     {
       tot++;
       for(int j=i; j<i+K; j++)
        str[j] = (str[j] == '-') ? '+' : '-';
     }

    bool good = true;
    for(int i=0; i<str.length(); i++)
     if(str[i] == '-')
      good = false;

    if(good)
     out<<"Case #"<<(t+1)<<": "<<tot<<"\n";
    else
     out<<"Case #"<<(t+1)<<": IMPOSSIBLE\n";
  }

  in.close();
  out.close();
  return 0;
}
