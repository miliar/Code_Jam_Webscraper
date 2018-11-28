#include <iostream>
#include <vector>

using namespace std;

class Pancake
{
  public:
  enum Val
  {
    HAPPY,
    SAD
  };

  private:
  int length;
  int flipperSize;
  vector<Val> states;
  public:
  int steps;

  Pancake(string inputStr, int flipper) : flipperSize{flipper}
  {
    steps = 0;
    length = inputStr.length();
    for(int i = 0; i < length; i++)
    {
      if(inputStr[i] == '+')
        states.push_back(HAPPY);
      else
        states.push_back(SAD);
    }
  }

  int flip()
  {
    steps = 0;
    int pos = 0;
    while(pos + flipperSize <= length)
    {
      if(states[pos] == SAD)
      {
        for(int i = pos; i < pos + flipperSize; i++)
        {
          states[i] = states[i] == SAD ? HAPPY : SAD;
        }

        steps++;
      }

      pos++;
    }

    bool allFlipped = true;
    for(auto &s : states)
    {
      if(s == SAD)
      {
        allFlipped = false;
        break;
      }
    }

    return allFlipped ? steps : -1;
  }

  void dump() const
  {
    for(auto& val : states)
    {
      cout << val;
    }

    cout << " FS: " << flipperSize << " STEPS: " << steps << endl;
  }
  
};

int main()
{
  int testCases;
  vector<Pancake> pancakes;

  string line;
  getline(cin, line);
  testCases = stoi(line);

  for(int i = 0; i < testCases; i++)
  {
    getline(cin, line);
    string delim = " ";
    string pcstr = line.substr(0, line.find(delim));
    int flipperSize = stoi(line.substr(line.find(delim), line.length()));
    Pancake p = Pancake(pcstr, flipperSize);
    pancakes.push_back(p);
  }

  int iter = 1;

  for(auto& p : pancakes)
  {
    int count = p.flip();
    if(count >= 0)
      cout << "Case #" << iter << ": " << count << endl;
    else
      cout << "Case #" << iter << ": " << "IMPOSSIBLE" << endl;
    //p.dump();
    
    iter++;
  }

}
