#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <iomanip>
using namespace std;

vector<vector<bool> > input;
int testnum;
vector<int> destinations;
vector<int> horsenumbers;
vector<double> result;
vector<vector<string> > matrixes;

bool getInput()
{
  string testcases;
  string onecase;
  ifstream inputfile("input.txt");
  if (inputfile.is_open())
  {
    getline (inputfile, testcases);
    testnum = atoi(testcases.c_str());
    for (int i=0;i<testnum;i++)
    {
      string str;
      getline (inputfile, str);

      string buf;
      string buf1;
      stringstream ss(str);

      ss >> buf;
      destinations.push_back(atoi(buf.c_str()));
      ss >> buf1;
      horsenumbers.push_back(atoi(buf1.c_str()));

      vector<string> temp;
      vector<int> pos;
      vector<int> speed;
      vector<double> candidates;
      for (int j=0;j<horsenumbers[i];++j)
      {
        string str;
        getline(inputfile, str);
        string buf;
        string buf1;
        stringstream ss(str);

        ss >> buf;
        pos.push_back(atoi(buf.c_str()));
        ss >> buf1;
        speed.push_back(atoi(buf1.c_str()));
        //cout<<destinations[i]<<" "<<pos[j]<<" "<<speed[j]<<endl;
        double vmi = (destinations[i]-pos[j])/(double)speed[j];
        //cout<<"sub"<<vmi<<endl;

        candidates.push_back(destinations[i]/vmi);
        //<<candidates[j]<<endl;
      }
      double min=candidates[0];
      for (int k=0;k<candidates.size();k++)
      {
        if (min>candidates[k])
        {
          min=candidates[k];
        }
      }
      result.push_back(min);
    }
    inputfile.close();
    return true;
  }
  else
  {
      cout << "Unable to open file";
      return false;
  }
}
int main()
{
  testnum=0;
  getInput();
  /*for (int k=0;k<result.size();k++)
      {
        cout<<result[k]<<endl;
      }*/
  ofstream filename ("output.txt");
  filename.is_open();
  for (int j=0;j<testnum;j++)
  {
    //filename << "Case #"<<j+1<<": "<<result[j]<<"\n";
    filename << "Case #"<<j+1<<": "<<std::fixed << std::setprecision(6) << result[j]<<"\n";
    /*if (impossible)
    {
      filename << "Case #"<<j+1<<": IMPOSSIBLE";
    }
    else
    {
      filename << "Case #"<<j+1<<": "<<switchcounter;
    }
    //if (j!=testnum-1)
      {
          filename <<"\n";
      }*/
  }
  return 0;
}
