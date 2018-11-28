#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <algorithm>
using namespace std;

string add_one(string & in)
{
  //assume in consists of a bunch of digits
  //with no left zeros
  //generate a string which is one larger

  int N = in.length();

  for (int i=N-1; i >= 0; i--)
  {
    if (in[i] != '9')  
    {
      in[i] = in[i] + 1; 
      for (int j=i+1; j <= N-1; j++)  {in[j] = '0';}
      return in; 
      //yes, in char order
    }
  }

  //it's all nines
  string plusone;
  plusone.resize(N+1);
  plusone[0] = '1';
  for (int i=1; i <=N; i++)
  {
    plusone[i] = '0';
  }
  return plusone;
}

bool is_tidy(string & in)
{
  //assume in consists of a bunch of digits
  //with no left zeros
  //check if in is tidy

  int N = in.size();
  for (int i=1; i <= N-1; i++)
  {
    if (in[i] < in[i-1])  {return false;}
  }
  return true;
}

string next_tidy(string & in)
{
  //assume in consists of a bunch of digits
  //with no left zeros
  //generate the next tidy number string

  if (is_tidy(in))  {in = add_one(in);}

  int N = in.size();
  for (int j=1; j <= N; j++)
  {
    if (in[j] < in[j-1])  {in[j] = in[j-1];}
  }
  return in;
}

vector<string> TIDY;

void init()
{
  TIDY.resize(5000000); //should probably be 4686825 ish
  string one = "1";
  for (int i=0; i < 5000000; i++)
  {
    TIDY[i] = one;
    one = next_tidy(one);
  }
}

bool less_than_or_eq(string in1, string in2)
{
  //assume both are lots of digits
  //no leading zeros
  //return true of in1 is less than or equal to in2
  if (in1.size() > in2.size())  {return false;}
  if (in1.size() < in2.size())  {return true;}

  for (int i=0; i < in1.size(); i++)
  {
    if (in1[i] > in2[i])  {return false;}
    if (in2[i] > in1[i])  {return true;}
  }
  return true;
}

string binary_search(string in, int lo, int hi)
{
  //cout << "lo: " << lo << ", hi: " << hi << endl;
  if (lo - hi >= 2 || hi - lo <= 2)
  {
    //it's around here somewhere...
    int lolo = max(0,lo-5);
    int lohi = min(int(TIDY.size()),lo+5);
    string prevNumber = TIDY[lolo];
    assert(less_than_or_eq(prevNumber,in));
    for (int i=lolo; i <= lohi; i++)
    {
      if (!less_than_or_eq(TIDY[i], in))
      {
        return prevNumber;
      }
      prevNumber = TIDY[i];
    }
    assert(false);
  }

  int mid = (lo+hi)/2;
  //cout << "TIDY[mid]: " << TIDY[mid] << endl;

  if (less_than_or_eq(TIDY[mid], in))
  {
    return binary_search(in, mid, hi);
  }
  else
  {
    return binary_search(in, lo, mid);
  }
}

string tick(string in)
{
  return binary_search(in, 0, TIDY.size());
}

int main()
{
  init();
  int bigN;
  cin >> bigN;
  for (int i=1; i <= bigN; i++)
  {
    cout << "Case #" << i << ": ";
    string in;
    cin >> in;
    cout << tick(in) << endl;
  }
}

int ssmain()
{
  init();
  cout << "in: ";
  string in;
  cin >> in;
  cout << binary_search(in, 0, TIDY.size()-1) << endl;
  return 0;
}

int smain()
{
  //init();
  cout << "in1: ";
  string in1;
  cin >> in1;
  cout << "in2: ";
  string in2;
  cin >> in2;
  cout << "less_than_or_eq(in1, in2): " << less_than_or_eq(in1,in2) << endl;
  return 0;
}

