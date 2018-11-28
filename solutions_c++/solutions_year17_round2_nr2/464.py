//
// Created by pierre on 08.04.17.
//

#include <iostream>
#include <algorithm>

using namespace std;

string solveOnes();
char getLetterOnes(int second);
char getLetterTwos(int second);
int getIndex(char i);

int ones[3];
int twos[3];
int n;


int main()
{
  int ilez;
  cin >> ilez;
  for (int aa = 0; aa < ilez; aa++)
  {
    cin >> n >> ones[0] >> twos[2] >> ones[1] >> twos[0] >> ones[2] >> twos[1];

    for (int i = 0; i < 3; i++)
    {
      ones[i] -= twos[i];
    }

    string s = solveOnes();

    cout << "Case #" << aa + 1 << ": ";

    if (s.size() == 0)
    {
      int licznik = 0;
      int nr;
      for (int i = 0; i < 3; i++)
        if (twos[i] > 0)
        {
          licznik++;
          nr = i;
        }

      if (licznik != 1)
      {
        cout << "IMPOSSIBLE";
      }
      else
      {
        for (int i = 0; i < twos[nr]; i++)
        {
          cout << getLetterOnes(nr) << getLetterTwos(nr);
        }
      }
    }
    else
    {
      if (s[0] == 'I')
      {
        cout << s;
      }
      else
      {
        for (int i = 0; i < s.size(); i++)
        {
          if (twos[getIndex(s[i])] > 0)
          {
            twos[getIndex(s[i])]--;
            cout << s[i];
            cout << getLetterTwos(getIndex(s[i]));
            cout << s[i];
          }
          else
          {
            cout << s[i];
          }
        }
      }
    }
    cout << endl;
  }
}

string solveOnes()
{
  pair<int, int> t[3];
  int sum = 0;
  for (int i = 0; i < 3; i++)
  {
    if (ones[i] < 0) return "IMPOSSIBLE";
    t[i].first = ones[i];
    t[i].second = i;
    sum += t[i].first;
  }

  sort(t, t + 3);
  reverse(t, t + 3);

  if (t[0].first > t[1].first + t[2].first)
    return "IMPOSSIBLE";

  string ret;


  int last = -1;
  for (int i = 0; i < sum; i++)
  {
    int maxi = 0;
    for (int i = 1; i < 3; i++)
    {
      if (maxi == last || t[i].first > t[maxi].first)
      {
        maxi = i;
      }
    }
    t[maxi].first--;
    last = maxi;
    ret += getLetterOnes(t[maxi].second);
  }

  return ret;

}


int getIndex(char i)
{
  if (i == 'R')
    return 0;
  else if (i == 'Y')
    return 1;
  else return 2;
}

char getLetterOnes(int second)
{
  if (second == 0)
    return 'R';
  else if (second == 1)
    return 'Y';
  else return 'B';
}

char getLetterTwos(int second)
{
  if (second == 0)
    return 'G';
  else if (second == 1)
    return 'V';
  else return 'O';
}
